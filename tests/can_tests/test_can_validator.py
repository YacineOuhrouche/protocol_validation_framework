# tests can validation rules

from configs.config_loader import load_can_config
from packet_validation.packet import Packet
from validators.can_validator import CanValidator


# creates a can validator for tests
def create_validator() -> CanValidator:
    config = load_can_config()
    return CanValidator(config)


# verifies that a valid can packet passes validation
def test_can_validator_accepts_valid_packet():
    validator = create_validator()
    packet = Packet(payload=b"12345678")

    assert validator.validate_packet(packet) is True


# verifies that an empty can packet fails validation
def test_can_validator_rejects_empty_packet():
    validator = create_validator()
    packet = Packet(payload=b"")

    assert validator.validate_packet(packet) is False


# verifies that oversized can packets fail validation
def test_can_validator_rejects_large_packet():
    validator = create_validator()
    packet = Packet(payload=b"123456789")

    assert validator.validate_packet(packet) is False


# verifies that a valid standard can id passes validation
def test_can_validator_accepts_standard_id():
    validator = create_validator()

    assert validator.validate_standard_id(256) is True


# verifies that an invalid standard can id fails validation
def test_can_validator_rejects_invalid_standard_id():
    validator = create_validator()

    assert validator.validate_standard_id(3000) is False


# verifies that a valid extended can id passes validation
def test_can_validator_accepts_extended_id():
    validator = create_validator()

    assert validator.validate_extended_id(100000) is True


# verifies that an expected can id passes validation
def test_can_validator_accepts_expected_id():
    validator = create_validator()

    assert validator.validate_expected_id(256) is True


# verifies that an unexpected can id fails validation
def test_can_validator_rejects_unexpected_id():
    validator = create_validator()

    assert validator.validate_expected_id(999) is False


# verifies that can bitrate passes validation
def test_can_validator_accepts_bitrate():
    validator = create_validator()

    assert validator.validate_bitrate() is True