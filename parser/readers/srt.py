import re
from parser.times import Times
from parser.constants import TIMESTAMP
from parser.readers.base import BaseReader

OVERRIDE_SEQUENCE = re.compile(r"{[^}]*}")
BYTE_ORDER_MARK = u"\ufeff"

class SRTReader(BaseReader):

    @staticmethod
    def parse(lines):
        timestamps = [] # (start, end)
        following_lines = [] # contains lists of lines following each timestamp

        for line in lines:
            stamps = TIMESTAMP.findall(line)
            if len(stamps) == 2: # timestamp line
                start, end = map(Times.from_timestamp, stamps)
                timestamps.append((start, end))
                following_lines.append([])
            else:
                if timestamps:
                    following_lines[-1].append(line)

        following_lines = [SRTReader.prepare_text(lines) for lines in following_lines]
        for timestamp, lines in zip(timestamps[0:5], following_lines[0:5]):
            print(timestamp, lines)
            pass
        return timestamps, following_lines