# tests can configuration loading

from configs.config_loader import load_can_config


# verifies that the can config can be loaded
def test_load_can_config():
    config = load_can_config()

    assert config["bitrate"] == 500000
    assert config["max_data_length"] == 8
    assert config["max_packet_size"] == 8
    assert config["standard_id_max"] == 2047
    assert config["expected_ids"] == [256, 512]