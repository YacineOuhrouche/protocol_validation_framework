# generates uart hardware validation reports

from automation.report_generator import create_report, save_report


# creates a uart hardware report
def create_uart_hardware_report(
    loopback_passed: bool,
    throughput_kbps: float,
    packets_captured: int,
) -> dict:
    failed_tests = 0 if loopback_passed else 1

    return create_report(
        protocol="uart_hardware",
        total_tests=3,
        passed_tests=3 - failed_tests,
        failed_tests=failed_tests,
        packets_tested=packets_captured,
        faults_injected=0,
        security_tests=0,
        throughput_bps=throughput_kbps * 1024 * 8,
        average_latency_ms=0,
    )


# saves a uart hardware report
def save_uart_hardware_report(
    report: dict,
    output_path: str = "reports/uart_hardware_validation_report.json",
) -> str:
    return save_report(
        report,
        output_path,
    )