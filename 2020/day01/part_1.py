import typing
from itertools import combinations


def part_1(numbers: typing.List[int]) -> int:
    # for idx, current in enumerate(numbers):
    #     n = next((n for n in numbers[idx:] if current + n == 2020), None)
    #     if n is not None:
    #         return current * n

    couples = combinations(numbers, 2)
    return next(a * b for a, b in couples if a + b == 2020)


if __name__ == "__main__":
    test_entries = [979, 1721, 366, 299, 675, 1456]
    assert part_1(test_entries) == 514579

    with open("./input.txt", "r") as f:
        entries = [int(line) for line in f.read().splitlines()]

    print(f"result = {part_1(entries)}")
