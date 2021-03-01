import os
import re
from enum import Enum
from collections import namedtuple


TXT_TIMESTAMP = "(^[\d,\s]*)"
TIMESTAMP = re.compile(r"(\d{1,2}):(\d{2}):(\d{2})[.,](\d{2,3})")
TIMESTAMP_WITH_FRAME = re.compile(r"(\d{1,2})\s+(\d{2})\s+(\d{2})\s+(\d{2,3})")


class Extensions(Enum):
    TXT = ".txt"
    SRT = ".srt"
    WEBVTT = ".webvtt"
    TTML = ".ttml"
    ITT = ".itt"

    @classmethod
    def get(cls, path):
        _, ext = os.path.splitext(path)
        return ext