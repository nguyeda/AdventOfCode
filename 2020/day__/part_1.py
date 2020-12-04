import typing


def part_1(lines: typing.List[str]) -> int:
    pass


if __name__ == "__main__":
    test_entries = []
    assert part_1(test_entries) == None

    with open("./input.txt", "r") as f:
        lines = f.read().splitlines()

    print(f"result = {part_1(lines)}")
