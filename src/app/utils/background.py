import threading
import time
from datetime import datetime, timedelta
from typing import Callable
from app.utils.config import config


def _seconds_until_next(hour: int) -> float:
    """Calculate seconds until the next occurrence of the given hour today or tomorrow."""
    now = datetime.now()
    target = now.replace(hour=hour, minute=0, second=0, microsecond=0)
    if target <= now:
        target += timedelta(days=1)
    return (target - now).total_seconds()


def start_scheduler(callback: Callable[[], None]) -> threading.Thread:
    """Start a background daemon thread that calls callback every day at the scheduled hour.

    :param callback: Function to call at the scheduled time each day
    :type callback: Callable[[], None]
    :return: The background thread running the scheduler
    :rtype: threading.Thread
    """

    def run() -> None:
        while True:
            delay = _seconds_until_next(config.schedule.hour)
            time.sleep(delay)
            try:
                callback()
            except Exception as e:
                print(f"Scheduled callback failed: {e}")

    thread = threading.Thread(target=run, daemon=True, name="daily-scheduler")
    thread.start()
    return thread
