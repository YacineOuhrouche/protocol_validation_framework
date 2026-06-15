# calculates communication bus utilization for protocol performance validation


class BusUtilizationAnalyzer:

    # calculates bus utilization percentage
    def calculate_utilization_percent(
        self,
        used_bandwidth_bps: float,
        max_bandwidth_bps: float,
    ) -> float:
        if max_bandwidth_bps <= 0:
            raise ValueError("max bandwidth must be greater than zero")

        if used_bandwidth_bps < 0:
            raise ValueError("used bandwidth must not be negative")

        return (used_bandwidth_bps / max_bandwidth_bps) * 100

    # checks whether bus utilization exceeds a limit
    def is_saturated(
        self,
        used_bandwidth_bps: float,
        max_bandwidth_bps: float,
        saturation_limit_percent: float,
    ) -> bool:
        utilization = self.calculate_utilization_percent(
            used_bandwidth_bps,
            max_bandwidth_bps,
        )

        return utilization >= saturation_limit_percent