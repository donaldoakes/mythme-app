from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class Video:
    title: str
    file: str
    watched: Optional[datetime] = None


@dataclass
class DailyVid:
    video: Video
    watched: int
    total: int
    earliest: datetime
    latest: datetime
