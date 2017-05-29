from dfs import File

import hashlib
import random


def test_versioning(file):
    assert file.version == 1

    file.write(b"test")
    assert file.version == 2


def test_update_hook(mocker):
    on_update = mocker.stub('on_update_stub')
    data = b'xxxx'

    file = File(name='somefile', on_update=on_update)
    file.write(data)

    on_update.assert_any_call(file, 'write', (data,), {})


def test_digest(file):
    data = b'abcdef'
    file.write(data)

    expected_hash = hashlib.sha256(data).hexdigest()
    assert expected_hash == file.sha256()


def test_read_write(file):
    data = b'\x00 somedata \xff'
    file.write(data)
    file.seek(0)

    read_data = file.read()
    assert read_data == data


def test_read_write_big(file):
    data = bytes(random.randint(0, 255) for x in range(1000**2))
    file.write(data)
    file.seek(0)

    read_data = file.read()
    assert read_data == data
