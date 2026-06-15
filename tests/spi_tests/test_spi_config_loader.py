# tests spi configuration loading

from configs.config_loader import load_spi_config


# verifies that the spi config can be loaded
def test_load_spi_config():
    config = load_spi_config()

    assert config["mode"] == 0
    assert config["clock_hz"] == 1000000
    assert config["max_packet_size"] == 256
    assert config["chip_select_count"] == 2
    assert config["default_chip_select"] == 0