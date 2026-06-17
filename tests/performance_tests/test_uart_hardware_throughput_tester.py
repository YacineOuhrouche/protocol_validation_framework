# tests uart throughput measurement

from adapters.fake_uart_adapter import FakeUartAdapter
from configs.config_loader import load_uart_config
from performance.uart_hardware_throughput_tester import (
    UartHardwareThroughputTester,
)


# verifies throughput measurement returns a value
def test_uart_throughput_measurement():
    adapter = FakeUartAdapter(
        load_uart_config(),
    )

    adapter.connect()

    tester = UartHardwareThroughputTester(
        adapter,
    )

    throughput = tester.measure_tx_throughput(
        packet_size=32,
        packet_count=100,
    )

    assert throughput > 0