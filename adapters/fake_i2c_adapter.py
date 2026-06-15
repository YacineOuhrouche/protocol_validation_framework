# simulates an i2c adapter for protocol validation without real hardware

from typing import Dict, Optional

from adapters.base_protocol_adapter import BaseProtocolAdapter
from packet_validation.packet import Packet


class FakeI2cAdapter(BaseProtocolAdapter):

    # creates a fake i2c adapter
    def __init__(self, config: dict):
        self.config = config
        self.connected = False
        self.devices: Dict[int, Packet] = {}

    # opens the fake i2c connection
    def connect(self) -> None:
        self.connected = True

    # closes the fake i2c connection
    def disconnect(self) -> None:
        self.connected = False

    # checks if the fake i2c adapter is connected
    def is_connected(self) -> bool:
        return self.connected

    # registers a fake i2c device
    def register_device(self, address: int, packet: Packet) -> None:
        self._validate_address(address)
        self._validate_packet_size(packet)

        self.devices[address] = packet

    # sends one packet to the default fake i2c device
    def send_packet(self, packet: Packet) -> None:
        self._ensure_connected()
        self._validate_packet_size(packet)

    # receives one packet from the first registered fake i2c device
    def receive_packet(self) -> Optional[Packet]:
        self._ensure_connected()

        if not self.devices:
            return None

        first_address = next(iter(self.devices))

        return self.devices[first_address]

    # writes one packet to a fake i2c device
    def write_to_device(self, address: int, packet: Packet) -> None:
        self._ensure_connected()
        self._validate_address(address)
        self._validate_packet_size(packet)

        self.devices[address] = packet

    # reads one packet from a fake i2c device
    def read_from_device(self, address: int) -> Optional[Packet]:
        self._ensure_connected()
        self._validate_address(address)

        return self.devices.get(address)

    # scans for registered fake i2c devices
    def scan_devices(self) -> list[int]:
        self._ensure_connected()

        return list(self.devices.keys())

    # checks that the adapter is connected
    def _ensure_connected(self) -> None:
        if not self.connected:
            raise RuntimeError("i2c adapter is not connected")

    # checks that the packet does not exceed the configured max size
    def _validate_packet_size(self, packet: Packet) -> None:
        max_packet_size = self.config["max_packet_size"]

        if packet.size() > max_packet_size:
            raise ValueError("packet exceeds maximum i2c packet size")

    # checks that the i2c address is valid
    def _validate_address(self, address: int) -> None:
        address_bits = self.config["address_bits"]
        max_address = (1 << address_bits) - 1

        if address < 0 or address > max_address:
            raise ValueError("invalid i2c address")