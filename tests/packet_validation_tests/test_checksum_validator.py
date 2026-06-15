# tests checksum validation behavior

from packet_validation.checksum_validator import ChecksumValidator


# verifies that checksum calculation works
def test_checksum_validator_calculates_checksum():
    validator = ChecksumValidator()
    data = bytes([1, 2, 3])

    assert validator.calculate_checksum(data) == 6


# verifies that checksum validation accepts a correct checksum
def test_checksum_validator_accepts_valid_checksum():
    validator = ChecksumValidator()
    data = bytes([10, 20, 30])

    assert validator.validate_checksum(data, 60) is True


# verifies that checksum validation rejects an incorrect checksum
def test_checksum_validator_rejects_invalid_checksum():
    validator = ChecksumValidator()
    data = bytes([10, 20, 30])

    assert validator.validate_checksum(data, 99) is False


# verifies that checksum wraps to 8 bits
def test_checksum_validator_wraps_to_8_bits():
    validator = ChecksumValidator()
    data = bytes([255, 2])

    assert validator.calculate_checksum(data) == 1