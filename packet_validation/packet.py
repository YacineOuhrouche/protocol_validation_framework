# defines the shared packet model used across protocol validation

from dataclasses import dataclass
from typing import Optional


@dataclass
class Packet:
    payload: bytes
    sequence_id: Optional[int] = None
    checksum: Optional[int] = None
    timestamp_ms: Optional[int] = None

    # returns the packet payload size
    def size(self) -> int:
        return len(self.payload)

    # checks whether the packet payload is empty
    def is_empty(self) -> bool:
        return len(self.payload) == 0

    # returns the packet payload as hexadecimal text
    def to_hex(self) -> str:
        return self.payload.hex()