# tests packet sequence validation behavior

from packet_validation.packet import Packet
from packet_validation.sequence_validator import SequenceValidator


# verifies that the first expected sequence id is accepted
def test_sequence_validator_accepts_first_sequence():
    validator = SequenceValidator()
    packet = Packet(payload=b"data", sequence_id=0)

    assert validator.validate_sequence(packet) is True


# verifies that ordered sequence ids are accepted
def test_sequence_validator_accepts_ordered_sequences():
    validator = SequenceValidator()
    packet_0 = Packet(payload=b"data", sequence_id=0)
    packet_1 = Packet(payload=b"data", sequence_id=1)

    assert validator.validate_sequence(packet_0) is True
    assert validator.validate_sequence(packet_1) is True


# verifies that missing sequence ids are rejected
def test_sequence_validator_rejects_missing_sequence():
    validator = SequenceValidator()
    packet = Packet(payload=b"data")

    assert validator.validate_sequence(packet) is False


# verifies that skipped sequence ids are rejected
def test_sequence_validator_rejects_skipped_sequence():
    validator = SequenceValidator()
    packet = Packet(payload=b"data", sequence_id=2)

    assert validator.validate_sequence(packet) is False


# verifies that reset returns the validator to sequence zero
def test_sequence_validator_can_reset():
    validator = SequenceValidator()
    packet = Packet(payload=b"data", sequence_id=0)

    assert validator.validate_sequence(packet) is True

    validator.reset()

    assert validator.expected_sequence_id == 0