import typing
import textwrap
import re

Passport = typing.Dict[str, str]
required_fields: typing.Final[typing.Set[str]] = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
allowed_eye_colors: typing.Final[typing.Set[str]] = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
passport_id_pattern: typing.Final = re.compile(r"^\d{9}$")
height_pattern: typing.Final = re.compile(r"^(\d{3})(cm)$|^(\d{2})(in)$")
hair_color_pattern: typing.Final = re.compile(r"^#[0-9a-f]{6}$")


def is_valid_year(value: str, min_allowed: int, max_allowed: int) -> bool:
    try:
        return min_allowed <= int(value) <= max_allowed
    except ValueError:
        return False


def is_valid_height(value: str) -> bool:
    match = height_pattern.match(value)
    if match is None:
        return False

    height, unit = (match for match in match.groups() if match is not None)
    min_allowed, max_allowed = (150, 193) if unit == "cm" else (59, 76)

    return min_allowed <= int(height) <= max_allowed


def is_valid_passport(passport: Passport) -> bool:
    return (
        len(required_fields.difference(passport.keys())) == 0
        and passport["ecl"] in allowed_eye_colors
        and passport_id_pattern.match(passport["pid"])
        and hair_color_pattern.match(passport["hcl"])
        and is_valid_year(passport["byr"], 1920, 2002)
        and is_valid_year(passport["iyr"], 2010, 2020)
        and is_valid_year(passport["eyr"], 2020, 2030)
        and is_valid_height(passport["hgt"])
    )


def filter_valid_passports(passports: typing.List[Passport]) -> typing.List[Passport]:
    return [passport for passport in passports if is_valid_passport(passport)]


def parse_input(input_str: str) -> typing.List[Passport]:
    def parse_passport_data(entry_str: str) -> Passport:
        pairs = entry_str.replace("\n", " ").strip().split(" ")
        return dict([pair.split(":") for pair in pairs])

    return [parse_passport_data(passport_raw_data) for passport_raw_data in input_str.split("\n\n")]


if __name__ == "__main__":
    test_input_invalids = textwrap.dedent(
        """
        eyr:1972 cid:100
        hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926
    
        iyr:2019
        hcl:#602927 eyr:1967 hgt:170cm
        ecl:grn pid:012533040 byr:1946
    
        hcl:dab227 iyr:2012
        ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277
    
        hgt:59cm ecl:zzz
        eyr:2038 hcl:74454a iyr:2023
        pid:3556412378 byr:2007
    
        hgt:59cm
        eyr:2038 hcl:74454a iyr:2023
        pid:3556412378 byr:2007
    
        eyr:2029 ecl:blu cid:129 byr:1989
        iyr:2014 pid:8960565391 hcl:#a97842 hgt:165cm
        """
    )
    assert len(filter_valid_passports(parse_input(test_input_invalids))) == 0

    test_input_valids = textwrap.dedent(
        """
        pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
        hcl:#623a2f
    
        eyr:2029 ecl:blu cid:129 byr:1989
        iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm
    
        hcl:#888785
        hgt:164cm byr:2001 iyr:2015 cid:88
        pid:545766238 ecl:hzl
        eyr:2022
    
        iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
        """
    )
    assert len(filter_valid_passports(parse_input(test_input_valids))) == 4

    with open("./input.txt", "r") as f:
        input_str = f.read()

    passports = parse_input(input_str)
    print(f"result = {len(filter_valid_passports(passports))}")
