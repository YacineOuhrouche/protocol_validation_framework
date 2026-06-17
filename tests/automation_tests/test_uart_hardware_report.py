# tests uart hardware report generation

import json

from automation.uart_hardware_report import (
    create_uart_hardware_report,
    save_uart_hardware_report,
)


# verifies that uart hardware report can be created
def test_create_uart_hardware_report():
    report = create_uart_hardware_report(
        loopback_passed=True,
        throughput_kbps=10.5,
        packets_captured=5,
    )

    assert report["protocol"] == "uart_hardware"
    assert report["status"] == "PASS"
    assert report["packets_tested"] == 5


# verifies that uart hardware report can be saved
def test_save_uart_hardware_report(tmp_path):
    report = create_uart_hardware_report(
        loopback_passed=True,
        throughput_kbps=10.5,
        packets_captured=5,
    )

    output_path = tmp_path / "uart_hardware_report.json"

    save_uart_hardware_report(
        report,
        str(output_path),
    )

    assert output_path.exists()

    with output_path.open("r", encoding="utf-8") as file:
        saved_report = json.load(file)

    assert saved_report["protocol"] == "uart_hardware"