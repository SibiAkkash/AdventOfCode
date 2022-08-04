# https://adventofcode.com/2020/day/1

from typing import List


def find_sum(expenses: List, target: int, exclude: int = []) -> int:
    seen = set()
    for i in range(len(expenses)):
        value = expenses[i]
        if i == exclude:
            continue
        if (target - value) not in seen:
            seen.add(value)
        else:
            print(value, target-value)
            return value * (target - value)
    return -1


def find_triple_sum(expenses: List, target: int) -> int:
    seen = set()
    # for each value, find 2 numbers such that they add up to target-value
    for i in range(len(expenses)):
        value = expenses[i]
        inter = target - value
        inter_prod = find_sum(expenses, inter, exclude=i)
        if inter_prod != -1:
            print(value)
            return value * inter_prod
        else:
            seen.add(value)

    return -1


if __name__ == "__main__":
    input = []
    with open('./inputs/1.txt', 'r') as input_file:
        input_text = input_file.read()
        input = list(map(int, input_text.split('\n')))

    print(find_sum(input, 2020))
    print(find_triple_sum(input, target=2020))

    # a, b, c in list
    # a + b + c = target
    # cubic -> brute, quad -> repeat find_sum() 'n' times
