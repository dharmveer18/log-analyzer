## Pipeline Overview

| Stage | Responsibility |
|---|---|
| **Reader** | Read the log file and return one line at a time |
| **Parser** | Extract IP and URL from each line |
| **Aggregator** | Count unique IPs, top 3 most active IPs, top 3 most visited URLs |
| **Result** | Sort and print aggregated results to stdout |

---

## Design Goals

**1. Extensible**
- Input format can be changed without affecting other components
- Output format can be changed independently
- Configurable parameters (e.g. top-k results)

**2. Modular**
- Clear separation of concerns: Reader, Parser, Analyzer, Result

**3. Data Storage**
- File loading: streamed line-by-line (no full load into memory)
- Aggregator: URL, IP, and counters stored in memory
- Unique tracking: sets for unique IPs and URLs

**4. Testing**
- Unit tests and integration tests
- Edge cases: malformed lines, empty lines, duplicate lines, tie-breaking in top 3

**5. Error Handling**
- Malformed or duplicate lines: skip and log (avoid fail-fast for individual lines)
- Empty file: fail fast with a clear error message

**6. Scalability**
- Line-by-line streaming to support large files (GBs)
- In-memory aggregation is sufficient for typical use; persistent storage may be needed for very large datasets

**7. Assumptions**
- Log format is consistent with the provided example
- Only IP and URL fields are required for analysis
- Invalid lines are silently skipped
- No specific tie-breaking rule is required for top results
