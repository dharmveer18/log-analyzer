import argparse
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Log Parser")
    parser.add_argument("file_path", type=Path, help="Path to the log file")
    args = parser.parse_args()

    # If not an absolute path and doesn't exist as-is, search in cwd
    file_path = args.file_path
    if not file_path.is_absolute() and not file_path.exists():
        candidate = Path.cwd() / file_path.name
        if candidate.exists():
            file_path = candidate

    if not file_path.exists():
        print(f"Error: File '{file_path}' does not exist.", file=sys.stderr)
        sys.exit(1)

    if not file_path.is_file():
        print(f"Error: '{file_path}' is not a file.", file=sys.stderr)
        sys.exit(1)

    print(f"Processing: {file_path}")


if __name__ == "__main__":
    main()
