# records packet captures for all supported protocols

from replay_testing.protocol_capture_runner import record_protocol_capture


# records captures for uart spi i2c and can
def main():
    protocols = ["uart", "spi", "i2c", "can"]

    for protocol in protocols:
        output_path = record_protocol_capture(protocol)
        print(f"{protocol} capture saved: {output_path}")


if __name__ == "__main__":
    main()