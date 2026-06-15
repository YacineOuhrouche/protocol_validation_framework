# replays packet captures for all supported protocols

from replay_testing.protocol_capture_runner import replay_protocol_capture


# replays captures for uart spi i2c and can
def main():
    protocols = ["uart", "spi", "i2c", "can"]

    for protocol in protocols:
        replayed_count = replay_protocol_capture(protocol)
        print(f"{protocol} packets replayed: {replayed_count}")


if __name__ == "__main__":
    main()