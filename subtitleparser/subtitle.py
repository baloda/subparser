import codecs
from chardet import detect
from subtitleparser.constants import Extensions
from subtitleparser.readers.srt import SRTReader
from subtitleparser.readers.txt import TXTReader


class SubtitleFile:

    def __init__(self, path, encoding='utf-8', language_code=None):
        self.path = path
        self.language_code = None
        self.ext = Extensions.get(path)
        self.encoding = encoding
        self.size = None
        self.contents = None
        self.style = None
        self.data = None


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
        self.data = SRTReader.parse(self.contents)
        # self.data = TXTReader.parse(self.contents)
        return self.data

    def print(self):
        print("Path: %s" % (self.path))
        print("Encoding: %s" % (self.encoding))
        print("DATA:- ")
        for ins in self.data:
            print(ins.start, ins.end, ins.text)