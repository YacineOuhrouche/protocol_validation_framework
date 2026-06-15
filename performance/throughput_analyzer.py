# measures protocol throughput from transmitted packet data


class ThroughputAnalyzer:

    # calculates throughput in bytes per second
    def calculate_bytes_per_second(self, total_bytes: int, elapsed_seconds: float) -> float:
        if elapsed_seconds <= 0:
            raise ValueError("elapsed seconds must be greater than zero")

        return total_bytes / elapsed_seconds

    # calculates throughput in bits per second
    def calculate_bits_per_second(self, total_bytes: int, elapsed_seconds: float) -> float:
        bytes_per_second = self.calculate_bytes_per_second(total_bytes, elapsed_seconds)

        return bytes_per_second * 8

    # calculates throughput from a list of packet sizes
    def calculate_packet_throughput(self, packet_sizes: list[int], elapsed_seconds: float) -> float:
        total_bytes = sum(packet_sizes)

        return self.calculate_bytes_per_second(total_bytes, elapsed_seconds)