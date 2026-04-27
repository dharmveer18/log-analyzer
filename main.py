import argparse
import sys
from pathlib import Path

from log_analyzer.analyzer import LogAnalyzer
from log_analyzer.parser import parse_line
from log_analyzer.reader import read_lines
from log_analyzer.results import print_results

def validate_file(file_path: Path) -> Path | None:
    if not file_path.is_absolute() and not file_path.exists():
        print(f"'{file_path}' not found")
        return None
        # candidate = Path.cwd() / file_path.name
        # if candidate.exists():
        #     file_path = candidate

    if not file_path.is_file():
        print(f"Error: '{file_path}' is not a valid file.")
        return None

    if file_path.stat().st_size == 0:
        print(f"Error: '{file_path}' is empty.")
        return None

    return file_path


def process_file(file_path: Path) -> LogAnalyzer:
    analyzer = LogAnalyzer()
    for line in read_lines(file_path):
        entry = parse_line(line)
        if entry:
            analyzer.process(entry)
    return analyzer


def main():
    parser = argparse.ArgumentParser(description="Log Parser")
    parser.add_argument("file_path", type=Path, help="Path to the log file")
    args = parser.parse_args()

    file_path = validate_file(args.file_path)

    if not file_path:
        return
    
    result = LogAnalyzer()
    result = process_file(file_path)
    print_results(result)


if __name__ == "__main__":
    main()
