import os
from .compressed import gzipped, bzipped

extension_map = {
    '.bz2': bzipped.opener,
    '.gz': gzipped.opener
}


class Reader:
    def __init__(self, filename):
        self.filename = filename
        extension = os.path.splitext(filename)[1]  # grab the tail to figure out the file extension
        opener = extension_map.get(extension, open)  # opener will be the appr file type opener; default to stndrd open
        self.f = opener(filename, 'rt')

    def close(self):
        self.f.close()

    def read(self):
        return self.f.read()
