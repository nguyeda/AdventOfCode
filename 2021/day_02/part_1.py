import typing
from functools import reduce


def main(lines: typing.List[str]) -> int:
    def path_reducer(acc, current):
        action, quantity = current.split(" ")
        quantity = int(quantity)
        h, d = acc
        match action:
            case "forward":
                return h + quantity, d
            case "up":
                return h, d - quantity
            case "down":
                return h, d + quantity

    horizontal_position, depth = reduce(path_reducer, lines, (0, 0))
    return horizontal_position * depth


if __name__ == "__main__":
    test_entries = [
        "forward 5",
        "down 5",
        "forward 8",
        "up 3",
        "down 8",
        "forward 2",
    ]
    assert main(test_entries) == 150

    with open("./input.txt", "r") as f:
        lines = f.read().splitlines()

    print(f"result = {main(lines)}")
