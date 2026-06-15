# tests packet drop behavior

import pytest

from fault_injection.packet_dropper import PacketDropper
from packet_validation.packet import Packet


# verifies that invalid drop rates are rejected
def test_packet_dropper_rejects_invalid_drop_rate():
    with pytest.raises(ValueError):
        PacketDropper(drop_rate=1.5)


# verifies that packet is always dropped with drop rate one
def test_packet_dropper_can_always_drop_packet():
    dropper = PacketDropper(drop_rate=1.0)
    packet = Packet(payload=b"data")

    result = dropper.maybe_drop_packet(packet)

    assert result is None


# verifies that packet is never dropped with drop rate zero
def test_packet_dropper_can_keep_packet():
    dropper = PacketDropper(drop_rate=0.0)
    packet = Packet(payload=b"data")

    result = dropper.maybe_drop_packet(packet)

    assert result == packet