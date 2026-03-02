from dataclasses import dataclass


@dataclass
class MythmeConfig:
    api_base: str


@dataclass
class AppConfig:
    mythme: MythmeConfig
