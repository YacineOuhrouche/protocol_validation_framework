# tests protocol validation pipeline behavior

from automation.validation_pipeline import run_uart_pipeline


# verifies that uart validation pipeline passes
def test_run_uart_pipeline():
    results = run_uart_pipeline()

    assert results["protocol"] == "uart"
    assert results["status"] == "PASS"