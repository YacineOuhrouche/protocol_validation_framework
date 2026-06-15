# tests packet replay behavior

from adapters.fake_uart_adapter import FakeUartAdapter
from configs.config_loader import load_uart_config
from packet_validation.packet import Packet
from replay_testing.packet_recorder import PacketRecorder
from replay_testing.packet_replayer import PacketReplayer


# verifies that a capture can be loaded
def test_packet_replayer_can_load_capture(tmp_path):
    recorder = PacketRecorder()
    replayer = PacketReplayer()

    packet = Packet(
        payload=b"abc",
        sequence_id=0,
    )

    recorder.record_packet(packet)

    capture_path = tmp_path / "capture.json"
    recorder.save_capture(str(capture_path))

    packets = replayer.load_capture(str(capture_path))

    assert len(packets) == 1
    assert packets[0].payload == b"abc"


# verifies that packets can be replayed through an adapter
def test_packet_replayer_can_replay_packets():
    config = load_uart_config()
    adapter = FakeUartAdapter(config)
    replayer = PacketReplayer()

    packets = [
        Packet(payload=b"one", sequence_id=0),
        Packet(payload=b"two", sequence_id=1),
    ]

    adapter.connect()

    replayed_count = replayer.replay_packets(
        adapter,
        packets,
    )

    assert replayed_count == 2
    assert adapter.get_last_transmitted_packet().payload == b"two"