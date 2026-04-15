from pathlib import Path
import json


def read_data(file_name, field):
    with open("file_name", "r" ) as f:
        data = json.load(f)

    if field not in data:
        return None

    return data[field]

def main():
    data = read_data("sequential.json", "unordered?numbers")
    print(data)
