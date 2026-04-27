Reader(log file) 
    Read and return one line at time.

Parse Logs(extract IP,URL)
    Parse and Return URL, IP

Aggregate (Unique IPs,  3 most active IPs,  3 most visited URLs)
    Count and store

Output(Console)
    Sort and Return Result
    stdout/print


1. Extensible- 
   Input format change
   Output format change
   Configuration(topk)

2. Modular
   Reader, Parser, Ananlyzer

3. Data Storage
   file loading - stream line-by-line
   Aggregator(URL, IP, counter) - in memory
   Set(unique IP, URL)


4. Testing
    Unit Testing
    Intergration testing

    Edge Cases
        Malformed, empty, duplicate lines
        handle ties top 3

5. Error handling
    Malformed, empty, duplicate lines - Fail
    Skip and log bad lines
    Tadeoff - avoid fail fast
     