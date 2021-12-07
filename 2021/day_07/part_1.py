import typing
from collections import Counter
from functools import reduce
from statistics import median

def get_fuel_consumption(target_position: int, population_by_position: Counter) -> int:
    def reducer(acc, current) -> int:
        position, population = current
        return acc + (abs(position - target_position) * population)

    return reduce(reducer, population_by_position.items(), 0)


def main(lines: typing.List[int]) -> int:
    target_position = round(median(lines))
    return get_fuel_consumption(target_position, Counter(lines))


if __name__ == "__main__":
    test_entries = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    assert main(test_entries) == 37

    with open("./input.txt", "r") as f:
        lines = [int(it) for it in (f.read().splitlines()[0]).split(",")]

    print(f"result = {main(lines)}")
