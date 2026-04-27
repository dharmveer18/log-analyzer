from log_analyzer.analyzer import LogAnalyzer
from log_analyzer.parser import LogEntry


def test_unique_ip_count():
    analyzer = LogAnalyzer()

    analyzer.process(LogEntry("1.1.1.1", "/home"))
    analyzer.process(LogEntry("2.2.2.2", "/home"))
    analyzer.process(LogEntry("1.1.1.1", "/about"))

    assert analyzer.unique_ip_count() == 2


def test_top_urls():
    analyzer = LogAnalyzer()

    analyzer.process(LogEntry("1.1.1.1", "/home"))
    analyzer.process(LogEntry("2.2.2.2", "/home"))
    analyzer.process(LogEntry("3.3.3.3", "/about"))

    result = analyzer.top_urls()

    assert result[0] == ("/home", 2)
    assert ("/about", 1) in result


def test_top_ips():
    analyzer = LogAnalyzer()

    analyzer.process(LogEntry("1.1.1.1", "/home"))
    analyzer.process(LogEntry("1.1.1.1", "/about"))
    analyzer.process(LogEntry("2.2.2.2", "/home"))

    result = analyzer.top_ips()

    assert result[0] == ("1.1.1.1", 2)
    assert ("2.2.2.2", 1) in result


def test_empty_analyzer():
    analyzer = LogAnalyzer()

    assert analyzer.unique_ip_count() == 0
    assert analyzer.top_urls() == []
    assert analyzer.top_ips() == []