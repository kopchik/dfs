#!/usr/bin/env python3
from io import BytesIO
from hashlib import sha256


def noop(*args, **kwargs):
    return True


class File:
    def __init__(self, name, on_update=noop):
        self.name = name
        self._fd = BytesIO()
        self.version = 1
        self.on_update = on_update

    def seek(self, *args, **kwargs):
        self._fd.seek(*args, **kwargs)
        return self

    def read(self):
        data = self._fd.read()
        return data

    def write(self, *args, **kwargs):
        self._fd.write(*args, **kwargs)
        self.version += 1
        self.on_update(self, 'write', args, kwargs)
        return self

    def flush(self):
        raise NotImplementedError

    def close(self):
        raise NotImplementedError

    def sha256(self):
        buf= self._fd.getbuffer()
        hash = sha256(buf)
        hexdigest = hash.hexdigest()
        return hexdigest

    def __repr__(self):
        cls_name = self.__class__.__name__
        return f"{cls_name}(\"{self.name}\")"


class DFS:
    def __init__(self, addr, peers):
        self.files = {}
        self.addr = addr
        self.peers = peers

    def new_file(self, name):
        if name in self.files:
            raise FileExistsError(name)

    def open(self, name):
        if name not in self.files:
            raise FileNotFoundError(name)
        file = self.files[name]
        return file
