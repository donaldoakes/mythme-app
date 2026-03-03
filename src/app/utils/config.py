import os
import yaml
from functools import cache
from app.model.config import (
    AppConfig,
    LircConfig,
    MythfrontendConfig,
    MythmeConfig,
    ScheduleConfig,
)


@cache
def load_config() -> AppConfig:
    yaml_file = os.getenv("MYTHME_APP_CONFIG", "config/app.yaml")
    print(f"Reading app config from {yaml_file}")
    with open(yaml_file, "r") as yf:
        cfg = yaml.safe_load(yf)
    if "mythme" in cfg:
        mythme = cfg["mythme"]
        mythme_config = MythmeConfig(api_base=mythme["api_base"])
    if "mythfrontend" in cfg:
        mythfrontend = cfg["mythfrontend"]
        mythfrontend_config = MythfrontendConfig(
            socket_host=mythfrontend["socket_host"],
            socket_port=mythfrontend["socket_port"],
        )
        if "test_mode" in mythfrontend:
            mythfrontend_config.test_mode = mythfrontend["test_mode"]
    if "lirc" in cfg:
        lirc = cfg["lirc"]
        lirc_config = LircConfig(
            socket_path=lirc["socket_path"], debounce_interval=lirc["debounce_interval"]
        )
    if "schedule" in cfg:
        schedule = cfg["schedule"]
        if "hour" in schedule:
            schedule_config = ScheduleConfig(hour=schedule["hour"])
    if mythme_config and mythfrontend_config:
        return AppConfig(
            mythme=mythme_config,
            mythfrontend=mythfrontend_config,
            lirc=lirc_config,
            schedule=schedule_config,
        )

    raise ValueError(f"Bad config: {yaml_file}")


config: AppConfig = load_config()
