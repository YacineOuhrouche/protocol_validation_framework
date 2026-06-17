# tests uart hardware capture behavior

from adapters.fake_uart_adapter import FakeUartAdapter
from configs.config_loader import load_uart_config
from packet_validation.packet import Packet
from replay_testing.uart_hardware_capture import UartHardwareCapture


# verifies that uart packets can be captured
def test_uart_hardware_capture_records_packets(tmp_path):
    adapter = FakeUartAdapter(load_uart_config())
    adapter.connect()

    adapter.inject_received_packet(
        Packet(payload=b"hello", sequence_id=0)
    )

    capture = UartHardwareCapture(adapter)

    output_path = tmp_path / "uart_capture.json"

    result = capture.capture_packets(
        packet_count=1,
        output_path=str(output_path),
    )

    assert result == str(output_path)
    assert output_path.exists()