# tests packet recording behavior

import json

from packet_validation.packet import Packet
from replay_testing.packet_recorder import PacketRecorder


# verifies that packets can be recorded
def test_packet_recorder_can_record_packet():
    recorder = PacketRecorder()

    packet = Packet(
        payload=b"abc",
        sequence_id=1,
    )

    recorder.record_packet(packet)

    assert len(recorder.recorded_packets) == 1


# verifies that packet recordings can be cleared
def test_packet_recorder_can_clear_packets():
    recorder = PacketRecorder()

    packet = Packet(payload=b"abc")

    recorder.record_packet(packet)

    recorder.clear()

    assert len(recorder.recorded_packets) == 0


# verifies that captures can be saved
def test_packet_recorder_can_save_capture(
    tmp_path,
):
    recorder = PacketRecorder()

    packet = Packet(
        payload=b"abc",
        sequence_id=1,
    )

    recorder.record_packet(packet)

    capture_path = tmp_path / "capture.json"

    recorder.save_capture(
        str(capture_path),
    )

    assert capture_path.exists()

    with capture_path.open(
        "r",
        encoding="utf-8",
    ) as file:
        capture = json.load(file)

    assert len(capture) == 1