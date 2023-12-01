import textwrap
from typing import List, Optional

DIGIT_STRINGS = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
]


def read_data_file(filename: str) -> str:
    with open(filename, "r", encoding="utf-8") as handle:
        return handle.read()


def get_lines(text: str) -> List[str]:
    trimmed = [x.strip() for x in text.split("\n")]
    non_empty_lines = filter(lambda x: x, trimmed)
    return non_empty_lines


def get_prefix_number(value: str) -> Optional[int]:
    """
    if the value starts with a number, return that value
    onetwo -> 1
    43two -> 1
    zone -> None
    """
    if not value:
        return None

    try:
        v = int(value[0])
        return v
    except:
        pass

    # iterate through 'one', 'two', 'three'
    for digit_value_minus_one, digit in enumerate(DIGIT_STRINGS):
        if value.startswith(digit):
            return digit_value_minus_one + 1

    return None


def get_calibration_value(line: str) -> int:
    numbers = []

    # find the first number going forward
    for i in range(len(line)):
        number = get_prefix_number(value=line[i:])
        if number:
            numbers.append(number)
            break

    # find the first number going backward
    for i in range(len(line)):
        number = get_prefix_number(value=line[-1 - i :])
        if number:
            numbers.append(number)
            break

    value = int(str(numbers[0]) + str(numbers[-1]))
    return value


def solve(lines: List[str]) -> int:

    values = [get_calibration_value(line=x) for x in lines]
    total = sum(values)
    return total


data_file = "data/2023_day_1.txt"

if data_file:
    raw = read_data_file("data/2023_day_1.txt")
else:
    raw = textwrap.dedent(
        """
        two1nine
        eightwothree
        abcone2threexyz
        xtwone3four
        4nineeightseven2
        zoneight234
        7pqrstsixteen
    """
    )

lines = get_lines(text=raw)
print(solve(lines=lines))
