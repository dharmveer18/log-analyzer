from dataclasses import dataclass
from typing import Optional


@dataclass
class LogEntry:
    ip: str
    url: str


def parse_line(line: str) -> Optional[LogEntry]:
    """
    Parses a single log line and extracts IP and URL.

    Returns:
        LogEntry if parsing is successful, otherwise None.
    """
    try:
        parts = line.split()

        if len(parts) < 7:
            return None

        ip = parts[0]

        # Extract request part: "GET /path HTTP/1.1"
        request_part = line.split('"')[1]
        request_tokens = request_part.split()

        if len(request_tokens) < 2:
            return None

        url = request_tokens[1]

        return LogEntry(ip=ip, url=url)

    except (IndexError, ValueError):
        return None