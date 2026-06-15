# tests packet corruption behavior

from fault_injection.packet_corruptor import PacketCorruptor
from packet_validation.packet import Packet


# verifies that a specific byte can be corrupted
def test_packet_corruptor_can_corrupt_byte():
    corruptor = PacketCorruptor()

    packet = Packet(payload=bytes([1, 2, 3]))

    corrupted_packet = corruptor.corrupt_byte(packet, 1)

    assert corrupted_packet.payload != packet.payload


# verifies that random corruption changes the payload
def test_packet_corruptor_can_corrupt_random_byte():
    corruptor = PacketCorruptor()

    packet = Packet(payload=bytes([1, 2, 3]))

    corrupted_packet = corruptor.corrupt_random_byte(packet)

    assert corrupted_packet.payload != packet.payload