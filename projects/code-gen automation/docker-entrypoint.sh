#!/usr/bin/env sh
set -e

# If secret.txt is not present but GITHUB_TOKEN is set, create it
if [ ! -f /app/secret.txt ] && [ -n "$GITHUB_TOKEN" ]; then
  echo "Writing token from GITHUB_TOKEN to /app/secret.txt"
  # Avoid trailing newline issues
  printf "%s" "$GITHUB_TOKEN" > /app/secret.txt
fi

# Ensure output directory exists
mkdir -p /app/output

exec python code_generator.py "$@"


