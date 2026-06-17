## Hardware Validation Reports

UART hardware validation reports are generated as JSON files.

Example output:

```text
reports/uart_hardware_validation_report.json
```

The report includes:

* Loopback status
* Packets captured
* Throughput measurements
* Validation status

## Running UART Hardware Report Generation

After running hardware validation, reports can be generated using:

```bash
python -m automation.uart_hardware_report
```

Generated reports are stored in:

```text
reports/
```

## Current Version 2 Scope

Version 2 focuses on introducing real hardware support while preserving compatibility with the Version 1 framework.

### Included

* Real UART adapter
* UART loopback validation
* UART throughput testing
* UART packet capture
* UART hardware validation reports
* Real CAN adapter skeleton

### Not Included Yet

* Real SPI adapter
* Real I²C adapter
* SPI hardware timing validation
* I²C hardware bus recovery validation

These capabilities may be added in future versions.

## Recommended Hardware

### UART

* USB-to-UART adapter
* STM32 development board
* ESP32 development board
* Raspberry Pi Pico

### CAN

* CANable
* USB-CAN adapter
* CAN development boards

## Future Hardware Support

Planned additions include:

* Real CAN validation
* SocketCAN integration
* Logic analyzer workflows
* Oscilloscope workflows
* Hardware capture analysis
* Automated hardware regression testing

## Notes

The framework is designed so that validators, diagnostics, reporting, and automation components work with both simulated adapters and real hardware adapters.

This allows Version 1 and Version 2 validation workflows to share the same architecture while gradually introducing hardware support.
