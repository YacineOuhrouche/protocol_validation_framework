# records packets to json files for replay testing

import json
from pathlib import Path

from packet_validation.packet import Packet


class PacketRecorder:

    # creates the packet recorder
    def __init__(self):
        self.recorded_packets = []

    # records one packet
    def record_packet(self, packet: Packet) -> None:
        self.recorded_packets.append(
            {
                "payload": packet.to_hex(),
                "sequence_id": packet.sequence_id,
                "checksum": packet.checksum,
                "timestamp_ms": packet.timestamp_ms,
            }
        )

    # clears all recorded packets
    def clear(self) -> None:
        self.recorded_packets.clear()

    # saves recorded packets to a json file
    def save_capture(self, output_path: str) -> str:
        path = Path(output_path)

        path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with path.open(
            "w",
            encoding="utf-8",
        ) as file:
            json.dump(
                self.recorded_packets,
                file,
                indent=4,
            )

        return str(path)