# tests packet trace analysis behavior

from diagnostics.packet_trace_analyzer import PacketTraceAnalyzer
from packet_validation.packet import Packet


# verifies that packets can be counted
def test_trace_analyzer_counts_packets():
    analyzer = PacketTraceAnalyzer()

    packets = [
        Packet(payload=b"a"),
        Packet(payload=b"b"),
    ]

    assert analyzer.count_packets(packets) == 2


# verifies that missing sequence ids are detected
def test_trace_analyzer_detects_missing_sequences():
    analyzer = PacketTraceAnalyzer()

    packets = [
        Packet(payload=b"a", sequence_id=0),
        Packet(payload=b"c", sequence_id=2),
    ]

    assert analyzer.detect_missing_sequences(packets) == [1]


# verifies that ordered packets are not marked out of order
def test_trace_analyzer_detects_ordered_packets():
    analyzer = PacketTraceAnalyzer()

    packets = [
        Packet(payload=b"a", sequence_id=0),
        Packet(payload=b"b", sequence_id=1),
    ]

    assert analyzer.detect_out_of_order_packets(packets) is False


# verifies that out of order packets are detected
def test_trace_analyzer_detects_out_of_order_packets():
    analyzer = PacketTraceAnalyzer()

    packets = [
        Packet(payload=b"b", sequence_id=1),
        Packet(payload=b"a", sequence_id=0),
    ]

    assert analyzer.detect_out_of_order_packets(packets) is True


# verifies that trace duration is calculated
def test_trace_analyzer_calculates_trace_duration():
    analyzer = PacketTraceAnalyzer()

    packets = [
        Packet(payload=b"a", timestamp_ms=100),
        Packet(payload=b"b", timestamp_ms=140),
    ]

    assert analyzer.calculate_trace_duration_ms(packets) == 40