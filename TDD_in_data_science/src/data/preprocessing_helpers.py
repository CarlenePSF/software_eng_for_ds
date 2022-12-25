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
