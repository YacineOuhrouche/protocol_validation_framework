# analyzes packet traces for ordering loss and timing issues

from packet_validation.packet import Packet


class PacketTraceAnalyzer:

    # counts packets in a trace
    def count_packets(self, packets: list[Packet]) -> int:
        return len(packets)

    # detects missing sequence ids in a packet trace
    def detect_missing_sequences(self, packets: list[Packet]) -> list[int]:
        sequence_ids = [
            packet.sequence_id
            for packet in packets
            if packet.sequence_id is not None
        ]

        if not sequence_ids:
            return []

        missing_sequences = []

        for sequence_id in range(min(sequence_ids), max(sequence_ids) + 1):
            if sequence_id not in sequence_ids:
                missing_sequences.append(sequence_id)

        return missing_sequences

    # detects packets that arrived out of order
    def detect_out_of_order_packets(self, packets: list[Packet]) -> bool:
        sequence_ids = [
            packet.sequence_id
            for packet in packets
            if packet.sequence_id is not None
        ]

        return sequence_ids != sorted(sequence_ids)

    # calculates packet trace duration
    def calculate_trace_duration_ms(self, packets: list[Packet]) -> int:
        timestamps = [
            packet.timestamp_ms
            for packet in packets
            if packet.timestamp_ms is not None
        ]

        if not timestamps:
            return 0

        return max(timestamps) - min(timestamps)