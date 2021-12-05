import typing
from dataclasses import dataclass
from functools import reduce


def main(lines: typing.List[str]) -> int:
    drawn_numbers_sequence = [int(it) for it in lines[0].split(",")]
    boards = _parse_boards(lines[2:])

    remaining_boards = list(boards[0:])
    for drawn_number in drawn_numbers_sequence:
        for board in remaining_boards[0:]:
            board.mark_number(drawn_number)
            if board.is_chicken_dinner():
                remaining_boards.remove(board)
                if len(remaining_boards) == 0:
                    return board.total_score(drawn_number)

    return -1

@dataclass
class Board:
    length = 5
    numbers: typing.List[typing.Optional[int]]

    def mark_number(self, number: int):
        if number in self.numbers:
            index = self.numbers.index(number)
            self.numbers[index] = None

    @property
    def rows(self):
        for index in range(0, self.length):
            start_index = index * self.length
            yield self.numbers[start_index: (start_index + self.length)]

    @property
    def columns(self):
        for index in range(0, self.length):
            yield [self.numbers[index + self.length * i] for i in range(0, self.length)]

    def is_chicken_dinner(self) -> bool:
        def is_full(seq: typing.Iterable[typing.Optional[int]]):
            return all(it is None for it in seq)

        for row, col in zip(self.rows, self.columns):
            if is_full(row) or is_full(col):
                return True

        return False

    def total_score(self, number: int) -> int:
        return sum([it for it in self.numbers if it]) * number


def _parse_boards(lines: typing.List[str]) -> typing.Iterable[Board]:
    def reducer(acc, current):
        if not current:
            board_numbers = []
        else:
            board_numbers = acc.pop() + [int(it) for it in current.split(" ") if it]
        return [*acc, board_numbers]

    return [Board(numbers=numbers) for numbers in reduce(reducer, lines, [[]])]


if __name__ == "__main__":
    test_entries = [
        "7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1",
        "",
        "22 13 17 11  0",
        "8  2 23  4 24",
        "21  9 14 16  7",
        "6 10  3 18  5",
        "1 12 20 15 19",
        "",
        "3 15  0  2 22",
        "9 18 13 17  5",
        "19  8  7 25 23",
        "20 11 10 24  4",
        "14 21 16 12  6",
        "",
        "14 21 17 24  4",
        "10 16 15  9 19",
        "18  8 23 26 20",
        "22 11 13  6  5",
        "2  0 12  3  7",
    ]
    assert main(test_entries) == 1924

    with open("./input.txt", "r") as f:
        lines = f.read().splitlines()

    print(f"result = {main(lines)}")
