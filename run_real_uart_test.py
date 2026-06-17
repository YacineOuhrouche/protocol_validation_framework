# runs a basic real uart hardware validation test

from adapters.real_uart_adapter import RealUartAdapter
from configs.config_loader import load_uart_config
from packet_validation.packet import Packet


# runs a uart loopback test
def main() -> None:
    config = load_uart_config()
    adapter = RealUartAdapter(config)

    print("available ports:")
    print(adapter.list_available_ports())

    packet = Packet(
        payload=bytes([170, 1, 2, 3, 85]),
        sequence_id=0,
    )

    try:
        adapter.connect()
        adapter.send_packet(packet)

        received_packet = adapter.receive_packet()

        if received_packet is None:
            print("no packet received")
            return

        print(f"received: {received_packet.to_hex()}")

    except RuntimeError as error:
        print(f"hardware test skipped: {error}")

    finally:
        adapter.disconnect()


if __name__ == "__main__":
    main()