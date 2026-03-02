from dataclasses import dataclass


@dataclass
class MythmeConfig:
    api_base: str


@dataclass
class AppConfig:
    mythme: MythmeConfig


@dataclass
class MythtvConfig:
    storage_groups: dict[str, str]
