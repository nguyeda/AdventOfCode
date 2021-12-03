import typing
from functools import reduce
from itertools import pairwise


def triplewise(iterable):
    # from recipes in https://docs.python.org/3/library/itertools.html
    for (a, _), (b, c) in pairwise(pairwise(iterable)):
        yield a, b, c


def main(lines: typing.List[int]) -> int:
    def measurement_reducer(
            acc: typing.Tuple[int, typing.Optional[int]],
            current_measurement_triplet: typing.Tuple[int, int, int],
    ):
        increase_count, previous_measurement = acc
        current_measurement_triplet = sum(current_measurement_triplet)
        if previous_measurement is not None and previous_measurement < current_measurement_triplet:
            increase_count += 1
        return increase_count, current_measurement_triplet

    total_increase, _ = reduce(measurement_reducer, triplewise(lines), (0, None))
    return total_increase


if __name__ == "__main__":
    test_entries = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    assert main(test_entries) == 5

    with open("./input.txt", "r") as f:
        lines = f.read().splitlines()

    print(f"result = {main([int(it) for it in lines])}")
