from dataclasses import dataclass
from datetime import datetime


@dataclass
class Video:
    title: str
    file: str


@dataclass
class DailyVid:
    video: Video
    watched: int
    total: int
    earliest: datetime
    latest: datetime
