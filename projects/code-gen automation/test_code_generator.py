import os
from pathlib import Path
import pytest

from code_generator import _safe_filename, save_output


@pytest.mark.parametrize(
    "program_name,language,expected",
    [
        ("Two Sum", "python", "two_sum_in_python.txt"),
        ("Hello-World!", "JS", "hello-world_in_js.txt"),
        ("  Weird   Name  ", "Go", "weird___name_in_go.txt"),
        ("", "rust", "generated_code_in_rust.txt"),
    ],
)
def test_safe_filename(program_name, language, expected):
    assert _safe_filename(program_name, language) == expected


def test_save_output_writes_file(tmp_path: Path):
    # Change CWD to temporary directory to avoid polluting repo
    cwd = os.getcwd()
    os.chdir(tmp_path)
    try:
        program = "My App"
        lang = "Python"
        content = "print('hello')\n"
        out_path = save_output(program, lang, content)

        # Ensure path is inside output dir and file exists
        assert Path(out_path).exists()
        assert Path(out_path).parent.name == "output"
        assert Path(out_path).read_text(encoding="utf-8") == content
    finally:
        os.chdir(cwd)


