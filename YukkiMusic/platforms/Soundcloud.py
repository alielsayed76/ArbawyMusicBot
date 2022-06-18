

import re
from os import path

from yt_dlp import YoutubeDL

from YukkiMusic.utils.formatters import seconds_to_min


class SoundAPI:
    def __init__(self):
        self.opts = {
            "outtmpl": "downloads/%(id)s.%(ext)s",
            "format": "best",
            "retries": 3,
            "nooverwrites": False,
            "continuedl": True,
        }

    async def valid(self, link: str):
        if "soundcloud" in link:
            return True
        else:
            return False

    async def download(self, url):
        d = YoutubeDL(self.opts)
        try:
            info = d.extract_info(url)
        except:
            return False
        xyz = path.join("downloads", f"{info['id']}.{info['ext']}")
        duration_min = seconds_to_min(info["duration"])
        track_details = {
            "الاسم": info["title"],
            "المدة بالثواني": info["duration"],
            "المدة بالدقايق": duration_min,
            "الرافع": info["uploader"],
            "الملف": xyz,
        }
        return track_details, xyz
