import typing
import re


policy_format = re.compile(r"(\d+)-(\d+) ([a-z]): ([a-z]+)")


def parse_entry(entry):
    min_occurrences, max_occurrences, char, passwd = [match for match in policy_format.split(entry) if match != ""]
    return int(min_occurrences), int(max_occurrences), char, passwd


def is_valid(entry):
    min_occurrences, max_occurrences, char, passwd = parse_entry(entry)
    return min_occurrences <= passwd.count(char) <= max_occurrences


def part_1(entries: typing.List[str]) -> int:
    return len([entry for entry in entries if is_valid(entry)])


if __name__ == "__main__":
    test_entries = [
        "1-3 a: abcde",
        "1-3 b: cdefg",
        "2-9 c: ccccccccc",
    ]
    assert part_1(test_entries) == 2

    with open("./input.txt", "r") as f:
        lines = f.read().splitlines()

    print(f"result = {part_1(lines)}")
