# validates spi transactions using spi-specific rules

from packet_validation.packet import Packet
from validators.protocol_validator import ProtocolValidator


class SpiValidator(ProtocolValidator):

    # creates the spi validator
    def __init__(self, config: dict):
        super().__init__(config)

    # validates the full spi transaction packet
    def validate_packet(self, packet: Packet) -> bool:
        if not self.validate_packet_size(packet):
            return False

        if not self.validate_not_empty(packet):
            return False

        return True

    # validates the spi mode
    def validate_mode(self) -> bool:
        return self.config["mode"] in [0, 1, 2, 3]

    # validates the spi clock speed
    def validate_clock_speed(self) -> bool:
        return self.config["clock_hz"] > 0

    # validates the spi chip select
    def validate_chip_select(self, chip_select: int) -> bool:
        chip_select_count = self.config["chip_select_count"]

        return 0 <= chip_select < chip_select_count

    # validates the spi bits per word
    def validate_bits_per_word(self) -> bool:
        return self.config["bits_per_word"] in [8, 16, 32]