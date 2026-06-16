# Examples

## UART Validation

```python
from configs.config_loader import load_uart_config
from packet_validation.packet import Packet
from validators.uart_validator import UartValidator

config = load_uart_config()
validator = UartValidator(config)

packet = Packet(
    payload=bytes([170, 1, 2, 3, 85]),
)

result = validator.validate_packet(packet)

print(result)
```

---

## SPI Validation

```python
from configs.config_loader import load_spi_config
from packet_validation.packet import Packet
from validators.spi_validator import SpiValidator

config = load_spi_config()
validator = SpiValidator(config)

packet = Packet(payload=b"spi data")

result = validator.validate_packet(packet)

print(result)
```

---

## I²C Validation

```python
from configs.config_loader import load_i2c_config
from packet_validation.packet import Packet
from validators.i2c_validator import I2cValidator

config = load_i2c_config()
validator = I2cValidator(config)

packet = Packet(payload=b"i2c data")

result = validator.validate_packet(packet)

print(result)
```

---

## CAN Validation

```python
from configs.config_loader import load_can_config
from packet_validation.packet import Packet
from validators.can_validator import CanValidator

config = load_can_config()
validator = CanValidator(config)

packet = Packet(payload=b"12345678")

result = validator.validate_packet(packet)

print(result)
```

---

## Packet Recording

```python
from packet_validation.packet import Packet
from replay_testing.packet_recorder import PacketRecorder

recorder = PacketRecorder()

recorder.record_packet(
    Packet(
        payload=b"hello",
        sequence_id=0,
        timestamp_ms=100,
    )
)

recorder.save_capture(
    "captures/uart_capture.json",
)
```

---

## Packet Replay

```python
from replay_testing.packet_replayer import PacketReplayer
from adapters.fake_uart_adapter import FakeUartAdapter
from configs.config_loader import load_uart_config

adapter = FakeUartAdapter(
    load_uart_config(),
)

adapter.connect()

replayer = PacketReplayer()

packets = replayer.load_capture(
    "captures/uart_capture.json",
)

replayer.replay_packets(
    adapter,
    packets,
)
```

---

## Fault Injection

```python
from fault_injection.packet_corruptor import PacketCorruptor
from packet_validation.packet import Packet

corruptor = PacketCorruptor()

packet = Packet(payload=b"hello")

corrupted_packet = (
    corruptor.corrupt_random_byte(packet)
)
```

---

## Generate Validation Report

```python
from automation.report_generator import (
    create_report,
    save_report,
)

report = create_report(
    protocol="uart",
    total_tests=10,
    passed_tests=10,
    failed_tests=0,
)

save_report(
    report,
    "reports/uart_validation_report.json",
)
```

---

## Run Validation Pipeline

```bash
python -m automation.validation_pipeline
```

---

## Run Regression Testing

```bash
python -m automation.regression_runner
```

---

## Run Full Test Suite

```bash
pytest
```
