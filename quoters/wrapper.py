import zlib
import json
from base64 import b64encode, b64decode
import os


class Wrapper:
    loaded_file = {}

    def __init__(self, path):
        self.path = path

    def open_file(self):
        abs_path = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(abs_path, "data", self.path), "r") as fp:
            self.loaded_file = json.loads(fp.read())

    def decode_file(self):
        self.decoded_data = json.loads(zlib.decompress(
            b64decode(self.loaded_file['compressed_data'])))

    def find_quote(self, index):
        self.open_file()
        self.decode_file()
        return self.decoded_data.get(index, None)
