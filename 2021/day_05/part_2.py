import typing
from functools import reduce
from collections import defaultdict
from itertools import chain


def main(lines: typing.List[str]) -> int:
    vectors = filter(
        lambda c: (c[0] == c[2]) or (c[1] == c[3]) or (abs(c[0] - c[2]) == abs(c[1] - c[3])),
        _parse_coordinates(lines)
    )

    def _get_range(start: int, end: int) -> range:
        step = 1 if start <= end else -1
        return range(start, end + step, step)

    def _get_covered_points(vector: typing.Tuple[int, int, int, int]) -> typing.Iterable[typing.Tuple[int, int]]:
        x1, y1, x2, y2 = vector
        if y1 == y2:
            return [(x, y1) for x in _get_range(x1, x2)]
        if x1 == x2:
            return [(x1, y) for y in _get_range(y1, y2)]
        return [(x, y) for x, y in zip(_get_range(x1, x2), _get_range(y1, y2))]

    def reducer(acc, vector: typing.Tuple[int, int, int, int]):
        for x, y in _get_covered_points(vector):
            acc[x][y] += 1
        return acc

    vents_map = reduce(reducer, vectors, defaultdict(lambda: defaultdict(lambda: 0)))
    return len([val for val in chain(*[it.values() for it in vents_map.values()]) if val > 1])


def _parse_coordinates(lines: typing.List[str]) -> typing.Iterable[typing.Tuple[int, int, int, int]]:
    def parser(line: str) -> typing.Tuple:
        return tuple([int(it.strip()) for it in line.replace(" -> ", ", ").split(",")])

    return map(parser, lines)


if __name__ == "__main__":
    test_entries = [
        "0, 9 -> 5, 9",
        "8, 0 -> 0, 8",
        "9, 4 -> 3, 4",
        "2, 2 -> 2, 1",
        "7, 0 -> 7, 4",
        "6, 4 -> 2, 0",
        "0, 9 -> 2, 9",
        "3, 4 -> 1, 4",
        "0, 0 -> 8, 8",
        "5, 5 -> 8, 2",
    ]
    assert main(test_entries) == 12

    with open("./input.txt", "r") as f:
        lines = f.read().splitlines()

    print(f"result = {main(lines)}")
