from pathlib import Path
from typing import Iterator


def read_lines(file_path: Path) -> Iterator[str]:
    """
    Reads a file line-by-line.

    Yields:
        Each line as a string.
    """
    with file_path.open("r", encoding="utf-8") as file:
        for line in file:
            yield line.strip()