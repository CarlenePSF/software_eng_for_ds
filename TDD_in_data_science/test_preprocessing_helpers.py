import pytest
import numpy as np
import os
from dotenv import load_dotenv

from src.data.preprocessing_helpers import (row_to_list,
                                            convert_to_int,
                                            convert_to_float)
from src.features.features_helpers import get_data_as_numpy_array

load_dotenv()
project_path = "PROJECT"
default_path = "DEFAULT_PATH"


def test_for_clean_row():
    assert row_to_list("2,081\t314,942\n") == ["2,081", "314,942"]


def test_for_missing_area():
    assert row_to_list("\t293,410\n") is None


# refactoring the test with a message
def test_for_missing_area_with_message():
    actual = row_to_list("\t293,410\n")
    expected = None
    message = ("row_to_list('\t293,410\n')"
               "returned {0} instead"
               "or {1}".format(actual, expected)
               )
    assert actual is expected, message


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


def test_on_clean_file():
    expected = np.array(
        [[2081.0, 314942.0],
         [1059.0, 186606.0],
         [1148.0, 206186.0]]
    )
    actual = get_data_as_numpy_array(os.getenv(project_path)+"/data/example_clean_data.txt")
    message = f"Expected return value: {expected}, Actual return value: {actual}"
    # Complete the assert statement
    assert actual == pytest.approx(expected), message

