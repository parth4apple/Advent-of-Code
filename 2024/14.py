import collections
from collections import deque, defaultdict
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

def part1(input):
    qs = [0] * 4
    # m, n = 103, 101    
    m, n = 7, 11
    for line in input:
        sx, sy, dx, dy = scanNums(line)
        for _ in range(100):
            sx = (sx+dx) % n
            sy = (sy+dy) % m
        
        if sx < n // 2 and sy < m // 2:
            qs[0] += 1
        elif sx > n // 2 and sy < m // 2:
            qs[1] += 1
        elif sx < n // 2 and sy > m // 2:
            qs[2] += 1
        elif sx > n // 2 and sy > m //2:
            qs[3] += 1  

    tot = 1
    for x in qs:
        tot *= x
    print(tot)

        

def part2(input):
    m, n = 103, 101    
    # m, n = 7, 11
    nums = []
    for line in input:
        nums.append(scanNums(line))

    def check(pos, i):
        grid = [[" "] * n for _ in range(m)]

        for y, x, _, _ in pos:
            grid[x][y] = "*"

        possible = False
        for row in grid:
            if "*" * 10 in "".join(row):
                possible = True
        if not possible:
            return False
        # uncomment to see christmas tree
        # print(i, "-----------------------")
        # for row in grid:
        #     print("".join(row))
        # print("-----------------------")
        return True

    for i in range(500000):
        for item in nums:
            item[0] = (item[0] + item[2]) % n
            item[1] = (item[1] + item[3]) % m
        
        if check(nums, i):
            print(i+1)
            break
        
            
if __name__ == "__main__":
  s = process()
  part1(s)
  part2(s)