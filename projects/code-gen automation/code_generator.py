#!/usr/bin/env python3
"""
Code Generator CLI using GitHub Models (OpenAI-compatible API)

Usage:
  python code_generator.py "Program description" language

Reads the token from secret.txt (same directory) and prints the generated code.
"""

import sys
import argparse
import logging
import socket
import ssl
from urllib.parse import urlparse
from pathlib import Path
from typing import Optional
from openai import OpenAI, APIConnectionError, RateLimitError, APIStatusError

DEFAULT_ENDPOINT = "https://models.github.ai/inference"
DEFAULT_MODEL = "openai/gpt-4o-mini"


def load_token_from_secret() -> str:
    secret_path = Path("secret.txt")
    if not secret_path.exists():
        print("Error: secret.txt not found. Place your GitHub token in secret.txt")
        sys.exit(1)
    token = secret_path.read_text(encoding="utf-8").strip()
    if not token:
        print("Error: secret.txt is empty.")
        sys.exit(1)
    return token


def generate_code(program_name: str, language: str, token: str, endpoint: str = DEFAULT_ENDPOINT, model: str = DEFAULT_MODEL) -> str:
    client = OpenAI(api_key=token, base_url=endpoint, timeout=30.0)

    prompt = f"""
    Generate a complete, working {language} program for: {program_name}

    Requirements:
    - Include clear comments and minimal error handling
    - Include example usage if applicable
    - Follow best practices for {language}
    - Only return the code, no explanations or markdown formatting
    """

    # Minimal retry loop for transient network errors
    last_error: Optional[Exception] = None
    for _ in range(3):
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": f"You are an expert {language} programmer. Generate clean, well-documented code."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=2000,
                temperature=0.7,
            )
            return response.choices[0].message.content.strip()
        except (APIConnectionError, RateLimitError, APIStatusError) as e:
            last_error = e

    raise Exception(f"Failed to generate after retries: {last_error}")


def _safe_filename(program_name: str, language: str) -> str:
    base = "".join(c for c in program_name if c.isalnum() or c in (" ", "-", "_")).strip()
    base = base.replace(" ", "_").lower() or "generated_code"
    return f"{base}_in_{language.lower()}.txt"


def save_output(program_name: str, language: str, content: str) -> str:
    """Save generated content to output/<safe>_<lang>.txt and return the path."""
    out_dir = Path("output")
    out_dir.mkdir(parents=True, exist_ok=True)
    filename = _safe_filename(program_name, language)
    out_path = out_dir / filename
    out_path.write_text(content, encoding="utf-8")
    return str(out_path)

import os
def debug_connection(token: str, endpoint: str = DEFAULT_ENDPOINT) -> None:
    """Deep connectivity diagnostics with extensive logging."""
    logging.info("Starting connection diagnostics")
    logging.info("Endpoint: %s", endpoint)
    logging.info("Env HTTPS_PROXY=%s", os.environ.get("HTTPS_PROXY"))
    logging.info("Env HTTP_PROXY=%s", os.environ.get("HTTP_PROXY"))
    logging.info("Env SSL_CERT_FILE=%s", os.environ.get("SSL_CERT_FILE"))
    logging.info("Env REQUESTS_CA_BUNDLE=%s", os.environ.get("REQUESTS_CA_BUNDLE"))

    # CA bundle path (certifi if available)
    ca_path = None
    try:
        import certifi  # type: ignore
        ca_path = certifi.where()
        logging.info("certifi.where() => %s", ca_path)
    except Exception as e:
        logging.warning("certifi not available or failed: %s", repr(e))

    parsed = urlparse(endpoint)
    host = parsed.hostname or ""
    port = parsed.port or 443
    path = (parsed.path.rstrip("/") or "") + "/v1/models"
    logging.info("Resolved request target host=%s port=%d path=%s", host, port, path)

    # DNS resolution
    try:
        addrs = socket.getaddrinfo(host, port, proto=socket.IPPROTO_TCP)
        unique_ips = sorted({ai[4][0] for ai in addrs})
        logging.info("DNS A/AAAA results: %s", ", ".join(unique_ips))
    except Exception as e:
        logging.error("DNS resolution failed: %s", repr(e))

    # TLS handshake and simple GET using stdlib
    try:
        context = ssl.create_default_context()
        if ca_path:
            context.load_verify_locations(cafile=ca_path)
        with socket.create_connection((host, port), timeout=10) as sock:
            with context.wrap_socket(sock, server_hostname=host) as ssock:
                logging.info("TLS handshake OK. Cipher=%s, TLSVersion=%s", ssock.cipher(), ssock.version())
                # Minimal HTTP/1.1 request
                req = (
                    f"GET {path} HTTP/1.1\r\n"
                    f"Host: {host}\r\n"
                    f"Authorization: Bearer {token[:6]}...\r\n"
                    f"User-Agent: debug-connection-cli\r\n"
                    f"Connection: close\r\n\r\n"
                )
                ssock.sendall(req.encode("utf-8"))
                data = ssock.recv(4096)
                preview = data.decode("latin1", errors="replace")
                logging.info("Initial HTTP response bytes=%d", len(data))
                logging.debug("HTTP response preview:\n%s", preview[:1000])
    except ssl.SSLError as e:
        logging.error("TLS/SSL error: %s", repr(e))
    except Exception as e:
        logging.error("Socket/HTTP error: %s", repr(e))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate code using GitHub Models")
    parser.add_argument("program_name", help="Name or description of the program to generate")
    parser.add_argument("language", help="Programming language for the generated code")
    parser.add_argument("--log-level", default="INFO", choices=["DEBUG","INFO","WARNING","ERROR","CRITICAL"], help="Logging level")
    parser.add_argument("--debug-connect", action="store_true", help="Run deep connection diagnostics before generation")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    logging.basicConfig(
        level=getattr(logging, args.log_level.upper(), logging.INFO),
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%H:%M:%S",
    )
    token = load_token_from_secret()
    if args.debug_connect:
        debug_connection(token, DEFAULT_ENDPOINT)
    try:
        code = generate_code(args.program_name, args.language, token)
        saved_path = save_output(args.program_name, args.language, code)
        print(code)
        print(f"\nSaved to: {saved_path}")
    except KeyboardInterrupt:
        print("\nOperation cancelled.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

