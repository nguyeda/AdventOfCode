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


def count_trees(lines: typing.List[str], right: int, down: int) -> int:
    def reducer(acc, current):
        idx, line = current
        return acc + 1 if idx % down == 0 and is_tree(line, right * int(idx / down)) else acc

    return reduce(reducer, enumerate(lines), 0)


def part_2(lines: typing.List[str]) -> int:
    moves = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    all_tree_counts = [count_trees(lines, right, down) for right, down in moves]

    return reduce(lambda acc, current: acc * current, all_tree_counts, 1)


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
    assert part_2(test_entries) == 336

    with open("./input.txt", "r") as f:
        lines = f.read().splitlines()

    print(f"result = {part_2(lines)}")
