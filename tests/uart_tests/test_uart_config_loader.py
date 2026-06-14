# tests uart configuration loading

from configs.config_loader import load_uart_config


# verifies that the uart config can be loaded
def test_load_uart_config():
    config = load_uart_config()

    assert config["baud_rate"] == 115200
    assert config["data_bits"] == 8
    assert config["stop_bits"] == 1
    assert config["parity"] == "none"
    assert config["timeout_ms"] == 100