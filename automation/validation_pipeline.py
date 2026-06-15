# runs protocol validation checks and summarizes pipeline results

from configs.config_loader import load_uart_config
from packet_validation.packet import Packet
from validators.uart_validator import UartValidator


# creates a valid uart test packet
def create_valid_uart_packet() -> Packet:
    return Packet(
        payload=bytes([170, 1, 2, 3, 85]),
        sequence_id=0,
    )


# creates an invalid uart test packet
def create_invalid_uart_packet() -> Packet:
    return Packet(
        payload=bytes([0, 1, 2, 3, 0]),
        sequence_id=1,
    )


# runs uart validation pipeline
def run_uart_pipeline() -> dict:
    config = load_uart_config()
    validator = UartValidator(config)

    valid_packet = create_valid_uart_packet()
    invalid_packet = create_invalid_uart_packet()

    valid_result = validator.validate_packet(valid_packet)
    invalid_result = validator.validate_packet(invalid_packet)

    return {
        "protocol": "uart",
        "valid_packet_passed": valid_result,
        "invalid_packet_rejected": not invalid_result,
        "status": "PASS" if valid_result and not invalid_result else "FAIL",
    }


# starts validation pipeline from command line
def main() -> None:
    results = run_uart_pipeline()

    print(results)


if __name__ == "__main__":
    main()