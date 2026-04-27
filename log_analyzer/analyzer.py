from collections import Counter
from typing import List, Tuple

from log_analyzer.parser import LogEntry


class LogAnalyzer:
    def __init__(self) -> None:
        self.ip_counts = Counter()
        self.url_counts = Counter()

    def process(self, entry: LogEntry) -> None:
        """Update counts using a single log entry."""
        self.ip_counts[entry.ip] += 1
        self.url_counts[entry.url] += 1

    def unique_ip_count(self) -> int:
        return len(self.ip_counts)

    def top_urls(self, n: int = 3) -> List[Tuple[str, int]]:
        return self.url_counts.most_common(n)

    def top_ips(self, n: int = 3) -> List[Tuple[str, int]]:
        return self.ip_counts.most_common(n)