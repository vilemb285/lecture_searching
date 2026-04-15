from pathlib import Path
import json


def read_data(file_name, field):
    cwd_path = Path.cwd()
    file_path = cwd_path / file_name

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if field not in data:
        return None

    return data[field]

def linear_search(sequence, found_key):
    dict = {
        "positions": [],
        "count" : 0
    }

    for i, value in enumerate(sequence):
        if found_key == value:
            dict["positions"].append(i)
            dict["count"] += 1
    return dict

def main():
    data = read_data("sequential.json", "unordered_numbers")
    search = linear_search("sequential.json",2)
    print(data)
    print(search)

if __name__ == "__main__":
    main()