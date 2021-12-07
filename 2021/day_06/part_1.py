import typing
from collections import Counter
from functools import reduce


def main(lines: typing.List[int], duration: int) -> int:
    def reducer(acc: dict, _):
        census = {timer-1: population for timer, population in acc.items()}
        if -1 in census:
            census[8] = census.pop(-1)  # offsprings
            census[6] = census[8] + census.get(6, 0)  # new cycle + offsprings who reached 6
        return census

    population_by_timer = reduce(reducer, range(0, duration), dict(Counter(lines)))
    return sum(population_by_timer.values())


if __name__ == "__main__":
    test_entries = [3, 4, 3, 1, 2]
    assert main(test_entries, 18) == 26
    assert main(test_entries, 80) == 5934

    with open("./input.txt", "r") as f:
        lines = [int(it) for it in (f.read().splitlines()[0]).split(",")]

    print(f"result = {main(lines, 80)}")
