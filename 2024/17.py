import collections
from collections import deque, defaultdict
import sys
from functools import lru_cache, cache, cmp_to_key
from itertools import zip_longest, product
import heapq
import math
import re
import sys
from utils import *
sys.setrecursionlimit(100000)

def process():
    s = ""
    for line in sys.stdin:
        s += line

    regInfo, progInfo = s.split("\n\n")
    registers = [scanNums(x)[0] for x in regInfo.split("\n")]
    program = scanNums(progInfo)
    
    return registers, program

def run(obj):
    (A, B, C), program = obj

    def getCombo(val):
        if val in [0, 1, 2, 3]:
            return val
        elif val == 4:
            return A
        elif val == 5:
            return B
        elif val == 6:
            return C
        else:
            assert False

    output = []
    ip = 0
    while ip < len(program):
        instr, operand = program[ip], program[ip+1]
        if instr == 0:
            A = A // (2**getCombo(operand))
        elif instr == 1:
            B = operand ^ B 
        elif instr == 2:
            B = getCombo(operand) % 8
        elif instr == 3:
            if A != 0 and ip != operand:
                ip = operand - 2
        elif instr == 4:
            B = B^C
        elif instr == 5:
            output.append(getCombo(operand) % 8)
        elif instr == 6:
            B = A // (2**getCombo(operand))
        elif instr == 7:
            C = A // (2**getCombo(operand))
        else:
            assert False

        ip += 2

    return output

def part1(obj):
    ans = ",".join([str(x) for x in run(obj)])
    print(ans)

def part2(obj):
    """
    2 4
    B = x % 8
    1 1
    B = B ^ 1
    7 5
    C = A // 2**B
    4 4
    B = B ^ C
    1 4
    B = B ^ A
    0 3
    A = A // 3
    5 5
    print (B % 8)
    3 0
    repeat if A > 0
    """
    target = obj[1]
    queue = deque([x for x in range(1024)])
    ans = None
    p = 1024
    for idx in range(len(obj[1])):
        for _ in range(len(queue)):
            cur = queue.popleft()
            partial = run(((cur, 0, 0), obj[1]))
            if target == partial and (ans is None or ans > cur):
                ans = cur
                break
            elif idx < len(partial) and target[idx] == partial[idx]:
                for i in range(8):
                    queue.append(cur + p * i)
            
        p *= 8
                
    print(ans)
            
if __name__ == "__main__":
  s = process()
  part1(s)
  part2(s)