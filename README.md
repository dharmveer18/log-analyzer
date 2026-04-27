# Log-Analyzer

A modular/extensible CLI tool to parse logs and report unique IPs, most visited URLs, and most active clients.

## Installation

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Git Bash on Windows
ource .venv/Scripts/activate 

# Linux / macOS
source .venv/bin/activate

pip install -e .[dev]
```

## Usage

```bash
python main.py "path/to/logfile.log"
```

<!-- If only a filename is provided, the tool will search for it in the current directory:

```bash
python main.py logfile.log
``` -->

## Running Tests

```bash
pytest
```
