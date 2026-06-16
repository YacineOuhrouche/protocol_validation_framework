# generates malformed protocol frames for robustness and security testing

from packet_validation.packet import Packet


class MalformedFrameGenerator:

    # creates an empty frame
    def create_empty_frame(self) -> Packet:
        return Packet(
            payload=b"",
        )

    # creates a frame larger than the allowed size
    def create_oversized_frame(self, size: int) -> Packet:
        return Packet(
            payload=b"x" * size,
        )

    # creates a frame with an invalid start byte
    def create_invalid_start_frame(self) -> Packet:
        return Packet(
            payload=bytes([0, 1, 2, 3, 85]),
        )

    # creates a frame with an invalid end byte
    def create_invalid_end_frame(self) -> Packet:
        return Packet(
            payload=bytes([170, 1, 2, 3, 0]),
        )

    # creates a frame with an invalid sequence id
    def create_invalid_sequence_frame(self) -> Packet:
        return Packet(
            payload=b"data",
            sequence_id=-1,
        )

    # creates a frame with a corrupted checksum
    def create_invalid_checksum_frame(self) -> Packet:
        return Packet(
            payload=b"data",
            checksum=999999,
        )