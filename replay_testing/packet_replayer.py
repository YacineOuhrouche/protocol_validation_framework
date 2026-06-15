# replays packets from json capture files for replay testing

import json
from pathlib import Path
from typing import List

from packet_validation.packet import Packet


class PacketReplayer:

    # loads packets from a json capture file
    def load_capture(self, capture_path: str) -> List[Packet]:
        path = Path(capture_path)

        if not path.exists():
            raise FileNotFoundError(f"capture file not found: {capture_path}")

        with path.open("r", encoding="utf-8") as file:
            capture = json.load(file)

        packets = []

        for item in capture:
            packets.append(
                Packet(
                    payload=bytes.fromhex(item["payload"]),
                    sequence_id=item.get("sequence_id"),
                    checksum=item.get("checksum"),
                    timestamp_ms=item.get("timestamp_ms"),
                )
            )

        return packets

    # replays packets through a protocol adapter
    def replay_packets(self, adapter, packets: List[Packet]) -> int:
        count = 0

        for packet in packets:
            adapter.send_packet(packet)
            count += 1

        return count