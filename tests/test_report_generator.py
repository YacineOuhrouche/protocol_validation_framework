# tests protocol validation report generation

import json

from automation.report_generator import (
    create_report,
    save_report,
)


# verifies that a report dictionary is created correctly
def test_create_report():
    report = create_report(
        protocol="uart",
        total_tests=10,
        passed_tests=10,
        failed_tests=0,
        packets_tested=100,
    )

    assert report["protocol"] == "uart"
    assert report["total_tests"] == 10
    assert report["status"] == "PASS"


# verifies that reports can be saved to disk
def test_save_report(tmp_path):
    report = create_report(
        protocol="uart",
        total_tests=10,
        passed_tests=10,
        failed_tests=0,
    )

    report_path = tmp_path / "report.json"

    save_report(
        report,
        str(report_path),
    )

    assert report_path.exists()


# verifies that saved report content is valid
def test_saved_report_content(tmp_path):
    report = create_report(
        protocol="uart",
        total_tests=10,
        passed_tests=9,
        failed_tests=1,
    )

    report_path = tmp_path / "report.json"

    save_report(
        report,
        str(report_path),
    )

    with report_path.open("r", encoding="utf-8") as file:
        loaded_report = json.load(file)

    assert loaded_report["protocol"] == "uart"
    assert loaded_report["failed_tests"] == 1
    assert loaded_report["status"] == "FAIL"