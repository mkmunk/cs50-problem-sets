import pytest
from fuel import convert, gauge


def test_convert():
    assert convert("3/4") == 75


def test_convert_y_zero():
    with pytest.raises(ZeroDivisionError):
        convert("5/0")


def test_convert_x_nagetive():
    with pytest.raises(ValueError):
        convert("-1/1")


def test_gauge_1():
    assert gauge(1) == "E"
    assert gauge(2) == "2%"
    assert gauge(99) == "F"


