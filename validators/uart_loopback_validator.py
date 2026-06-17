# validates uart loopback behavior on real or fake adapters

from packet_validation.packet import Packet


class UartLoopbackValidator:

    # creates the uart loopback validator
    def __init__(self, adapter):
        self.adapter = adapter

    # validates that transmitted data is received back unchanged
    def validate_loopback(self, packet: Packet) -> bool:
        if not self.adapter.is_connected():
            self.adapter.connect()

        self.adapter.send_packet(packet)

        received_packet = self.adapter.receive_packet()

        if received_packet is None:
            return False

        return received_packet.payload == packet.payload