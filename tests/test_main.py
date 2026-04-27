import pytest
from unittest.mock import patch
from pathlib import Path

from main import main


class TestMainValidFile:
    def test_valid_file_prints_processing(self, tmp_path, capsys):
        log_file = tmp_path / "sample.log"
        log_file.write_text("log line")

        with patch("sys.argv", ["main.py", str(log_file)]):
            main()

        captured = capsys.readouterr()
        assert f"Processing: {log_file}" in captured.out

    def test_valid_file_no_stderr(self, tmp_path, capsys):
        log_file = tmp_path / "sample.log"
        log_file.write_text("log line")

        with patch("sys.argv", ["main.py", str(log_file)]):
            main()

        captured = capsys.readouterr()
        assert captured.err == ""


class TestMainNonExistentFile:
    def test_exits_with_code_1(self, tmp_path):
        missing = tmp_path / "missing.log"

        with patch("sys.argv", ["main.py", str(missing)]):
            with pytest.raises(SystemExit) as exc_info:
                main()

        assert exc_info.value.code == 1

    def test_prints_error_to_stderr(self, tmp_path, capsys):
        missing = tmp_path / "missing.log"

        with patch("sys.argv", ["main.py", str(missing)]):
            with pytest.raises(SystemExit):
                main()

        captured = capsys.readouterr()
        assert "does not exist" in captured.err


class TestMainDirectoryPath:
    def test_exits_with_code_1_for_directory(self, tmp_path):
        with patch("sys.argv", ["main.py", str(tmp_path)]):
            with pytest.raises(SystemExit) as exc_info:
                main()

        assert exc_info.value.code == 1

    def test_prints_error_to_stderr_for_directory(self, tmp_path, capsys):
        with patch("sys.argv", ["main.py", str(tmp_path)]):
            with pytest.raises(SystemExit):
                main()

        captured = capsys.readouterr()
        assert "is not a file" in captured.err
        assert str(tmp_path) in captured.err


class TestMainCwdFallback:
    def test_filename_only_found_in_cwd(self, tmp_path, capsys):
        log_file = tmp_path / "app.log"
        log_file.write_text("log line")

        with patch("sys.argv", ["main.py", "app.log"]):
            with patch("main.Path.cwd", return_value=tmp_path):
                main()

        captured = capsys.readouterr()
        assert "Processing:" in captured.out
        assert "app.log" in captured.out

    def test_filename_only_not_found_anywhere(self, tmp_path, capsys):
        with patch("sys.argv", ["main.py", "ghost.log"]):
            with patch("main.Path.cwd", return_value=tmp_path):
                with pytest.raises(SystemExit) as exc_info:
                    main()

        assert exc_info.value.code == 1
        captured = capsys.readouterr()
        assert "does not exist" in captured.err

    def test_absolute_path_does_not_fallback_to_cwd(self, tmp_path, capsys):
        # File exists in cwd but an absolute path to a missing file should still fail
        cwd_file = tmp_path / "app.log"
        cwd_file.write_text("log line")

        other_dir = tmp_path / "other"
        other_dir.mkdir()
        missing_absolute = other_dir / "app.log"

        with patch("sys.argv", ["main.py", str(missing_absolute)]):
            with patch("main.Path.cwd", return_value=tmp_path):
                with pytest.raises(SystemExit) as exc_info:
                    main()

        assert exc_info.value.code == 1
