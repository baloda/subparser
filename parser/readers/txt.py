
import re
from parser.times import Times
from parser.constants import TXT_TIMESTAMP
from parser.constants import TIMESTAMP_WITH_FRAME
from parser.readers.base import BaseReader

class TXTReader(BaseReader):

    @staticmethod
    def parse(lines):

        timestamps = [] # (start, end)
        following_lines = [] # contains lists of lines following each timestamp

        for line in lines:
            stamps = TIMESTAMP_WITH_FRAME.findall(line)
            if len(stamps) == 2: # timestamp line
                start, end = map(Times.from_frame_timestamp, stamps)
                timestamps.append((start, end))
                following_lines.append([re.sub(TXT_TIMESTAMP, "", line)])

        contents = [
            TXTReader(timestamp[0], timestamp[1], lines)
            for timestamp, lines in zip(timestamps, following_lines)
        ]
        return contents