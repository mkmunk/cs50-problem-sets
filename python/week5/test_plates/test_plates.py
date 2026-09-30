from plates import is_valid


def test_beginning_alphabetical():
    assert is_valid("11") == False


def test_length():
    assert is_valid("eieiei1") == False


def test_number_placement():
    assert is_valid("e2iei") == False


def test_zero_placement():
    assert is_valid("eieie0") == False


def test_alphanumeric_characters():
    assert is_valid("dieifi") == True
