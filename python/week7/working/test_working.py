from working import convert
import pytest


def test_1():
    assert convert("1 AM to 2 AM") == ("01:00 to 02:00")

def test_2():
    assert convert("1:05 PM to 1 AM") == ("13:05 to 01:00")

def test_3():
    with pytest.raises(ValueError):
        convert("13:01 PM to 11:10 AM")

def test_4():
    assert convert("12:00 AM to 12 PM") == ("00:00 to 12:00")

def test_5():
    with pytest.raises(ValueError):
        convert("111")