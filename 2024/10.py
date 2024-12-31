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

def explore(grid, i, j, part2):
    p2 = 0
    q = deque([(i, j, 0)])
    m, n = len(grid), len(grid[0])
    seen = set()

    while len(q) > 0:
        ni, nj, c = q.popleft()

        if c == 9:
            p2 += 1
            seen.add((ni, nj))
            continue
            
        for ii, jj in (ni+1, nj), (ni-1, nj), (ni, nj+1), (ni, nj-1):
            if 0 <= ii < m and 0 <= jj < n and str(c+1) == grid[ii][jj]:
                q.append((ii, jj, c+1))
    
    p1 = len(seen)
    return p2 if part2 else p1

def part1(grid, part2=False):
    grid = [list(d) for d in grid]

    m, n = len(grid), len(grid[0])
    tot = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "0":
                tot+= explore(grid, i, j, part2)
    print(tot)

def part2(grid):
    part1(grid, True)
            
if __name__ == "__main__":
  s = process()
  part1(s)
  part2(s)