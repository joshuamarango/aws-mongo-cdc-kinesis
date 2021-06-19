import pytest

def subtract(x:int, y:int) -> int:
    return x - y

def test_subtract():
    assert subtract(2,1) == 1