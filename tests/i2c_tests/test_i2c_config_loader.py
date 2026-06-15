# tests i2c configuration loading

from configs.config_loader import load_i2c_config


# verifies that the i2c config can be loaded
def test_load_i2c_config():
    config = load_i2c_config()

    assert config["bus_speed_hz"] == 100000
    assert config["max_packet_size"] == 256
    assert config["address_bits"] == 7
    assert config["expected_devices"] == [80, 104]
    assert config["timeout_ms"] == 100