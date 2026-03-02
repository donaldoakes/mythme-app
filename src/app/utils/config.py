import os
import yaml
from functools import cache
from app.model.config import AppConfig, MythmeConfig


@cache
def load_config() -> AppConfig:
    yaml_file = os.getenv("MYTHME_APP_CONFIG", "config/app.yaml")
    print(f"Reading app config from {yaml_file}")
    with open(yaml_file, "r") as yf:
        cfg = yaml.safe_load(yf)
    if "mythme" in cfg:
        mythme = cfg["mythme"]
        if "api_base" in mythme:
            return AppConfig(mythme=MythmeConfig(api_base=mythme["api_base"]))
    raise ValueError(f"Bad config: {yaml_file}")


config: AppConfig = load_config()
