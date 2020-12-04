import typing
import textwrap

Passport = typing.Dict[str, str]
required_fields: typing.Final[typing.Set[str]] = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}


def is_valid_passport(passport: Passport) -> bool:
    return len(required_fields.difference(passport.keys())) == 0


def count_valid_passports(passports: typing.List[Passport]) -> int:
    return len([passport for passport in passports if is_valid_passport(passport)])


def parse_input(input_str: str) -> typing.List[Passport]:
    def parse_passport_data(entry_str: str) -> Passport:
        pairs = entry_str.replace("\n", " ").strip().split(" ")
        return dict([pair.split(":") for pair in pairs])

    return [parse_passport_data(passport_raw_data) for passport_raw_data in input_str.split("\n\n")]


if __name__ == "__main__":
    test_input = textwrap.dedent("""
    ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
    byr:1937 iyr:2017 cid:147 hgt:183cm

    iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
    hcl:#cfa07d byr:1929

    hcl:#ae17e1 iyr:2013
    eyr:2024
    ecl:brn pid:760753108 byr:1931
    hgt:179cm

    hcl:#cfa07d eyr:2025 pid:166559648
    iyr:2011 ecl:brn hgt:59in
    """)
    assert count_valid_passports(parse_input(test_input)) == 2

    with open("./input.txt", "r") as f:
        input_str = f.read()

    passports = parse_input(input_str)
    print(f"result = {count_valid_passports(passports)}")
