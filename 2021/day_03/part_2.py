import typing
from collections import Counter


def _get_ratings(ratings: typing.List[str], extract_filtering_bit: typing.Callable[[Counter], str]) -> int:
    i = 0
    while len(ratings) > 1:
        bit = extract_filtering_bit(Counter([it[i] for it in ratings]))
        ratings = [it for it in ratings if it[i] == bit]
        i += 1
    return int(ratings[0], 2)


def get_o2_ratings(ratings: typing.List[str]) -> int:
    return _get_ratings(ratings, lambda counter: "1" if counter["1"] >= counter["0"] else "0")


def get_co2_ratings(ratings: typing.List[str]) -> int:
    return _get_ratings(ratings, lambda counter: "0" if counter["0"] <= counter["1"] else "1")


def main(lines: typing.List[str]) -> int:
    return get_o2_ratings(lines) * get_co2_ratings(lines)


if __name__ == "__main__":
    test_entries = [
        '00100',
        '11110',
        '10110',
        '10111',
        '10101',
        '01111',
        '00111',
        '11100',
        '10000',
        '11001',
        '00010',
        '01010',
    ]
    assert main(test_entries) == 230

    with open("./input.txt", "r") as f:
        lines = f.read().splitlines()

    print(f"result = {main(lines)}")
