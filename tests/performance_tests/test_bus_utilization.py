# tests bus utilization analysis behavior

import pytest

from performance.bus_utilization import BusUtilizationAnalyzer


# verifies that bus utilization percentage is calculated
def test_bus_utilization_calculates_percent():
    analyzer = BusUtilizationAnalyzer()

    result = analyzer.calculate_utilization_percent(
        used_bandwidth_bps=500,
        max_bandwidth_bps=1000,
    )

    assert result == 50


# verifies that bus saturation is detected
def test_bus_utilization_detects_saturation():
    analyzer = BusUtilizationAnalyzer()

    result = analyzer.is_saturated(
        used_bandwidth_bps=900,
        max_bandwidth_bps=1000,
        saturation_limit_percent=80,
    )

    assert result is True


# verifies that non saturated bus is detected
def test_bus_utilization_detects_non_saturation():
    analyzer = BusUtilizationAnalyzer()

    result = analyzer.is_saturated(
        used_bandwidth_bps=500,
        max_bandwidth_bps=1000,
        saturation_limit_percent=80,
    )

    assert result is False


# verifies that invalid max bandwidth is rejected
def test_bus_utilization_rejects_invalid_max_bandwidth():
    analyzer = BusUtilizationAnalyzer()

    with pytest.raises(ValueError):
        analyzer.calculate_utilization_percent(
            used_bandwidth_bps=500,
            max_bandwidth_bps=0,
        )


# verifies that negative used bandwidth is rejected
def test_bus_utilization_rejects_negative_used_bandwidth():
    analyzer = BusUtilizationAnalyzer()

    with pytest.raises(ValueError):
        analyzer.calculate_utilization_percent(
            used_bandwidth_bps=-1,
            max_bandwidth_bps=1000,
        )