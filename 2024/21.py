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

numeric = ["789", "456", "123", " 0A"]
directional = [" ^A", "<v>"]
dirs = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}

def process():
    s = []
    for line in sys.stdin:
        s.append(line.strip())
    return s

def getPad(pos, pad):
    x, y = pos

    if 0 <= x < len(pad) and 0 <= y < len(pad[0]) and pad[x][y] != " ":
        return pad[x][y]

    return None

def press(pos, move, nextPad):
    x, y = pos
    if move == "A":
        return (pos, getPad(pos, nextPad))
    else:
        x, y = pos
        dx, dy = dirs[move]
        return ((x+dx, y+dy), None)
    
def calculate(target):
    queue = deque([((3, 2), (0, 2), (0, 2), "")])
    seen = set()
    counter = 0
    while queue:
        for _ in range(len(queue)):
            obj = queue.popleft()
            p, a, b, chars = obj

            if target == chars:
                return counter
            elif not target.startswith(chars) or obj in seen:
                continue
            seen.add(obj)
            
            pp, pa, pb = getPad(p, numeric), getPad(a, directional), getPad(b, directional)
            if pp is None or pa is None or pb is None:
                continue
            for move in ["^", "<", ">", "v", "A"]:
                np, na = p, a
                newChars = chars
                nb, forA = press(b, move, directional)
                if forA is not None:
                    na, forB = press(a, forA, directional)
                    if forB is not None:
                        np, char = press(p, forB, numeric)
                        if char is not None:
                            newChars += char
                
                queue.append((np, na, nb, newChars))

        counter += 1

def part1(input):
    ans = 0
    for line in input:
        best = calculate(line)
        num = scanNums(line)[0]
        ans += best * num
    print(ans)

def explore(keypad, invalid_coords):
    adj = {}
    for x1 in range(len(keypad)):
        for y1 in range(len(keypad[0])):
            for x2 in range(len(keypad)):
                for y2 in range(len(keypad[0])):
                    path = '<' * (y1 - y2) +  'v' * (x2 - x1) + '^' * (x1 - x2) + '>' * (y2 - y1)
                    if invalid_coords == (x1, y2) or invalid_coords == (x2, y1):
                        path = path[::-1]
                    adj[(keypad[x1][y1], keypad[x2][y2])] = path + 'A'
    return adj

def part2(input):
    numericAdj = explore(numeric, (3, 0))
    directionalAdj = explore(directional, (0, 0)) 

    @cache
    def compute(toType, iters, flag=False) -> int:
        if iters == 0: 
            return len(toType)
        prev = 'A'
        tot = 0
        graph = numericAdj if flag else directionalAdj
        for char in toType:
            tot += compute(graph[(prev, char)], iters - 1) 
            prev = char
        return tot

    ans = 0
    for target in input:
        ans += int(target[:-1]) * compute(target, 26, True)

    print(ans)

if __name__ == "__main__":
  s = process()
  part1(s)
  part2(s)