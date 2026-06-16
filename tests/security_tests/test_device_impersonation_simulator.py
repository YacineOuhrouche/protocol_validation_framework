# tests device impersonation simulation behavior

import pytest

from security.device_impersonation_simulator import DeviceImpersonationSimulator


# verifies that a fake device can be registered
def test_device_impersonation_registers_fake_device():
    simulator = DeviceImpersonationSimulator()

    simulator.register_fake_device(
        device_id=1,
        device_name="fake_sensor",
    )

    assert simulator.is_impersonating(1) is True


# verifies that a spoofed packet can be created
def test_device_impersonation_creates_spoofed_packet():
    simulator = DeviceImpersonationSimulator()

    simulator.register_fake_device(
        device_id=1,
        device_name="fake_sensor",
    )

    packet = simulator.create_spoofed_packet(
        device_id=1,
        payload=b"fake data",
        sequence_id=10,
    )

    assert packet.payload == b"fake data"
    assert packet.sequence_id == 10


# verifies that unregistered devices cannot create spoofed packets
def test_device_impersonation_rejects_unregistered_device():
    simulator = DeviceImpersonationSimulator()

    with pytest.raises(ValueError):
        simulator.create_spoofed_packet(
            device_id=99,
            payload=b"fake data",
        )


# verifies that fake devices can be removed
def test_device_impersonation_removes_fake_device():
    simulator = DeviceImpersonationSimulator()

    simulator.register_fake_device(
        device_id=1,
        device_name="fake_sensor",
    )

    simulator.remove_fake_device(1)

    assert simulator.is_impersonating(1) is False