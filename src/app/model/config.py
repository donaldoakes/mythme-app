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
class AppConfig:
    mythme: MythmeConfig
    mythfrontend: MythfrontendConfig


@dataclass
class MythtvConfig:
    storage_groups: dict[str, str]
