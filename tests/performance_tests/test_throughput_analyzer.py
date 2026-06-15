# tests throughput analysis behavior

import pytest

from performance.throughput_analyzer import ThroughputAnalyzer


# verifies that bytes per second is calculated
def test_throughput_analyzer_calculates_bytes_per_second():
    analyzer = ThroughputAnalyzer()

    result = analyzer.calculate_bytes_per_second(
        total_bytes=1000,
        elapsed_seconds=2,
    )

    assert result == 500


# verifies that bits per second is calculated
def test_throughput_analyzer_calculates_bits_per_second():
    analyzer = ThroughputAnalyzer()

    result = analyzer.calculate_bits_per_second(
        total_bytes=1000,
        elapsed_seconds=2,
    )

    assert result == 4000


# verifies that packet throughput is calculated
def test_throughput_analyzer_calculates_packet_throughput():
    analyzer = ThroughputAnalyzer()

    result = analyzer.calculate_packet_throughput(
        packet_sizes=[100, 200, 300],
        elapsed_seconds=2,
    )

    assert result == 300


# verifies that invalid elapsed time is rejected
def test_throughput_analyzer_rejects_zero_elapsed_time():
    analyzer = ThroughputAnalyzer()

    with pytest.raises(ValueError):
        analyzer.calculate_bytes_per_second(
            total_bytes=1000,
            elapsed_seconds=0,
        )