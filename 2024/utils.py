import re

def scanNums(s: str) -> list:
    matches = re.findall(r'-?\d+', s)
    return [int(m) for m in matches]