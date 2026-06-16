# tests packet mutation behavior

from fault_injection.packet_mutator import PacketMutator
from packet_validation.packet import Packet


# verifies that the start byte can be mutated
def test_packet_mutator_mutates_start_byte():
    mutator = PacketMutator()
    packet = Packet(payload=bytes([170, 1, 2, 85]))

    mutated_packet = mutator.mutate_start_byte(packet, 0)

    assert mutated_packet.payload[0] == 0


# verifies that the end byte can be mutated
def test_packet_mutator_mutates_end_byte():
    mutator = PacketMutator()
    packet = Packet(payload=bytes([170, 1, 2, 85]))

    mutated_packet = mutator.mutate_end_byte(packet, 0)

    assert mutated_packet.payload[-1] == 0


# verifies that the sequence id can be mutated
def test_packet_mutator_mutates_sequence_id():
    mutator = PacketMutator()
    packet = Packet(payload=b"data", sequence_id=1)

    mutated_packet = mutator.mutate_sequence_id(packet, 99)

    assert mutated_packet.sequence_id == 99


# verifies that the checksum can be mutated
def test_packet_mutator_mutates_checksum():
    mutator = PacketMutator()
    packet = Packet(payload=b"data", checksum=10)

    mutated_packet = mutator.mutate_checksum(packet, 99)

    assert mutated_packet.checksum == 99


# verifies that an empty packet can be created
def test_packet_mutator_creates_empty_packet():
    mutator = PacketMutator()

    packet = mutator.create_empty_packet()

    assert packet.payload == b""


# verifies that an oversized packet can be created
def test_packet_mutator_creates_oversized_packet():
    mutator = PacketMutator()

    packet = mutator.create_oversized_packet(300)

    assert packet.size() == 300