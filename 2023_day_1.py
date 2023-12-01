from typing import List
import textwrap

def read_data_file(filename: str) -> str:
    with open(filename, 'r', encoding='utf-8') as handle:
        return handle.read()

def get_lines(text: str) -> List[str]:
    trimmed = [x.strip() for x in text.split('\n')]
    non_empty_lines = filter(lambda x: x, trimmed)
    return non_empty_lines

def get_calibration_value(line: str) -> int:
    numbers = []
    for letter in line:
        try:
            v = int(letter)
            numbers.append(letter)
        except: 
            pass
    value = int(numbers[0] + numbers[-1])
    return value

def solve(lines: List[str]) -> int:

    values = [get_calibration_value(line=x) for x in lines]
    total = sum(values)
    return total


#data_file = None
data_file = 'data/2023_day_1.txt'

if data_file:
    raw = read_data_file('data/2023_day_1.txt')
else:
    raw = textwrap.dedent("""
        1abc2
        pqr3stu8vwx
        a1b2c3d4e5f
        treb7uchet
        """)

lines = get_lines(text = raw)
print(solve(lines=lines))
