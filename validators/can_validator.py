# validates can messages using can-specific rules

from packet_validation.packet import Packet
from validators.protocol_validator import ProtocolValidator


class CanValidator(ProtocolValidator):

    # creates the can validator
    def __init__(self, config: dict):
        super().__init__(config)

    # validates the full can packet
    def validate_packet(self, packet: Packet) -> bool:
        if not self.validate_packet_size(packet):
            return False

        if not self.validate_not_empty(packet):
            return False

        return True

    # validates a standard can identifier
    def validate_standard_id(self, can_id: int) -> bool:
        return 0 <= can_id <= self.config["standard_id_max"]

    # validates an extended can identifier
    def validate_extended_id(self, can_id: int) -> bool:
        return 0 <= can_id <= self.config["extended_id_max"]

    # validates that the can id is expected
    def validate_expected_id(self, can_id: int) -> bool:
        return can_id in self.config["expected_ids"]

    # validates can bitrate
    def validate_bitrate(self) -> bool:
        return self.config["bitrate"] > 0

    # validates can data length
    def validate_data_length(self, packet: Packet) -> bool:
        return packet.size() <= self.config["max_data_length"]