import textwrap
import typing
from collections import Counter
from functools import reduce


def count_all_yay(group_answers: typing.List[str]) -> int:
    answers_occurrences = reduce(lambda counter, answers: Counter(answers) + counter, group_answers, Counter())
    return len(
        [answer for answer, occurrences in answers_occurrences.items() if occurrences // len(group_answers) == 1]
    )


def parse_answers(input_str: str) -> typing.List:
    def parse_group_answers(group_answers_raw: str):
        return [answer for answer in group_answers_raw.split("\n") if answer != ""]

    return [parse_group_answers(group_answers_raw) for group_answers_raw in input_str.split("\n\n")]


def part_2(input_str: str) -> int:
    all_answers = parse_answers(input_str)
    return sum([count_all_yay(group_answers) for group_answers in all_answers])


if __name__ == "__main__":
    test_input = textwrap.dedent(
        """
        abc
    
        a
        b
        c
    
        ab
        ac
    
        a
        a
        a
        a
    
        b
        """
    )
    assert (part_2(test_input)) == 6

    with open("./input.txt", "r") as f:
        input_str = f.read()

    print(f"result = {part_2(input_str)}")
