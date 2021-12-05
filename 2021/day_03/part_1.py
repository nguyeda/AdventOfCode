import typing
from functools import reduce


def main(lines: typing.List[str]) -> int:
    def common_bits_reducer(acc, current):
        g, e = acc
        append_g, append_d = ('1', '0') if current.count("1") > len(current)/2 else ('0', '1')
        return g + append_g, e + append_d

    transposed = zip(*map(lambda s: list(s), lines))
    gamma, epsilon = reduce(common_bits_reducer, transposed, ("", ""))
    return int(gamma, 2) * int(epsilon, 2)


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
    assert main(test_entries) == 198

    with open("./input.txt", "r") as f:
        lines = f.read().splitlines()

    print(f"result = {main(lines)}")
