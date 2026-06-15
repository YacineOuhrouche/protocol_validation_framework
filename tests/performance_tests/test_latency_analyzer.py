# tests latency analysis behavior

import pytest

from performance.latency_analyzer import LatencyAnalyzer


# verifies that latency is calculated
def test_latency_analyzer_calculates_latency():
    analyzer = LatencyAnalyzer()

    result = analyzer.calculate_latency_ms(
        start_time_ms=100,
        end_time_ms=150,
    )

    assert result == 50


# verifies that average latency is calculated
def test_latency_analyzer_calculates_average_latency():
    analyzer = LatencyAnalyzer()

    result = analyzer.calculate_average_latency_ms([10, 20, 30])

    assert result == 20


# verifies that maximum latency is calculated
def test_latency_analyzer_calculates_max_latency():
    analyzer = LatencyAnalyzer()

    result = analyzer.calculate_max_latency_ms([10, 20, 30])

    assert result == 30


# verifies that minimum latency is calculated
def test_latency_analyzer_calculates_min_latency():
    analyzer = LatencyAnalyzer()

    result = analyzer.calculate_min_latency_ms([10, 20, 30])

    assert result == 10


# verifies that negative latency is rejected
def test_latency_analyzer_rejects_negative_latency():
    analyzer = LatencyAnalyzer()

    with pytest.raises(ValueError):
        analyzer.calculate_latency_ms(
            start_time_ms=200,
            end_time_ms=100,
        )


# verifies that empty latency lists are rejected
def test_latency_analyzer_rejects_empty_latency_list():
    analyzer = LatencyAnalyzer()

    with pytest.raises(ValueError):
        analyzer.calculate_average_latency_ms([])