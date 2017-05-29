from dfs import File
import pytest
from pytest_mock import mocker

def test_append():
    block = File(name='somefile')

    assert block.version == 1
    block.write(b"test")
    assert block.version == 2


def test_block_hook(mocker):
    on_update = mocker.stub('on_update_stub')
    data = b'xxxx'

    file = File(name='somefile', on_update=on_update)
    file.write(data)

    on_update.assert_any_call(file, 'write', (data,), {})
    assert file.version == 2
