import pytest

from my_module import my_sum, my_division


def test_sum_int():
    """it adds two integers and returns integer"""
    assert my_sum(1, 1) == 2


def test_sum_float():
    """it adds an integer and a float and returns float"""
    assert my_sum(1.5, 1) == 2.5


def test_division():
    """It divides an integer by another integer and returns an integer"""
    assert my_division(4, 2) == 2
