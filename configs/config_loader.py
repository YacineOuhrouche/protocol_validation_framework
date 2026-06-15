# loads yaml configuration files for protocol validation

from pathlib import Path
from typing import Any, Dict

import yaml


# loads a yaml config file
def load_config(config_path: str) -> Dict[str, Any]:
    path = Path(config_path)

    if not path.exists():
        raise FileNotFoundError(f"config file not found: {config_path}")

    with path.open("r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    if config is None:
        return {}

    return config


# loads the uart configuration section
def load_uart_config(config_path: str = "configs/uart_config.yaml") -> Dict[str, Any]:
    config = load_config(config_path)

    if "uart" not in config:
        raise KeyError("missing uart config section")

    return config["uart"]

    # loads the spi configuration section
def load_spi_config(config_path: str = "configs/spi_config.yaml") -> Dict[str, Any]:
    config = load_config(config_path)

    if "spi" not in config:
        raise KeyError("missing spi config section")

    return config["spi"]