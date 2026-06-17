# runs uart throughput measurement on real hardware

from adapters.real_uart_adapter import RealUartAdapter
from configs.config_loader import load_uart_config
from performance.uart_hardware_throughput_tester import (
    UartHardwareThroughputTester,
)


# runs throughput measurement
def main() -> None:
    adapter = RealUartAdapter(
        load_uart_config(),
    )

    try:
        adapter.connect()

        tester = UartHardwareThroughputTester(
            adapter,
        )

        throughput = tester.measure_tx_throughput_kbps(
            packet_size=64,
            packet_count=1000,
        )

        print(
            f"uart throughput: {throughput:.2f} KB/s"
        )

    except Exception as error:
        print(
            f"hardware test skipped: {error}"
        )

    finally:
        adapter.disconnect()


if __name__ == "__main__":
    main()