import codecs
from chardet import detect
from parser.constants import Extensions
from parser.readers.srt import SRTReader
from parser.readers.txt import TXTReader


class SubtitleFile:

    def __init__(self, path, encoding='utf-8', language_code=None):
        self.path = path
        self.language_code = None
        self.ext = Extensions.get(path)
        self.encoding = encoding
        self.size = None
        self.contents = None
        self.style = None


    def detect_encoding(self):
        with open(file=self.path, mode='rb') as f:
            info = detect(f.read())
        self.encoding = info and info['encoding'] or self.encoding
        return self


    def read(self):
        with open(file=self.path, encoding=self.encoding, mode="r") as f:
            self.contents = f.readlines()
        return self

    def parse(self):
        # d = SRTReader.parse(self.contents)
        d = TXTReader.parse(self.contents)
        return d