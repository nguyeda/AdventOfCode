import typing
from itertools import islice, cycle
from functools import reduce


def nth(iterable, n, default=None):
    """
    Returns the nth item or a default value
    from itertools recipes
    """
    return next(islice(iterable, n, None), default)


def is_tree(line: str, at_pos: int) -> bool:
    return nth(cycle(line), at_pos) == "#"


def part_1(lines: typing.List[str]) -> int:
    def reducer(acc, current):
        idx, line = current
        return acc + 1 if is_tree(line, 3 * idx) else acc

    return reduce(reducer, enumerate(lines), 0)


if __name__ == "__main__":
    test_entries = [
        "..##.......",
        "#...#...#..",
        ".#....#..#.",
        "..#.#...#.#",
        ".#...##..#.",
        "..#.##.....",
        ".#.#.#....#",
        ".#........#",
        "#.##...#...",
        "#...##....#",
        ".#..#...#.#",
    ]
    assert part_1(test_entries) == 7

    with open("./input.txt", "r") as f:
        lines = f.read().splitlines()

    print(f"result = {part_1(lines)}")
