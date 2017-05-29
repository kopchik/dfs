import pytest

from dfs import File


@pytest.fixture()
def file():
    return File(name='<test_file_name>')