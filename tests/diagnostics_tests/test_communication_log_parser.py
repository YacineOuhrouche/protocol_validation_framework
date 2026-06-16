# tests communication log parsing behavior

import pytest

from diagnostics.communication_log_parser import CommunicationLogParser


# verifies that one log line can be parsed
def test_log_parser_parses_line():
    parser = CommunicationLogParser()

    entry = parser.parse_line("100,uart,tx,68656c6c6f")

    assert entry["timestamp_ms"] == 100
    assert entry["protocol"] == "uart"
    assert entry["direction"] == "tx"
    assert entry["payload"] == "68656c6c6f"


# verifies that multiple log lines can be parsed
def test_log_parser_parses_lines():
    parser = CommunicationLogParser()

    entries = parser.parse_lines(
        [
            "100,uart,tx,68656c6c6f",
            "120,spi,rx,776f726c64",
        ]
    )

    assert len(entries) == 2


# verifies that protocol filtering works
def test_log_parser_filters_by_protocol():
    parser = CommunicationLogParser()

    parser.parse_lines(
        [
            "100,uart,tx,68656c6c6f",
            "120,spi,rx,776f726c64",
        ]
    )

    entries = parser.filter_by_protocol("uart")

    assert len(entries) == 1
    assert entries[0]["protocol"] == "uart"


# verifies that invalid log lines are rejected
def test_log_parser_rejects_invalid_line():
    parser = CommunicationLogParser()

    with pytest.raises(ValueError):
        parser.parse_line("invalid log")