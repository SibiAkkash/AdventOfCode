from __future__ import annotations
import re
from dataclasses import dataclass

@dataclass
class Number():
    n: int
    
    def __add__(self, other: Number) -> Number:
        return Number(self.n + other.n)
    
    def __sub__(self, other: Number) -> Number:
        return Number(self.n * other.n)
    
@dataclass
class Number_2():
    n: int
    
    def __add__(self, other: Number_2) -> Number_2:
        return Number_2(self.n * other.n)
    
    def __mul__(self, other: Number_2) -> Number_2:
        return Number_2(self.n + other.n)


def same_precendence(exp: str) -> int:
    pattern = r'(?P<number>\d+)'
    # https://docs.python.org/3/library/re.html
    repl = r'Number_2(\g<number>)'
    repl = r'Number_2(\g<1>)'
    repl = r'Number_2(\1)'
    
    modified_exp = re.sub(pattern=pattern, repl=repl, string=exp)
    modified_exp = modified_exp.replace('*', '/')
    modified_exp = modified_exp.replace('+', '*')
    modified_exp = modified_exp.replace('/', '+')
    
    result: Number = eval(modified_exp)
    return result.n
    

if __name__ == "__main__":
    with open('./input_1.txt', 'r') as f:
        total: int = 0
        while line := f.readline():
            total += same_precendence(line)
        print(total)        
        