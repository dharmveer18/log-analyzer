from unittest.mock import MagicMock, patch
from pathlib import Path

from main import validate_file, process_file


class TestValidateFile:
    def test_valid_file_returns_path(self, tmp_path):
        log_file = tmp_path / "app.log"
        log_file.write_text("log line")

        result = validate_file(log_file)

        assert result == log_file

    def test_nonexistent_file_returns_none(self, tmp_path, capsys):
        missing = tmp_path / "missing.log"

        result = validate_file(missing)

        assert result is None

    def test_nonexistent_file_prints_error(self, tmp_path, capsys):
        missing = tmp_path / "missing.log"

        validate_file(missing)

        assert "not a valid file" in capsys.readouterr().out

    def test_empty_file_returns_none(self, tmp_path):
        empty = tmp_path / "empty.log"
        empty.write_text("")

        result = validate_file(empty)

        assert result is None

    def test_empty_file_prints_error(self, tmp_path, capsys):
        empty = tmp_path / "empty.log"
        empty.write_text("")

        validate_file(empty)

        assert "empty" in capsys.readouterr().out

    def test_directory_returns_none(self, tmp_path, capsys):
        result = validate_file(tmp_path)

        assert result is None

    def test_directory_prints_error(self, tmp_path, capsys):
        validate_file(tmp_path)

        assert "not a valid file" in capsys.readouterr().out

    def test_not_found_prints_searching_message(self, capsys):
        validate_file(Path("ghost_nonexistent.log"))

        assert "not found" in capsys.readouterr().out


class TestProcessFile:
    def test_returns_analyzer(self, tmp_path):
        log_file = tmp_path / "app.log"
        log_file.write_text(
            '177.71.128.21 - - [10/Jul/2018:22:21:28 +0200] "GET /home HTTP/1.1" 200 3574\n'
        )

        from log_analyzer.analyzer import LogAnalyzer
        result = process_file(log_file)

        assert isinstance(result, LogAnalyzer)

    def test_skips_invalid_lines(self, tmp_path):
        log_file = tmp_path / "app.log"
        log_file.write_text("invalid line\nanother bad line\n")

        from log_analyzer.analyzer import LogAnalyzer
        result = process_file(log_file)

        assert isinstance(result, LogAnalyzer)

