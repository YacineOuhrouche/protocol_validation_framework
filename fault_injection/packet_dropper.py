# simulates packet loss for protocol robustness testing

import random
from typing import Optional

from packet_validation.packet import Packet


class PacketDropper:

    # creates the packet dropper
    def __init__(self, drop_rate: float):
        if drop_rate < 0 or drop_rate > 1:
            raise ValueError("drop rate must be between 0 and 1")

        self.drop_rate = drop_rate

    # returns none when the packet is dropped
    def maybe_drop_packet(self, packet: Packet) -> Optional[Packet]:
        if random.random() < self.drop_rate:
            return None

        return packet