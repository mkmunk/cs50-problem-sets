from twttr import shorten


def test_english():
    assert shorten("aaaabbbbcccc") == "bbbbcccc"


def test_big_english():
    assert shorten("AAAABBBBCCCC") == "BBBBCCCC"


def test_marks():
    assert shorten("AE,,,Bec") == ",,,Bc"


def test_number():
    assert shorten("1111aebb") =="1111bb"