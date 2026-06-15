# tests uart packet validation rules

from configs.config_loader import load_uart_config
from packet_validation.packet import Packet
from validators.uart_validator import UartValidator


# creates a uart validator for tests
def create_validator() -> UartValidator:
    config = load_uart_config()
    return UartValidator(config)


# verifies that a valid uart packet passes validation
def test_uart_validator_accepts_valid_packet():
    validator = create_validator()
    packet = Packet(payload=bytes([170, 1, 2, 3, 85]))

    assert validator.validate_packet(packet) is True


# verifies that an empty uart packet fails validation
def test_uart_validator_rejects_empty_packet():
    validator = create_validator()
    packet = Packet(payload=b"")

    assert validator.validate_packet(packet) is False


# verifies that an oversized uart packet fails validation
def test_uart_validator_rejects_large_packet():
    validator = create_validator()
    packet = Packet(payload=bytes([170]) + b"x" * 300 + bytes([85]))

    assert validator.validate_packet(packet) is False


# verifies that a packet with the wrong start byte fails validation
def test_uart_validator_rejects_wrong_start_byte():
    validator = create_validator()
    packet = Packet(payload=bytes([0, 1, 2, 3, 85]))

    assert validator.validate_packet(packet) is False


# verifies that a packet with the wrong end byte fails validation
def test_uart_validator_rejects_wrong_end_byte():
    validator = create_validator()
    packet = Packet(payload=bytes([170, 1, 2, 3, 0]))

    assert validator.validate_packet(packet) is False