import requests
from typing import Literal, Optional
from datetime import datetime
from app.model.config import MythtvConfig
from app.model.video import DailyVid, Video
from app.utils.config import config

ApiMethod = Literal["GET", "PATCH"]


def api_call(path: str, method: ApiMethod = "GET") -> Optional[dict]:
    url = f"{config.mythme.api_base}/{path}"
    headers = {"Accept": "application/json"}

    if method == "PATCH":
        response = requests.patch(url, headers=headers)  # nosec B113
    else:
        response = requests.get(url, headers=headers)  # nosec B113

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        print(f"{method} {url} NOT FOUND")
        return None
    else:
        print(f"{method} {url} FAILED: {response.text}")
        raise Exception(f"{method} {url} FAILED: {response.status_code}")


def dailyvid() -> DailyVid:
    resp = api_call(path="dailyvid")
    if resp is None:
        raise ValueError("Daily video not retrieved")
    if "earliest" in resp:
        resp["earliest"] = datetime.strptime(resp["earliest"], "%Y-%m-%dT%H:%M:%S")
    if "latest" in resp:
        resp["latest"] = datetime.strptime(resp["latest"], "%Y-%m-%dT%H:%M:%S")

    dailyvid = DailyVid(**resp)
    del resp["video"]["id"]
    dailyvid.video = Video(**(resp["video"]))
    return dailyvid


def mythtv_config() -> MythtvConfig:
    resp = api_call(path="configs/mythtv")
    if resp is None:
        raise ValueError("MythTV config not found")
    return MythtvConfig(storage_groups=resp["storage_groups"])
