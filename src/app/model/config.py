from dataclasses import dataclass


@dataclass
class MythmeConfig:
    api_base: str


@dataclass
class MythfrontendConfig:
    socket_host: str
    socket_port: int
    test_mode: bool = False


@dataclass
class LircConfig:
    socket_path: str
    debounce_interval: float


@dataclass
class SchedulerConfig:
    hour: int  # 0-23, hour of day to trigger activation


@dataclass
class AppConfig:
    mythme: MythmeConfig
    mythfrontend: MythfrontendConfig
    lirc: LircConfig
    scheduler: SchedulerConfig


@dataclass
class MythtvConfig:
    storage_groups: dict[str, str]
