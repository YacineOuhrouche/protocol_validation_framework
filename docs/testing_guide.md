# Testing Guide

## Test Structure

```text
tests/

├── uart_tests/
├── spi_tests/
├── i2c_tests/
├── can_tests/
├── packet_validation_tests/
├── performance_tests/
├── security_tests/
├── diagnostics_tests/
└── automation_tests/
```

## Run All Tests

```bash
pytest
```

## Run One Test File

```bash
pytest tests/uart_tests/test_uart_validator.py
```

## Adding Tests

1. Create a new test file.
2. Add validation scenarios.
3. Execute pytest.
4. Verify results.

## Regression Testing

```bash
python -m automation.regression_runner
```
