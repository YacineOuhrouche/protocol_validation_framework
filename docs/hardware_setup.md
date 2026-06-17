# Hardware Setup

This document explains how to run real hardware validation for the Protocol Validation Framework.

## Current Hardware Support

The first real hardware target is UART using PySerial.

## Requirements

* USB-to-UART adapter, microcontroller board, or development board
* UART TX/RX access
* Common ground connection
* Python environment with PySerial installed

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Find Serial Ports

### macOS

```bash
ls /dev/tty.*
```

Example:

```text
/dev/tty.usbserial-0001
/dev/tty.usbmodem1101
/dev/tty.SLAB_USBtoUART
/dev/tty.wchusbserial
```

### Linux

```bash
ls /dev/ttyUSB*
ls /dev/ttyACM*
```

### Windows

Open Device Manager and check:

```text
Ports (COM & LPT)
```

Example:

```text
COM3
COM5
COM7
```

## Configure UART Port

Update:

```text
configs/uart_config.yaml
```

Example:

```yaml
uart:
  port: /dev/tty.usbserial-0001
  baud_rate: 115200
  data_bits: 8
  stop_bits: 1
  parity: none
  timeout_ms: 100
  max_packet_size: 256
  expected_start_byte: 170
  expected_end_byte: 85
```

## Loopback Wiring

### USB-UART Adapter

Connect:

```text
TX -> RX
GND -> GND
```

This allows transmitted bytes to be received back by the adapter.

### Microcontroller Echo Test

Example:

```text
USB-UART Adapter TX -> MCU RX
USB-UART Adapter RX -> MCU TX
USB-UART Adapter GND -> MCU GND
```

The firmware should echo received bytes back to the sender.

## Run Hardware Test

```bash
python run_real_uart_test.py
```

Expected output:

```text
available ports:
['/dev/tty.usbserial-0001']

received: aa01020355
```

If no hardware is connected:

```text
hardware test skipped: uart port not found
```

## Troubleshooting

### Port Not Found

Check available ports:

```bash
ls /dev/tty.*
```

Verify that the configured port matches the connected device.

### No Data Received

Verify:

* TX/RX wiring
* Ground connection
* Baud rate
* Firmware echo functionality

### Permission Errors

Linux:

```bash
sudo usermod -a -G dialout $USER
```

Log out and back in.

## Version 2 Scope

Planned hardware support:

* Real UART adapter
* UART loopback validation
* UART throughput validation
* Real CAN adapter
* SocketCAN integration
* Logic analyzer workflows
* Oscilloscope workflows
* Hardware validation reporting
