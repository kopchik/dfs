#!/usr/bin/env python3
from io import BytesIO


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

    def write(self, *args, **kwargs):
        self._fd.write(*args, **kwargs)
        self.version += 1
        self.on_update(self, 'write', args, kwargs)

    def close(self):
        pass

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
