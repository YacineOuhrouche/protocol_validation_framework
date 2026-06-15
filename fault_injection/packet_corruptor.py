# injects bit errors into packets for protocol robustness testing

import random

from packet_validation.packet import Packet


class PacketCorruptor:

    # corrupts a random byte in the packet payload
    def corrupt_random_byte(self, packet: Packet) -> Packet:
        payload = bytearray(packet.payload)

        if len(payload) == 0:
            return packet

        index = random.randint(0, len(payload) - 1)

        payload[index] ^= 0xFF

        return Packet(
            payload=bytes(payload),
            sequence_id=packet.sequence_id,
            checksum=packet.checksum,
            timestamp_ms=packet.timestamp_ms,
        )

    # corrupts a specific byte in the packet payload
    def corrupt_byte(self, packet: Packet, index: int) -> Packet:
        payload = bytearray(packet.payload)

        if index >= len(payload):
            raise IndexError("invalid payload index")

        payload[index] ^= 0xFF

        return Packet(
            payload=bytes(payload),
            sequence_id=packet.sequence_id,
            checksum=packet.checksum,
            timestamp_ms=packet.timestamp_ms,
        )