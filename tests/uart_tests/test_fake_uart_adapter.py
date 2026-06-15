# tests the fake uart adapter behavior

import pytest

from adapters.fake_uart_adapter import FakeUartAdapter
from configs.config_loader import load_uart_config
from packet_validation.packet import Packet


# creates a fake uart adapter for tests
def create_adapter() -> FakeUartAdapter:
    config = load_uart_config()
    return FakeUartAdapter(config)


# verifies that the fake uart adapter can connect
def test_fake_uart_adapter_can_connect():
    adapter = create_adapter()

    adapter.connect()

    assert adapter.is_connected() is True


# verifies that the fake uart adapter can disconnect
def test_fake_uart_adapter_can_disconnect():
    adapter = create_adapter()

    adapter.connect()
    adapter.disconnect()

    assert adapter.is_connected() is False


# verifies that the fake uart adapter can send a packet
def test_fake_uart_adapter_can_send_packet():
    adapter = create_adapter()
    packet = Packet(payload=b"hello")

    adapter.connect()
    adapter.send_packet(packet)

    assert adapter.get_last_transmitted_packet() == packet


# verifies that the fake uart adapter can receive a packet
def test_fake_uart_adapter_can_receive_packet():
    adapter = create_adapter()
    packet = Packet(payload=b"data")

    adapter.connect()
    adapter.inject_received_packet(packet)

    assert adapter.receive_packet() == packet


# verifies that sending fails when the adapter is disconnected
def test_fake_uart_adapter_rejects_send_when_disconnected():
    adapter = create_adapter()
    packet = Packet(payload=b"hello")

    with pytest.raises(RuntimeError):
        adapter.send_packet(packet)


# verifies that oversized packets are rejected
def test_fake_uart_adapter_rejects_large_packet():
    adapter = create_adapter()
    packet = Packet(payload=b"x" * 300)

    adapter.connect()

    with pytest.raises(ValueError):
        adapter.send_packet(packet)


# verifies that buffers can be cleared
def test_fake_uart_adapter_can_clear_buffers():
    adapter = create_adapter()
    packet = Packet(payload=b"hello")

    adapter.connect()
    adapter.send_packet(packet)
    adapter.inject_received_packet(packet)
    adapter.clear_buffers()

    assert adapter.get_last_transmitted_packet() is None
    assert adapter.receive_packet() is None