# captures uart packets from a real or fake uart adapter

from replay_testing.packet_recorder import PacketRecorder


class UartHardwareCapture:

    # creates the uart hardware capture helper
    def __init__(self, adapter):
        self.adapter = adapter
        self.recorder = PacketRecorder()

    # captures packets from the uart adapter
    def capture_packets(
        self,
        packet_count: int,
        output_path: str,
    ) -> str:
        if not self.adapter.is_connected():
            self.adapter.connect()

        for _ in range(packet_count):
            packet = self.adapter.receive_packet()

            if packet is not None:
                self.recorder.record_packet(packet)

        return self.recorder.save_capture(output_path)