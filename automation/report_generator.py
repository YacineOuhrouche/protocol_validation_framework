# generate protocol validation reports
# summarize protocol test results into json format

import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict


# create validation report dictionary
def create_report(
    protocol: str,
    total_tests: int,
    passed_tests: int,
    failed_tests: int,
    packets_tested: int = 0,
    faults_injected: int = 0,
    security_tests: int = 0,
    throughput_bps: float = 0,
    average_latency_ms: float = 0,
) -> Dict[str, Any]:
    return {
        "timestamp": datetime.now().isoformat(),
        "protocol": protocol,
        "total_tests": total_tests,
        "passed_tests": passed_tests,
        "failed_tests": failed_tests,
        "packets_tested": packets_tested,
        "faults_injected": faults_injected,
        "security_tests": security_tests,
        "throughput_bps": throughput_bps,
        "average_latency_ms": average_latency_ms,
        "status": "PASS" if failed_tests == 0 else "FAIL",
    }


# save validation report to json file
def save_report(report: Dict[str, Any], output_path: str) -> str:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as file:
        json.dump(report, file, indent=4)

    return str(path)


# generate default uart validation report
def generate_default_report() -> str:
    report = create_report(
        protocol="uart",
        total_tests=0,
        passed_tests=0,
        failed_tests=0,
        packets_tested=0,
        faults_injected=0,
        security_tests=0,
    )

    return save_report(report, "reports/uart_validation_report.json")


# start report generator from command line
def main() -> None:
    output_path = generate_default_report()
    print(f"report generated: {output_path}")


if __name__ == "__main__":
    main()