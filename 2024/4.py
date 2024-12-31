import collections
import sys
from functools import lru_cache, cache, cmp_to_key
from itertools import zip_longest, product
import heapq
import math
import re
from utils import *

def process():
    s = []
    for line in sys.stdin:
        s.append(line.strip())
    return s

target = "XMAS"
def part1(input):
    result = 0
    m, n = len(input), len(input[0])
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]


    for i in range(m):
        for j in range(n):
            for dx, dy in dirs:
                ok = True
                ptr = 0
                x, y = i, j
                while 0 <= x < m and 0 <= y < n and ptr < 4:
                    if input[x][y] != target[ptr]:
                        ok = False
                        break
                    x += dx
                    y += dy
                    ptr += 1
                if ok and ptr == 4:
                    result += 1
            
    print(result)

def part2(input):
    m, n = len(input), len(input[0])
    result = 0
    sam, mas = "SAM", "MAS"
    forward = [[False] * n for _ in range(m)]
    back = [[False] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            x, y = i, j
            sok, mok = True, True
            for ptr in range(3):
                xx, yy = x+ptr, y+ptr
                if 0 <= xx < m and 0 <= yy < n:
                    if sam[ptr] != input[xx][yy]:
                        sok = False
                    if mas[ptr] != input[xx][yy]:
                        mok = False
                else:
                    sok, mok = False, False
            forward[i][j] = sok or mok

            x, y = i, j
            sok, mok = True, True
            for ptr in range(3):
                xx, yy = x+ptr, y-ptr
                if 0 <= xx < m and 0 <= yy < n:
                    if sam[ptr] != input[xx][yy]:
                        sok = False
                    if mas[ptr] != input[xx][yy]:
                        mok = False
                else:
                    sok, mok = False, False
            back[i][j] = sok or mok

    result = 0
    for i in range(m):
        for j in range(n):
            if j + 2 < n:
                result += (forward[i][j] and back[i][j+2])
    print(result)
            
if __name__ == "__main__":
  s = process()
  part1(s)
  part2(s)