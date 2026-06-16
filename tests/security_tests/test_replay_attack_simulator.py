# tests replay attack simulation behavior

from adapters.fake_uart_adapter import FakeUartAdapter
from configs.config_loader import load_uart_config
from packet_validation.packet import Packet
from replay_testing.packet_recorder import PacketRecorder
from security.replay_attack_simulator import ReplayAttackSimulator


# verifies that replay attack packets can be loaded
def test_replay_attack_simulator_loads_packets(tmp_path):
    recorder = PacketRecorder()
    simulator = ReplayAttackSimulator()

    packet = Packet(
        payload=b"attack",
        sequence_id=0,
    )

    recorder.record_packet(packet)

    capture_path = tmp_path / "attack_capture.json"
    recorder.save_capture(str(capture_path))

    packets = simulator.load_attack_packets(str(capture_path))

    assert len(packets) == 1
    assert packets[0].payload == b"attack"


# verifies that replay attack can be executed
def test_replay_attack_simulator_executes_attack(tmp_path):
    recorder = PacketRecorder()
    simulator = ReplayAttackSimulator()
    adapter = FakeUartAdapter(load_uart_config())

    packet = Packet(
        payload=b"attack",
        sequence_id=0,
    )

    recorder.record_packet(packet)

    capture_path = tmp_path / "attack_capture.json"
    recorder.save_capture(str(capture_path))

    replayed_count = simulator.execute_replay_attack(
        adapter,
        str(capture_path),
    )

    assert replayed_count == 1
    assert adapter.get_last_transmitted_packet().payload == b"attack"