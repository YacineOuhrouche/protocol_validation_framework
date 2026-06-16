# mutates packets for protocol security and robustness testing

from packet_validation.packet import Packet


class PacketMutator:

    # changes the first byte of a packet
    def mutate_start_byte(self, packet: Packet, new_value: int) -> Packet:
        payload = bytearray(packet.payload)

        if not payload:
            return packet

        payload[0] = new_value

        return Packet(
            payload=bytes(payload),
            sequence_id=packet.sequence_id,
            checksum=packet.checksum,
            timestamp_ms=packet.timestamp_ms,
        )

    # changes the last byte of a packet
    def mutate_end_byte(self, packet: Packet, new_value: int) -> Packet:
        payload = bytearray(packet.payload)

        if not payload:
            return packet

        payload[-1] = new_value

        return Packet(
            payload=bytes(payload),
            sequence_id=packet.sequence_id,
            checksum=packet.checksum,
            timestamp_ms=packet.timestamp_ms,
        )

    # changes the packet sequence id
    def mutate_sequence_id(self, packet: Packet, new_sequence_id: int) -> Packet:
        return Packet(
            payload=packet.payload,
            sequence_id=new_sequence_id,
            checksum=packet.checksum,
            timestamp_ms=packet.timestamp_ms,
        )

    # changes the packet checksum
    def mutate_checksum(self, packet: Packet, new_checksum: int) -> Packet:
        return Packet(
            payload=packet.payload,
            sequence_id=packet.sequence_id,
            checksum=new_checksum,
            timestamp_ms=packet.timestamp_ms,
        )

    # creates an empty malformed packet
    def create_empty_packet(self) -> Packet:
        return Packet(payload=b"")

    # creates an oversized malformed packet
    def create_oversized_packet(self, size: int) -> Packet:
        return Packet(payload=b"x" * size)