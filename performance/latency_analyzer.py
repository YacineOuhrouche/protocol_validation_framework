# measures communication latency from packet timestamps


class LatencyAnalyzer:

    # calculates latency in milliseconds
    def calculate_latency_ms(self, start_time_ms: int, end_time_ms: int) -> int:
        if end_time_ms < start_time_ms:
            raise ValueError("end time must not be before start time")

        return end_time_ms - start_time_ms

    # calculates average latency in milliseconds
    def calculate_average_latency_ms(self, latencies_ms: list[int]) -> float:
        if not latencies_ms:
            raise ValueError("latency list must not be empty")

        return sum(latencies_ms) / len(latencies_ms)

    # calculates maximum latency in milliseconds
    def calculate_max_latency_ms(self, latencies_ms: list[int]) -> int:
        if not latencies_ms:
            raise ValueError("latency list must not be empty")

        return max(latencies_ms)

    # calculates minimum latency in milliseconds
    def calculate_min_latency_ms(self, latencies_ms: list[int]) -> int:
        if not latencies_ms:
            raise ValueError("latency list must not be empty")

        return min(latencies_ms)