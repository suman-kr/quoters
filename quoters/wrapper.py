import zlib
import json
from base64 import b64encode, b64decode

class Wrapper:
    loaded_file = {}

    def __init__(self, path):
        self.path = path

    def open_file(self):
        with open(self.path) as fp:
            self.loaded_file = json.loads(fp.read())

    def decode_file(self):
        self.decoded_data = json.loads(zlib.decompress(
            b64decode(self.loaded_file['compressed_data'])))

    def find_quote(self, index):
        self.open_file()
        self.decode_file()
        return self.decoded_data.get(index, None)
