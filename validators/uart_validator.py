# validates uart packets using uart-specific rules

from packet_validation.packet import Packet
from validators.protocol_validator import ProtocolValidator


class UartValidator(ProtocolValidator):

    # creates the uart validator
    def __init__(self, config: dict):
        super().__init__(config)

    # validates the full uart packet
    def validate_packet(self, packet: Packet) -> bool:
        if not self.validate_packet_size(packet):
            return False

        if not self.validate_not_empty(packet):
            return False

        if not self.validate_start_byte(packet):
            return False

        if not self.validate_end_byte(packet):
            return False

        return True

    # validates the expected uart start byte
    def validate_start_byte(self, packet: Packet) -> bool:
        expected_start_byte = self.config["expected_start_byte"]

        if packet.is_empty():
            return False

        return packet.payload[0] == expected_start_byte

    # validates the expected uart end byte
    def validate_end_byte(self, packet: Packet) -> bool:
        expected_end_byte = self.config["expected_end_byte"]

        if packet.is_empty():
            return False

        return packet.payload[-1] == expected_end_byte