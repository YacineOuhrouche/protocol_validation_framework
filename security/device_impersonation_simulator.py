# simulates device impersonation for protocol security testing

from packet_validation.packet import Packet


class DeviceImpersonationSimulator:

    # creates the device impersonation simulator
    def __init__(self):
        self.impersonated_devices = {}

    # registers a fake device identity
    def register_fake_device(self, device_id: int, device_name: str) -> None:
        self.impersonated_devices[device_id] = device_name

    # checks whether a device identity is being impersonated
    def is_impersonating(self, device_id: int) -> bool:
        return device_id in self.impersonated_devices

    # creates a spoofed packet from a fake device
    def create_spoofed_packet(
        self,
        device_id: int,
        payload: bytes,
        sequence_id: int = 0,
    ) -> Packet:
        if not self.is_impersonating(device_id):
            raise ValueError("device id is not registered for impersonation")

        return Packet(
            payload=payload,
            sequence_id=sequence_id,
        )

    # removes a fake device identity
    def remove_fake_device(self, device_id: int) -> None:
        if device_id in self.impersonated_devices:
            del self.impersonated_devices[device_id]