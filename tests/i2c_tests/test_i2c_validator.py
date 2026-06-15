# tests i2c validation rules

from configs.config_loader import load_i2c_config
from packet_validation.packet import Packet
from validators.i2c_validator import I2cValidator


# creates an i2c validator for tests
def create_validator() -> I2cValidator:
    config = load_i2c_config()
    return I2cValidator(config)


# verifies that a valid i2c packet passes validation
def test_i2c_validator_accepts_valid_packet():
    validator = create_validator()
    packet = Packet(payload=b"i2c data")

    assert validator.validate_packet(packet) is True


# verifies that an empty i2c packet fails validation
def test_i2c_validator_rejects_empty_packet():
    validator = create_validator()
    packet = Packet(payload=b"")

    assert validator.validate_packet(packet) is False


# verifies that an oversized i2c packet fails validation
def test_i2c_validator_rejects_large_packet():
    validator = create_validator()
    packet = Packet(payload=b"x" * 300)

    assert validator.validate_packet(packet) is False


# verifies that a valid i2c address passes validation
def test_i2c_validator_accepts_valid_address():
    validator = create_validator()

    assert validator.validate_address(80) is True


# verifies that an invalid i2c address fails validation
def test_i2c_validator_rejects_invalid_address():
    validator = create_validator()

    assert validator.validate_address(200) is False


# verifies that an expected i2c device passes validation
def test_i2c_validator_accepts_expected_device():
    validator = create_validator()

    assert validator.validate_expected_device(80) is True


# verifies that an unexpected i2c device fails validation
def test_i2c_validator_rejects_unexpected_device():
    validator = create_validator()

    assert validator.validate_expected_device(10) is False


# verifies that i2c bus speed passes validation
def test_i2c_validator_accepts_bus_speed():
    validator = create_validator()

    assert validator.validate_bus_speed() is True


# verifies that clock stretching setting passes validation
def test_i2c_validator_accepts_clock_stretching_allowed():
    validator = create_validator()

    assert validator.validate_clock_stretching_allowed() is True