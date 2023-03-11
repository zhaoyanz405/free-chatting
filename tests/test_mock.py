import pytest
from mocks import string

def test_string():

    @string
    def func(a, b):
        pass

    res = func()
    assert not res

