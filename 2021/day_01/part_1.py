import typing
from functools import reduce


def main(lines: typing.List[int]) -> int:
    def measurement_reducer(acc, current_measurement):
        increase_count, previous_measurement = acc
        if previous_measurement is not None and previous_measurement < current_measurement:
            increase_count += 1
        return increase_count, current_measurement

    total_increase, _ = reduce(measurement_reducer, lines, (0, None))
    return total_increase


if __name__ == "__main__":
    test_entries = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    assert main(test_entries) == 7

    with open("./input.txt", "r") as f:
        lines = f.read().splitlines()

    print(f"result = {main([int(it) for it in lines])}")
