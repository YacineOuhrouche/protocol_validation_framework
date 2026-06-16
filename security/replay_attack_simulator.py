# simulates replay attacks using previously captured packets

from typing import List

from packet_validation.packet import Packet
from replay_testing.packet_replayer import PacketReplayer


class ReplayAttackSimulator:

    # creates the replay attack simulator
    def __init__(self):
        self.replayer = PacketReplayer()

    # loads captured packets for replay attack testing
    def load_attack_packets(self, capture_path: str) -> List[Packet]:
        return self.replayer.load_capture(capture_path)

    # replays captured packets through an adapter
    def execute_replay_attack(self, adapter, capture_path: str) -> int:
        packets = self.load_attack_packets(capture_path)

        if not adapter.is_connected():
            adapter.connect()

        return self.replayer.replay_packets(
            adapter,
            packets,
        )