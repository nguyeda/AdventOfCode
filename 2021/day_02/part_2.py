import typing
from functools import reduce


def main(lines: typing.List[str]) -> int:
    def path_reducer(acc, current):
        action, quantity = current.split(" ")
        quantity = int(quantity)
        h, d, a = acc
        match action:
            case "forward":
                return h + quantity, d + a * quantity, a
            case "up":
                return h, d, a - quantity
            case "down":
                return h, d, a + quantity

    horizontal_position, depth, aim = reduce(path_reducer, lines, (0, 0, 0))
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
    assert main(test_entries) == 900

    with open("./input.txt", "r") as f:
        lines = f.read().splitlines()

    print(f"result = {main(lines)}")
