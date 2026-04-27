from log_analyzer.analyzer import LogAnalyzer


def print_results(analyzer: LogAnalyzer) -> None:
    print("\n--- Results ---")

    print(f"Unique IP addresses: {analyzer.unique_ip_count()}")

    print("\nTop 3 most visited URLs:")
    for url, count in analyzer.top_urls():
        print(f"{url} ({count})")

    print("\nTop 3 most active IP addresses:")
    for ip, count in analyzer.top_ips():
        print(f"{ip} ({count})")