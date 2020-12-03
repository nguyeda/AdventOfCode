import typing
import re


policy_format = re.compile(r"(\d+)-(\d+) ([a-z]): ([a-z]+)")

def parse_entry(entry):
    pos1, pos2, char, passwd = [match for match in policy_format.split(entry) if match != '']
    return int(pos1), int(pos2), char, passwd


def is_valid(entry):
    pos1, pos2, char, passwd = parse_entry(entry)
    return (passwd[pos1 - 1] == char) ^ (passwd[pos2 - 1] == char)


def part_2(entries: typing.List[str]) -> int:
    return len([entry for entry in entries if is_valid(entry)])


if __name__ == "__main__":
    test_entries = [
        "1-3 a: abcde",
        "1-3 b: cdefg",
        "2-9 c: ccccccccc",
    ]
    assert part_2(test_entries) == 1

    with open("./input.txt", "r") as f:
        lines = f.read().splitlines()

    print(f"result = {part_2(lines)}")
