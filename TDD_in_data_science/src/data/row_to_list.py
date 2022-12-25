

def row_to_list(row: str):
    if row.startswith("\t") or row[5] != "\t":
        return None
    else:
        return row.replace('\t', '-').replace('\n', '').split('-')


