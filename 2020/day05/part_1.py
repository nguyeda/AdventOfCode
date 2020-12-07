import typing
from functools import reduce


def decoder(low: int, high: int, current: str, lower_half_code: str) -> typing.Tuple[int, int]:
    new_bound = (high - low + 1) // 2 + low
    return (low, new_bound - 1) if current == lower_half_code else (new_bound, high)


def decode_row(code: str) -> int:
    row_range = reduce(lambda acc, current: decoder(*acc, current, lower_half_code="F"), code, (0, 127))
    return row_range[0]


def decode_col(code: str) -> int:
    col_range = reduce(lambda acc, current: decoder(*acc, current, lower_half_code="L"), code, (0, 7))
    return col_range[0]


def decode_seat(code: str) -> typing.Tuple[int, int]:
    return decode_row(code[0:7]), decode_col(code[7:])


def seat_id(row: int, column: int) -> int:
    return row * 8 + column


def part_1(encoded_seats: typing.List[str]) -> int:
    seat_ids = [seat_id(*decode_seat(encoded)) for encoded in encoded_seats]
    return max(seat_ids)


if __name__ == "__main__":
    assert decode_seat("FBFBBFFRLR") == (44, 5)
    assert decode_seat("BFFFBBFRRR") == (70, 7)
    assert decode_seat("FFFBBBFRRR") == (14, 7)
    assert decode_seat("BBFFBBFRLL") == (102, 4)

    with open("./input.txt", "r") as f:
        lines = f.read().splitlines()

    print(f"result = {part_1(lines)}")
