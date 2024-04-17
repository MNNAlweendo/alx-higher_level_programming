#!/usr/bin/python3
"""Parse log entries from stdin and compute metrics."""


import sys
import signal
from collections import defaultdict


def signal_handler(sig, frame):
    """Handle keyboard interrupt (CTRL + C)."""
    print_metrics()


def print_metrics():
    """Print computed metrics."""
    print(f"Total file size: {total_size}")
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")


def parse_line(line):
    """Parse a log line and update metrics."""
    global total_size
    global status_codes

    try:
        parts = line.split()
        if len(parts) < 9:
            return

        status_code = parts[-2]
        file_size = int(parts[-1])

        total_size += file_size
        status_codes[status_code] += 1
    except ValueError:
        pass


if __name__ == "__main__":
    total_size = 0
    status_codes = defaultdict(int)

    # Register signal handler for CTRL+C
    signal.signal(signal.SIGINT, signal_handler)

    try:
        line_count = 0
        for line in sys.stdin:
            parse_line(line.strip())
            line_count += 1

            if line_count % 10 == 0:
                print_metrics()

    except KeyboardInterrupt:
        print_metrics()

