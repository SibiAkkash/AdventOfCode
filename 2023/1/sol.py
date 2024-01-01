#!/usr/bin/python3
import re


def first_and_last_digit(input: str) -> int:
    value = 0
    
    left = 0
    right = len(input) - 1
    first_num = -1
    last_num = -1
    
    while (first_num == -1 or last_num == -1) and (left <= right) and (left < len(input) and right >= 0):
        
        if first_num == -1:
            if input[left].isdigit():
                first_num = int(input[left])
            else:
                left += 1
            
        if last_num == -1:
            if input[right].isdigit():
                last_num = int(input[right])
            else:
                right -= 1
            
    return int(f'{first_num}{last_num}')


words_to_digit = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def first_and_last_digit_words_re(first_pattern: re.Pattern, last_pattern: re.Pattern, input: str) -> int:
    # we're guarenteed to have atleast 1 number/word in the string
    first = first_pattern.search(input).group(0)
    last = last_pattern.search(input[::-1]).group(0)
    
    first = words_to_digit.index(first) + 1 if (not first.isdigit()) else first
    last = words_to_digit.index(last[::-1]) + 1 if (not last.isdigit()) else last
    
    return int(f'{first}{last}')



if __name__ == "__main__":
    total = 0
    
    first_pattern = re.compile(r'\d')
    last_pattern  = re.compile(r'\d')
    
    first_pattern = re.compile(r'(one|two|three|four|five|six|seven|eight|nine|\d)')
    last_pattern  = re.compile(r'(eno|owt|eerht|ruof|evif|xis|neves|thgie|enin|\d)')
    
    with open("./input.txt", 'r') as file:
        lines = file.readlines()
        for line in lines:
            value = first_and_last_digit_words_re(first_pattern, last_pattern, line.strip())
            total += value
            
    print(total)