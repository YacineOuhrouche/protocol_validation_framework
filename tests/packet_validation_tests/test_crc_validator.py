# tests crc validation behavior

from packet_validation.crc_validator import CrcValidator


# verifies that crc-16 calculation works
def test_crc_validator_calculates_crc16():
    validator = CrcValidator()
    data = b"123456789"

    assert validator.calculate_crc16(data) == 0x29B1


# verifies that crc validation accepts a correct crc
def test_crc_validator_accepts_valid_crc16():
    validator = CrcValidator()
    data = b"123456789"

    assert validator.validate_crc16(data, 0x29B1) is True


# verifies that crc validation rejects an incorrect crc
def test_crc_validator_rejects_invalid_crc16():
    validator = CrcValidator()
    data = b"123456789"

    assert validator.validate_crc16(data, 0x0000) is False