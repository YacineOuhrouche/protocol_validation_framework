# provides a real uart adapter using pyserial for hardware validation

from typing import Optional

import serial
from serial.tools import list_ports

from adapters.base_protocol_adapter import BaseProtocolAdapter
from packet_validation.packet import Packet


class RealUartAdapter(BaseProtocolAdapter):

    # creates a real uart adapter from configuration
    def __init__(self, config: dict):
        self.config = config
        self.serial_port = None

    # returns available serial ports on the system
    def list_available_ports(self) -> list[str]:
        return [
            port.device
            for port in list_ports.comports()
        ]

    # checks whether the configured uart port exists
    def port_exists(self) -> bool:
        return self.config["port"] in self.list_available_ports()

    # opens the real uart connection
    def connect(self) -> None:
        if not self.port_exists():
            available_ports = self.list_available_ports()

            raise RuntimeError(
                f"uart port not found: {self.config['port']}. "
                f"available ports: {available_ports}"
            )

        self.serial_port = serial.Serial(
            port=self.config["port"],
            baudrate=self.config["baud_rate"],
            bytesize=self.config["data_bits"],
            stopbits=self.config["stop_bits"],
            parity=self._get_parity(),
            timeout=self.config["timeout_ms"] / 1000,
        )

    # closes the real uart connection
    def disconnect(self) -> None:
        if self.serial_port is not None:
            self.serial_port.close()
            self.serial_port = None

    # checks if the real uart adapter is connected
    def is_connected(self) -> bool:
        return self.serial_port is not None and self.serial_port.is_open

    # sends one packet through the real uart adapter
    def send_packet(self, packet: Packet) -> None:
        self._ensure_connected()
        self._validate_packet_size(packet)

        self.serial_port.write(packet.payload)

    # receives one packet from the real uart adapter
    def receive_packet(self) -> Optional[Packet]:
        self._ensure_connected()

        data = self.serial_port.read(
            self.config["max_packet_size"]
        )

        if not data:
            return None

        return Packet(payload=data)

    # converts config parity into pyserial parity value
    def _get_parity(self) -> str:
        parity = self.config["parity"]

        if parity == "none":
            return serial.PARITY_NONE

        if parity == "even":
            return serial.PARITY_EVEN

        if parity == "odd":
            return serial.PARITY_ODD

        raise ValueError("unsupported uart parity")

    # checks that the adapter is connected
    def _ensure_connected(self) -> None:
        if not self.is_connected():
            raise RuntimeError("uart adapter is not connected")

    # checks that packet size does not exceed the configured maximum
    def _validate_packet_size(self, packet: Packet) -> None:
        if packet.size() > self.config["max_packet_size"]:
            raise ValueError("packet exceeds maximum uart packet size")