from um import count
import pytest

def test_1():
    assert count("UM,UM") == 2

def test_2():
    assert count("umum") == 0

def test_3():
    assert count("hello, my name is wayne. your name is um.") == 1