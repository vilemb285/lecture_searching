import time
from pathlib import Path
import json
import time


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
        "count" : 0,
    }

    for i, value in enumerate(sequence):
        if found_key == value:
            dict["positions"].append(i)
            dict["count"] += 1


    return dict

def binary_search(sequence, found_key):
    left = 0
    right = len(sequence) - 1
    while left <= right:
        middle = (left + right) // 2

        if sequence == sequence:
            return middle
        elif sequence < found_key:
            left = middle + 1
        elif sequence > found_key:
            right = middle - 1
    return None

def main():
    data = read_data("sequential.json", "unordered_numbers")
    search = linear_search(data,2)
    print(data)
    print(search)
    data_ordered = binary_search("sequential.json", " ordered_numbers")
    search_ordered = binary_search(data_ordered, 2)
    print(data_ordered)
    print(search_ordered)
    duration = 0
    repetitions = 100
    for measurements in range(100):
        start_time = time.perf_counter()
        found_num = linear_search(data, 0)
        end_time = time.perf_counter()
        duration += end_time - start_time
    print(duration)

if __name__ == "__main__":
    main()