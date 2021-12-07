import typing
from collections import Counter
from functools import reduce


def get_fuel_consumption(target_position: int, population_by_position: Counter) -> int:
    def reducer(acc, current) -> int:
        position, population = current
        return acc + (abs(position - target_position) * population)

    return reduce(reducer, population_by_position.items(), 0)


def main(lines: typing.List[int]) -> int:
    positions_population = Counter(lines)
    # TODO: do not brute force to calculate the target position
    return sorted([
        get_fuel_consumption(to_pos, positions_population)
        for to_pos in range(min(lines) + 1, max(lines))
    ]).pop(0)


if __name__ == "__main__":
    test_entries = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    assert main(test_entries) == 37

    with open("./input.txt", "r") as f:
        lines = [int(it) for it in (f.read().splitlines()[0]).split(",")]

    print(f"result = {main(lines)}")
