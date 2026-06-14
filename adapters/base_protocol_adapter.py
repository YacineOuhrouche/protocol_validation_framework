# defines the shared adapter interface for fake and real protocol adapters

from abc import ABC, abstractmethod
from typing import Optional

from packet_validation.packet import Packet


class BaseProtocolAdapter(ABC):

    # opens the protocol connection
    @abstractmethod
    def connect(self) -> None:
        pass

    # closes the protocol connection
    @abstractmethod
    def disconnect(self) -> None:
        pass

    # sends one packet through the adapter
    @abstractmethod
    def send_packet(self, packet: Packet) -> None:
        pass

    # receives one packet from the adapter
    @abstractmethod
    def receive_packet(self) -> Optional[Packet]:
        pass

    # returns whether the adapter is currently connected
    @abstractmethod
    def is_connected(self) -> bool:
        pass