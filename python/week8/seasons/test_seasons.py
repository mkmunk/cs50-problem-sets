import pytest
from week8.problemset8.seasons.seasons import calculate_minutes


def test_1():
    assert calculate_minutes("1999-10-10") == ("Fourteen million, one hundred thirty-three thousand, six hundred minutes")

def test_2():
    assert calculate_minutes("2024-01-01") == ("One million, three hundred ninety-one thousand forty minutes")