# validates uart packets using configuration rules

from packet_validation.packet import Packet


class UartValidator:

    # creates the uart validator
    def __init__(self, config: dict):
        self.config = config

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

    # validates that the packet is not empty
    def validate_not_empty(self, packet: Packet) -> bool:
        return not packet.is_empty()

    # validates that the packet size is within the configured limit
    def validate_packet_size(self, packet: Packet) -> bool:
        max_packet_size = self.config["max_packet_size"]

        return packet.size() <= max_packet_size

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