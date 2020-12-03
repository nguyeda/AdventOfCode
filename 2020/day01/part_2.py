import typing
from itertools import combinations


def part_2(numbers: typing.List[int]) -> int:
    trouples = combinations(numbers, 3)
    return next(a * b * c for a, b, c in trouples if a + b + c == 2020)


if __name__ == "__main__":
    test_entries = [979, 1721, 366, 299, 675, 1456]
    assert part_2(test_entries) == 241861950

    with open("./input.txt", "r") as f:
        entries = [int(line) for line in f.read().splitlines()]

    print(f"result = {part_2(entries)}")
