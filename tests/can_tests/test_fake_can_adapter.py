# tests the fake can adapter behavior

import pytest

from adapters.fake_can_adapter import FakeCanAdapter
from configs.config_loader import load_can_config
from packet_validation.packet import Packet


# creates a fake can adapter for tests
def create_adapter() -> FakeCanAdapter:
    config = load_can_config()
    return FakeCanAdapter(config)


# verifies that the fake can adapter can connect
def test_fake_can_adapter_can_connect():
    adapter = create_adapter()

    adapter.connect()

    assert adapter.is_connected() is True


# verifies that the fake can adapter can disconnect
def test_fake_can_adapter_can_disconnect():
    adapter = create_adapter()

    adapter.connect()
    adapter.disconnect()

    assert adapter.is_connected() is False


# verifies that the fake can adapter can send a packet
def test_fake_can_adapter_can_send_packet():
    adapter = create_adapter()
    packet = Packet(payload=b"12345678")

    adapter.connect()
    adapter.send_packet(packet)

    assert adapter.get_last_transmitted_packet() == packet


# verifies that the fake can adapter can receive a packet
def test_fake_can_adapter_can_receive_packet():
    adapter = create_adapter()
    packet = Packet(payload=b"12345678")

    adapter.connect()
    adapter.inject_received_packet(packet)

    assert adapter.receive_packet() == packet


# verifies that sending fails when disconnected
def test_fake_can_adapter_rejects_send_when_disconnected():
    adapter = create_adapter()
    packet = Packet(payload=b"12345678")

    with pytest.raises(RuntimeError):
        adapter.send_packet(packet)


# verifies that oversized can packets are rejected
def test_fake_can_adapter_rejects_large_packet():
    adapter = create_adapter()
    packet = Packet(payload=b"123456789")

    adapter.connect()

    with pytest.raises(ValueError):
        adapter.send_packet(packet)


# verifies that buffers can be cleared
def test_fake_can_adapter_can_clear_buffers():
    adapter = create_adapter()
    packet = Packet(payload=b"12345678")

    adapter.connect()
    adapter.send_packet(packet)
    adapter.inject_received_packet(packet)
    adapter.clear_buffers()

    assert adapter.get_last_transmitted_packet() is None
    assert adapter.receive_packet() is None