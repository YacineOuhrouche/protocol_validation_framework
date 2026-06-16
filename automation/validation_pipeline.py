# runs protocol validation checks for all supported protocols

from configs.config_loader import (
    load_can_config,
    load_i2c_config,
    load_spi_config,
    load_uart_config,
)
from packet_validation.packet import Packet
from validators.can_validator import CanValidator
from validators.i2c_validator import I2cValidator
from validators.spi_validator import SpiValidator
from validators.uart_validator import UartValidator


# runs uart validation pipeline
def run_uart_pipeline() -> dict:
    validator = UartValidator(load_uart_config())

    valid_packet = Packet(payload=bytes([170, 1, 2, 3, 85]))
    invalid_packet = Packet(payload=bytes([0, 1, 2, 3, 0]))

    return {
        "protocol": "uart",
        "valid_packet_passed": validator.validate_packet(valid_packet),
        "invalid_packet_rejected": not validator.validate_packet(invalid_packet),
    }


# runs spi validation pipeline
def run_spi_pipeline() -> dict:
    validator = SpiValidator(load_spi_config())

    valid_packet = Packet(payload=b"spi data")
    invalid_packet = Packet(payload=b"")

    return {
        "protocol": "spi",
        "valid_packet_passed": validator.validate_packet(valid_packet),
        "invalid_packet_rejected": not validator.validate_packet(invalid_packet),
        "mode_valid": validator.validate_mode(),
        "clock_valid": validator.validate_clock_speed(),
    }


# runs i2c validation pipeline
def run_i2c_pipeline() -> dict:
    validator = I2cValidator(load_i2c_config())

    valid_packet = Packet(payload=b"i2c data")
    invalid_packet = Packet(payload=b"")

    return {
        "protocol": "i2c",
        "valid_packet_passed": validator.validate_packet(valid_packet),
        "invalid_packet_rejected": not validator.validate_packet(invalid_packet),
        "expected_device_valid": validator.validate_expected_device(80),
        "bus_speed_valid": validator.validate_bus_speed(),
    }


# runs can validation pipeline
def run_can_pipeline() -> dict:
    validator = CanValidator(load_can_config())

    valid_packet = Packet(payload=b"12345678")
    invalid_packet = Packet(payload=b"123456789")

    return {
        "protocol": "can",
        "valid_packet_passed": validator.validate_packet(valid_packet),
        "invalid_packet_rejected": not validator.validate_packet(invalid_packet),
        "expected_id_valid": validator.validate_expected_id(256),
        "bitrate_valid": validator.validate_bitrate(),
    }


# checks whether one protocol pipeline passed
def pipeline_passed(results: dict) -> bool:
    return all(
        value is True
        for key, value in results.items()
        if key != "protocol"
    )


# runs all protocol validation pipelines
def run_all_pipelines() -> dict:
    pipelines = [
        run_uart_pipeline(),
        run_spi_pipeline(),
        run_i2c_pipeline(),
        run_can_pipeline(),
    ]

    return {
        "pipelines": pipelines,
        "status": "PASS" if all(pipeline_passed(item) for item in pipelines) else "FAIL",
    }


# starts validation pipeline from command line
def main() -> None:
    results = run_all_pipelines()

    print(results)


if __name__ == "__main__":
    main()