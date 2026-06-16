# Testing Guide

## Running Tests

Run all tests:

```bash
pytest
```

Run one test file:

```bash
pytest tests/uart_tests/test_uart_validator.py
```

## Test Categories

### Protocol Tests

* UART
* SPI
* I²C
* CAN

### Packet Validation Tests

* CRC validation
* Checksum validation
* Sequence validation

### Fault Injection Tests

* Packet corruption
* Packet loss
* Packet delay
* Bus faults

### Security Tests

* Replay attacks
* Packet mutation
* Device impersonation
* Malformed frames

### Performance Tests

* Throughput
* Latency
* Bus utilization

## Adding Tests

1. Create a test file.
2. Add validation scenarios.
3. Execute pytest.
4. Verify test coverage.

## Regression Testing

Run regression validation before merging changes.

```bash
python -m automation.regression_runner
```
