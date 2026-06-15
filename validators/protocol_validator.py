# provides common packet validation functionality shared by all protocols

from packet_validation.packet import Packet


class ProtocolValidator:

    # creates the protocol validator
    def __init__(self, config: dict):
        self.config = config

    # validates that the packet is not empty
    def validate_not_empty(self, packet: Packet) -> bool:
        return not packet.is_empty()

    # validates the maximum packet size
    def validate_packet_size(self, packet: Packet) -> bool:
        max_packet_size = self.config["max_packet_size"]

        return packet.size() <= max_packet_size

    # validates the minimum packet size
    def validate_minimum_size(self, packet: Packet, minimum_size: int) -> bool:
        return packet.size() >= minimum_size