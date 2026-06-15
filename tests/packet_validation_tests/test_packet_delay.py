# tests packet delay behavior

import time

import pytest

from fault_injection.packet_delay import PacketDelay
from packet_validation.packet import Packet


# verifies that negative delays are rejected
def test_packet_delay_rejects_negative_delay():
    with pytest.raises(ValueError):
        PacketDelay(delay_ms=-1)


# verifies that packet delay returns the same packet
def test_packet_delay_returns_packet():
    delay = PacketDelay(delay_ms=1)
    packet = Packet(payload=b"data")

    result = delay.delay_packet(packet)

    assert result == packet


# verifies that packet delay waits before returning
def test_packet_delay_waits():
    delay = PacketDelay(delay_ms=10)
    packet = Packet(payload=b"data")

    start_time = time.time()
    delay.delay_packet(packet)
    elapsed_ms = (time.time() - start_time) * 1000

    assert elapsed_ms >= 10