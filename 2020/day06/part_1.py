import textwrap
import typing


def count_unique_yay(group_answers: typing.List[str]) -> int:
    unique_answers = {item for answer in group_answers for item in answer}
    return len(unique_answers)


def parse_answers(input_str: str) -> typing.List:
    def parse_group_answers(group_answers_raw: str):
        return [answer for answer in group_answers_raw.split("\n") if answer != ""]

    return [parse_group_answers(group_answers_raw) for group_answers_raw in input_str.split("\n\n")]


def part_1(input_str: str) -> int:
    all_answers = parse_answers(input_str)
    return sum([count_unique_yay(group_answers) for group_answers in all_answers])


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
    assert (part_1(test_input)) == 11

    with open("./input.txt", "r") as f:
        input_str = f.read()

    print(f"result = {part_1(input_str)}")
