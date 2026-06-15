# validates packet sequence ordering and detects lost packets

from packet_validation.packet import Packet


class SequenceValidator:

    # creates the sequence validator
    def __init__(self):
        self.expected_sequence_id = 0

    # validates that the packet has the expected sequence id
    def validate_sequence(self, packet: Packet) -> bool:
        if packet.sequence_id is None:
            return False

        if packet.sequence_id != self.expected_sequence_id:
            return False

        self.expected_sequence_id += 1
        return True

    # resets the expected sequence id
    def reset(self) -> None:
        self.expected_sequence_id = 0