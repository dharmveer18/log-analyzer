from log_analyzer.parser import parse_line, LogEntry


def test_parse_valid_line():
    line = '177.71.128.21 - - [10/Jul/2018:22:21:28 +0200] "GET /home HTTP/1.1" 200 3574'
    
    result = parse_line(line)

    assert result == LogEntry(ip="177.71.128.21", url="/home")


def test_parse_invalid_line_missing_parts():
    line = 'invalid log line'

    result = parse_line(line)

    assert result is None


def test_parse_invalid_request_section():
    line = '177.71.128.21 - - [date] "-" 200 123'

    result = parse_line(line)

    assert result is None


def test_parse_line_with_extra_spaces():
    line = '177.71.128.21   - -   [10/Jul/2018:22:21:28 +0200]   "GET /test HTTP/1.1"   200 3574'
    
    result = parse_line(line)

    assert result == LogEntry(ip="177.71.128.21", url="/test")


def test_parse_empty_line():
    line = ""

    result = parse_line(line)

    assert result is None