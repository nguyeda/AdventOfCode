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


def part_2(encoded_seats: typing.List[str]) -> int:
    seat_ids = {seat_id(*decode_seat(encoded)) for encoded in encoded_seats}

    # as "the seats with IDs +1 and -1 from yours will be in your list", we can limit the search to the seats that are
    # within the allocated seat id range
    allocated_seat_ids_range = range(min(seat_ids), max(seat_ids) + 1)

    return next(s for s in allocated_seat_ids_range if s not in seat_ids)


if __name__ == "__main__":
    with open("./input.txt", "r") as f:
        lines = f.read().splitlines()

    print(f"result = {part_2(lines)}")
