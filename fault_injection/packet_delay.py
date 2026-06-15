# simulates delayed packet delivery for latency and timeout testing

import time

from packet_validation.packet import Packet


class PacketDelay:

    # creates the packet delay injector
    def __init__(self, delay_ms: int):
        if delay_ms < 0:
            raise ValueError("delay must not be negative")

        self.delay_ms = delay_ms

    # delays and returns the packet
    def delay_packet(self, packet: Packet) -> Packet:
        time.sleep(self.delay_ms / 1000)

        return packet