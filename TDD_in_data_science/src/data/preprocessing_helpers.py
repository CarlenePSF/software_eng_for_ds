import os
from dotenv import load_dotenv
load_dotenv()

project_path = "PROJECT"
default_path = "DEFAULT_PATH"


def row_to_list(row: str):
    if row.startswith("\t") or row[5] != "\t":
        return None
    else:
        return row.replace('\t', '-').replace('\n', '').split('-')


def convert_to_int(string: str):
    if '.' in string:
        return int(string.replace(".", ""))
    elif ',' in string:
        return int(string.replace(",", ""))
    else:
        return int(string)


def convert_to_float(string: str):
    if ',' in string:
        return float(string.replace(",", "."))
    else:
        return float(string)


def get_data_as_numpy_array(file):
    with open(file, 'r') as arquivo:
        arquivo.read()


get_data_as_numpy_array("/home/carlenepsf/PycharmProjects/software_eng_and_ds/software_eng_for_ds/TDD_in_data_science/data/example_clean_data.txt")
