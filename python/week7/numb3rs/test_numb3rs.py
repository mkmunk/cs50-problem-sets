from numb3rs import validate


def test_1234():
    assert validate("111.111.111.111") == True

def test_5678():
    assert validate("01.0.1.1") == False

def test_1():
    assert validate("1.999.1.1") == False