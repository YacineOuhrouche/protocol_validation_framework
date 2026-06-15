# records and replays packets for multiple communication protocols

from adapters.fake_can_adapter import FakeCanAdapter
from adapters.fake_i2c_adapter import FakeI2cAdapter
from adapters.fake_spi_adapter import FakeSpiAdapter
from adapters.fake_uart_adapter import FakeUartAdapter
from configs.config_loader import (
    load_can_config,
    load_i2c_config,
    load_spi_config,
    load_uart_config,
)
from packet_validation.packet import Packet
from replay_testing.packet_recorder import PacketRecorder
from replay_testing.packet_replayer import PacketReplayer


# creates a fake adapter for the selected protocol
def create_adapter(protocol: str):
    if protocol == "uart":
        return FakeUartAdapter(load_uart_config())

    if protocol == "spi":
        return FakeSpiAdapter(load_spi_config())

    if protocol == "i2c":
        return FakeI2cAdapter(load_i2c_config())

    if protocol == "can":
        return FakeCanAdapter(load_can_config())

    raise ValueError("unsupported protocol")


# creates sample packets for the selected protocol
def create_sample_packets(protocol: str) -> list[Packet]:
    if protocol == "can":
        return [
            Packet(payload=b"12345678", sequence_id=0, timestamp_ms=100),
            Packet(payload=b"ABCDEFGH", sequence_id=1, timestamp_ms=120),
        ]

    return [
        Packet(payload=b"hello", sequence_id=0, timestamp_ms=100),
        Packet(payload=b"world", sequence_id=1, timestamp_ms=120),
    ]


# records sample packets for the selected protocol
def record_protocol_capture(protocol: str) -> str:
    recorder = PacketRecorder()
    packets = create_sample_packets(protocol)

    for packet in packets:
        recorder.record_packet(packet)

    return recorder.save_capture(f"captures/{protocol}_capture.json")


# replays packets for the selected protocol
def replay_protocol_capture(protocol: str) -> int:
    adapter = create_adapter(protocol)
    replayer = PacketReplayer()

    adapter.connect()

    packets = replayer.load_capture(f"captures/{protocol}_capture.json")

    return replayer.replay_packets(adapter, packets)