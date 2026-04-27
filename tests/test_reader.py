from log_analyzer.reader import read_lines


def test_read_lines(tmp_path):
    file = tmp_path / "test.log"
    file.write_text("line1\nline2\nline3\n")

    lines = list(read_lines(file))

    assert lines == ["line1", "line2", "line3"]


def test_empty_file(tmp_path):
    file = tmp_path / "empty.log"
    file.write_text("")

    lines = list(read_lines(file))

    assert lines == []