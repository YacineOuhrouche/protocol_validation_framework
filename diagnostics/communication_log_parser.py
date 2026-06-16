# parses communication logs for protocol diagnostics

from typing import List


class CommunicationLogParser:

    # creates the communication log parser
    def __init__(self):
        self.entries = []

    # parses log lines into stored entries
    def parse_lines(self, lines: List[str]) -> list[dict]:
        self.entries = []

        for line in lines:
            entry = self.parse_line(line)
            self.entries.append(entry)

        return self.entries

    # parses one communication log line
    def parse_line(self, line: str) -> dict:
        parts = line.strip().split(",")

        if len(parts) != 4:
            raise ValueError("invalid log line format")

        return {
            "timestamp_ms": int(parts[0]),
            "protocol": parts[1],
            "direction": parts[2],
            "payload": parts[3],
        }

    # returns entries matching one protocol
    def filter_by_protocol(self, protocol: str) -> list[dict]:
        return [
            entry
            for entry in self.entries
            if entry["protocol"] == protocol
        ]