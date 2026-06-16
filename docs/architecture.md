# Architecture

The framework is organized into modular components.

## Adapters

Provide protocol-specific communication interfaces.

```text
adapters/
```

Examples:

* FakeUartAdapter
* FakeSpiAdapter
* FakeI2cAdapter
* FakeCanAdapter

## Validators

Validate protocol behavior and packet correctness.

```text
validators/
packet_validation/
```

Examples:

* UART validation
* CRC validation
* Checksum validation
* Sequence validation

## Fault Injection

Simulate communication failures.

```text
fault_injection/
```

Examples:

* Packet corruption
* Packet loss
* Packet delay
* Bus faults

## Security

Simulate protocol attacks.

```text
security/
```

Examples:

* Replay attacks
* Device impersonation
* Malformed frames

## Performance

Measure communication performance.

```text
performance/
```

Examples:

* Throughput
* Latency
* Bus utilization

## Automation

Execute validation workflows and generate reports.

```text
automation/
```
