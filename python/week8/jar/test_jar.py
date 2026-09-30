import pytest
from jar import Jar


def test_init():
    jar = Jar(11)
    assert jar.capacity == 11
    jar = Jar(20)
    assert jar.capacity == 20
    with pytest.raises(ValueError):
        jar = Jar(-10)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert jar.size == 1
    jar.deposit(5)
    assert jar.size == 6
    with pytest.raises(ValueError):
        jar.deposit(7)

def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(3)
    assert jar.size == 9
    jar.withdraw(6)
    assert jar.size == 3
    with pytest.raises(ValueError):
        jar.withdraw(4)