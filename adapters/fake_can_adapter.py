# simulates a can adapter for protocol validation without real hardware

from collections import deque
from typing import Deque, Optional

from adapters.base_protocol_adapter import BaseProtocolAdapter
from packet_validation.packet import Packet


class FakeCanAdapter(BaseProtocolAdapter):

    # creates a fake can adapter
    def __init__(self, config: dict):
        self.config = config
        self.connected = False
        self.rx_buffer: Deque[Packet] = deque()
        self.tx_buffer: Deque[Packet] = deque()

    # opens the fake can connection
    def connect(self) -> None:
        self.connected = True

    # closes the fake can connection
    def disconnect(self) -> None:
        self.connected = False

    # checks if the fake can adapter is connected
    def is_connected(self) -> bool:
        return self.connected

    # sends one can packet
    def send_packet(self, packet: Packet) -> None:
        self._ensure_connected()
        self._validate_packet_size(packet)
        self.tx_buffer.append(packet)

    # receives one can packet
    def receive_packet(self) -> Optional[Packet]:
        self._ensure_connected()

        if not self.rx_buffer:
            return None

        return self.rx_buffer.popleft()

    # injects a can packet into the receive buffer for tests
    def inject_received_packet(self, packet: Packet) -> None:
        self._validate_packet_size(packet)
        self.rx_buffer.append(packet)

    # returns the latest transmitted can packet
    def get_last_transmitted_packet(self) -> Optional[Packet]:
        if not self.tx_buffer:
            return None

        return self.tx_buffer[-1]

    # clears all fake can buffers
    def clear_buffers(self) -> None:
        self.rx_buffer.clear()
        self.tx_buffer.clear()

    # checks that the adapter is connected
    def _ensure_connected(self) -> None:
        if not self.connected:
            raise RuntimeError("can adapter is not connected")

    # checks that the can packet does not exceed max data length
    def _validate_packet_size(self, packet: Packet) -> None:
        max_packet_size = self.config["max_packet_size"]

        if packet.size() > max_packet_size:
            raise ValueError("packet exceeds maximum can packet size")