
from typing import List


def num_valid_part1(pwd_list: List) -> int:
    valid_count = 0
    for line in pwd_list:
        # extract input
        parts = line.split(':')
        rule = parts[0]
        limits, letter = rule.split()
        ll, ul = list(map(int, limits.split('-')))
        pwd = parts[1].strip()

        # validate
        occurences = 0
        for char in pwd:
            if char == letter:
                occurences = occurences + 1

        if ll <= occurences <= ul:
            valid_count += 1

    return valid_count


def num_valid_part2(pwd_list: List) -> int:
    valid_count = 0
    for line in pwd_list:
        # extract input
        parts = line.split(':')
        rule = parts[0]
        limits, letter = rule.split()
        idx1, idx2 = list(map(int, limits.split('-')))
        pwd = parts[1].strip()
        print(idx1, idx2, pwd, letter)
        # validate
        valid = (pwd[idx1 - 1] is letter) ^ (pwd[idx2 - 1] is letter)
        if valid:
            valid_count += 1


    return valid_count


if __name__ == "__main__":
    input = []
    with open('./inputs/2.txt', 'r') as input_file:
        input_text = input_file.read()
        input = input_text.split('\n')

        print(num_valid_part2(input))
