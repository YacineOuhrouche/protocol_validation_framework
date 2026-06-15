# validates i2c communication using i2c-specific rules

from packet_validation.packet import Packet
from validators.protocol_validator import ProtocolValidator


class I2cValidator(ProtocolValidator):

    # creates the i2c validator
    def __init__(self, config: dict):
        super().__init__(config)

    # validates the full i2c packet
    def validate_packet(self, packet: Packet) -> bool:
        if not self.validate_packet_size(packet):
            return False

        if not self.validate_not_empty(packet):
            return False

        return True

    # validates the i2c address range
    def validate_address(self, address: int) -> bool:
        address_bits = self.config["address_bits"]
        max_address = (1 << address_bits) - 1

        return 0 <= address <= max_address

    # validates that a device is expected on the bus
    def validate_expected_device(self, address: int) -> bool:
        expected_devices = self.config["expected_devices"]

        return address in expected_devices

    # validates the i2c bus speed
    def validate_bus_speed(self) -> bool:
        return self.config["bus_speed_hz"] > 0

    # validates whether clock stretching is allowed
    def validate_clock_stretching_allowed(self) -> bool:
        return self.config["clock_stretching_allowed"] is True