from bank import value

def test_hello_greeting():
    assert value("hello") == 0


def test_h_greeting():
    assert value("hey, bro") == 20


def test_otherwords_greeting():
    assert value("What's up man? ") == 100


def test_case_insensitivity():
    assert value("HELLO") == 0