import re
from collections import defaultdict

gears: dict[str, list[int]] = defaultdict(list)


def gear_position_hash(row: int, col: int) -> str:
    return f"{row},{col}"


def is_adjacent_to_symbol(part_num: int, row: int, col: int, lines: list[str]) -> bool:
    directions = [
        [-1, 0],  # up
        [1, 0],  # down
        [0, -1],  # left
        [0, 1],  # right
        [-1, -1],  # top left
        [-1, 1],  # top right
        [1, 1],  # bottom right
        [1, -1],  # bottom left
    ]

    for delta_row, delta_col in directions:
        check_row, check_col = row + delta_row, col + delta_col
        if (not 0 <= check_row < len(lines)) or (not 0 <= check_col < len(lines[0])):
            continue

        ch = lines[check_row][check_col]

        if ch != "." and not ch.isalnum():
            if ch == "*":
                gears[gear_position_hash(check_row, check_col)].append(part_num)

            return True

    return False


def sum_part_numbers(schematic_lines: list[str]) -> int:
    part_nums_total = 0

    for row, line in enumerate(schematic_lines):
        for match in re.finditer(r"\d+", line):
            part_number = int(match.group(0))
            start, end = match.span(0)

            if is_adjacent_to_symbol(
                part_number, row, start, schematic_lines
            ) or is_adjacent_to_symbol(part_number, row, end - 1, schematic_lines):
                part_nums_total += part_number

    return part_nums_total


schematic = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""


with open("./input.txt", "r") as f:
    schematic = list(map(lambda line: line.strip(), f.readlines()))
    print(sum_part_numbers(schematic))

sum_gear_ratios = 0

for gear_pos_str, part_nums in gears.items():
    if len(part_nums) == 2:
        sum_gear_ratios += part_nums[0] * part_nums[1]

print(sum_gear_ratios)
