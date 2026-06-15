# tests the fake i2c adapter behavior

import pytest

from adapters.fake_i2c_adapter import FakeI2cAdapter
from configs.config_loader import load_i2c_config
from packet_validation.packet import Packet


# creates a fake i2c adapter for tests
def create_adapter() -> FakeI2cAdapter:
    config = load_i2c_config()
    return FakeI2cAdapter(config)


# verifies that the fake i2c adapter can connect
def test_fake_i2c_adapter_can_connect():
    adapter = create_adapter()

    adapter.connect()

    assert adapter.is_connected() is True


# verifies that the fake i2c adapter can disconnect
def test_fake_i2c_adapter_can_disconnect():
    adapter = create_adapter()

    adapter.connect()
    adapter.disconnect()

    assert adapter.is_connected() is False


# verifies that a fake i2c device can be registered
def test_fake_i2c_adapter_can_register_device():
    adapter = create_adapter()
    packet = Packet(payload=b"device")

    adapter.register_device(80, packet)

    assert 80 in adapter.devices


# verifies that a fake i2c device can be written and read
def test_fake_i2c_adapter_can_write_and_read_device():
    adapter = create_adapter()
    packet = Packet(payload=b"data")

    adapter.connect()
    adapter.write_to_device(80, packet)

    assert adapter.read_from_device(80) == packet


# verifies that the fake i2c adapter can scan devices
def test_fake_i2c_adapter_can_scan_devices():
    adapter = create_adapter()
    packet = Packet(payload=b"device")

    adapter.connect()
    adapter.register_device(80, packet)

    assert adapter.scan_devices() == [80]


# verifies that invalid i2c addresses are rejected
def test_fake_i2c_adapter_rejects_invalid_address():
    adapter = create_adapter()
    packet = Packet(payload=b"data")

    with pytest.raises(ValueError):
        adapter.register_device(200, packet)


# verifies that oversized packets are rejected
def test_fake_i2c_adapter_rejects_large_packet():
    adapter = create_adapter()
    packet = Packet(payload=b"x" * 300)

    with pytest.raises(ValueError):
        adapter.register_device(80, packet)


# verifies that read fails when the adapter is disconnected
def test_fake_i2c_adapter_rejects_read_when_disconnected():
    adapter = create_adapter()

    with pytest.raises(RuntimeError):
        adapter.read_from_device(80)