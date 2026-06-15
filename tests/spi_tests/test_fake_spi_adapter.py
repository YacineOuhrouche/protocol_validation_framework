# tests the fake spi adapter behavior

import pytest

from adapters.fake_spi_adapter import FakeSpiAdapter
from configs.config_loader import load_spi_config
from packet_validation.packet import Packet


# creates a fake spi adapter for tests
def create_adapter() -> FakeSpiAdapter:
    config = load_spi_config()
    return FakeSpiAdapter(config)


# verifies that the fake spi adapter can connect
def test_fake_spi_adapter_can_connect():
    adapter = create_adapter()

    adapter.connect()

    assert adapter.is_connected() is True


# verifies that the fake spi adapter can disconnect
def test_fake_spi_adapter_can_disconnect():
    adapter = create_adapter()

    adapter.connect()
    adapter.disconnect()

    assert adapter.is_connected() is False


# verifies that the fake spi adapter can select a chip
def test_fake_spi_adapter_can_select_chip():
    adapter = create_adapter()

    adapter.select_chip(1)

    assert adapter.active_chip_select == 1


# verifies that invalid chip selects are rejected
def test_fake_spi_adapter_rejects_invalid_chip_select():
    adapter = create_adapter()

    with pytest.raises(ValueError):
        adapter.select_chip(99)


# verifies that the fake spi adapter can send a packet
def test_fake_spi_adapter_can_send_packet():
    adapter = create_adapter()
    packet = Packet(payload=b"hello")

    adapter.connect()
    adapter.send_packet(packet)

    assert adapter.get_last_transmitted_packet() == packet


# verifies that the fake spi adapter can receive a packet
def test_fake_spi_adapter_can_receive_packet():
    adapter = create_adapter()
    packet = Packet(payload=b"response")

    adapter.connect()
    adapter.inject_received_packet(packet)

    assert adapter.receive_packet() == packet


# verifies that the fake spi adapter can transfer a packet
def test_fake_spi_adapter_can_transfer_packet():
    adapter = create_adapter()
    tx_packet = Packet(payload=b"command")
    rx_packet = Packet(payload=b"response")

    adapter.connect()
    adapter.inject_received_packet(rx_packet)

    result = adapter.transfer_packet(tx_packet)

    assert adapter.get_last_transmitted_packet() == tx_packet
    assert result == rx_packet


# verifies that sending fails when the adapter is disconnected
def test_fake_spi_adapter_rejects_send_when_disconnected():
    adapter = create_adapter()
    packet = Packet(payload=b"hello")

    with pytest.raises(RuntimeError):
        adapter.send_packet(packet)


# verifies that oversized packets are rejected
def test_fake_spi_adapter_rejects_large_packet():
    adapter = create_adapter()
    packet = Packet(payload=b"x" * 300)

    adapter.connect()

    with pytest.raises(ValueError):
        adapter.send_packet(packet)