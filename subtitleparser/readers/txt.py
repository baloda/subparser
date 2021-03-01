
import re
from subtitleparser.times import Times
from subtitleparser.constants import TXT_TIMESTAMP
from subtitleparser.constants import TIMESTAMP_WITH_FRAME
from subtitleparser.readers.base import BaseReader

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