# measures uart throughput using a real uart adapter

import time

from packet_validation.packet import Packet


class UartHardwareThroughputTester:

    # creates the throughput tester
    def __init__(self, adapter):
        self.adapter = adapter

    # measures transmit throughput in bytes per second
    def measure_tx_throughput(
        self,
        packet_size: int,
        packet_count: int,
    ) -> float:

        if not self.adapter.is_connected():
            self.adapter.connect()

        payload = bytes([85] * packet_size)

        start_time = time.perf_counter()

        for _ in range(packet_count):
            packet = Packet(payload=payload)
            self.adapter.send_packet(packet)

        elapsed_time = time.perf_counter() - start_time

        total_bytes = packet_size * packet_count

        if elapsed_time <= 0:
            return 0.0

        return total_bytes / elapsed_time

    # measures transmit throughput in kilobytes per second
    def measure_tx_throughput_kbps(
        self,
        packet_size: int,
        packet_count: int,
    ) -> float:

        throughput = self.measure_tx_throughput(
            packet_size,
            packet_count,
        )

        return throughput / 1024