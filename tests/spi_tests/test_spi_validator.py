# tests spi validation rules

from configs.config_loader import load_spi_config
from packet_validation.packet import Packet
from validators.spi_validator import SpiValidator


# creates a spi validator for tests
def create_validator() -> SpiValidator:
    config = load_spi_config()
    return SpiValidator(config)


# verifies that a valid spi packet passes validation
def test_spi_validator_accepts_valid_packet():
    validator = create_validator()
    packet = Packet(payload=b"spi data")

    assert validator.validate_packet(packet) is True


# verifies that an empty spi packet fails validation
def test_spi_validator_rejects_empty_packet():
    validator = create_validator()
    packet = Packet(payload=b"")

    assert validator.validate_packet(packet) is False


# verifies that an oversized spi packet fails validation
def test_spi_validator_rejects_large_packet():
    validator = create_validator()
    packet = Packet(payload=b"x" * 300)

    assert validator.validate_packet(packet) is False


# verifies that a valid spi mode passes validation
def test_spi_validator_accepts_valid_mode():
    validator = create_validator()

    assert validator.validate_mode() is True


# verifies that a valid spi clock speed passes validation
def test_spi_validator_accepts_valid_clock_speed():
    validator = create_validator()

    assert validator.validate_clock_speed() is True


# verifies that a valid chip select passes validation
def test_spi_validator_accepts_valid_chip_select():
    validator = create_validator()

    assert validator.validate_chip_select(0) is True


# verifies that an invalid chip select fails validation
def test_spi_validator_rejects_invalid_chip_select():
    validator = create_validator()

    assert validator.validate_chip_select(99) is False


# verifies that valid bits per word passes validation
def test_spi_validator_accepts_valid_bits_per_word():
    validator = create_validator()

    assert validator.validate_bits_per_word() is True