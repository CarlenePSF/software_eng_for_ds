import pytest
from src.data.preprocessing_helpers import (row_to_list,
                                            convert_to_int,
                                            convert_to_float)


def test_for_clean_row():
    assert row_to_list("2,081\t314,942\n") == ["2,081", "314,942"]


def test_for_missing_area():
    assert row_to_list("\t293,410\n") is None


def test_for_missing_area_with_message():
    assert row_to_list("\t293,410\n") is None


def test_for_missing_tab():
    assert row_to_list("1,463238,765\n") is None


# Complete the unit test name by adding a prefix
def test_convert_to_int():
    assert convert_to_int("2,841") == 2841
    assert convert_to_int("2.841") == 2841
    assert convert_to_int("2841") == 2841


def test_convert_to_float():
    assert convert_to_float("2841.05") == 2841.05
    assert convert_to_float("2841,05") == 2841.05


