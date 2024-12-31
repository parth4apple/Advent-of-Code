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

def part1(grid):
    locs = defaultdict(list)
    grid = [list(x) for x in grid]
    m, n = len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j] != ".":
                locs[grid[i][j]].append((i, j))
    seen = set()
    for pts in locs.values():
        for i in range(len(pts)):
            for j in range(i+1, len(pts)):
                x1, y1 = pts[i]
                x2, y2 = pts[j]

                dx = x2-x1
                dy = y2-y1

                o1 = (x1-dx, y1-dy)
                o2 = (x2+dx, y2+dy)

                if 0 <= o1[0] < m and 0 <= o1[1] < n and o1 not in seen:
                    seen.add(o1)
                if 0 <= o2[0] < m and 0 <= o2[1] < n and o2 not in seen:
                    seen.add(o2)

    print(len(seen))

def part2(grid):
    locs = defaultdict(list)
    grid = [list(x) for x in grid]
    m, n = len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j] != ".":
                locs[grid[i][j]].append((i, j))
    seen = set()
    for pts in locs.values():
        for i in range(len(pts)):
            for j in range(i+1, len(pts)):
                x1, y1 = pts[i]
                x2, y2 = pts[j]

                dx = x2-x1
                dy = y2-y1

                xx, yy = x1, y1
                while True:
                    if 0 <= xx < m and 0 <= yy < n:
                        seen.add((xx, yy))
                    else:
                        break
                    xx -= dx
                    yy -= dy

                xx, yy = x2, y2
                while True:
                    if 0 <= xx < m and 0 <= yy < n:
                        seen.add((xx, yy))
                    else:
                        break
                    xx += dx
                    yy += dy

    print(len(seen))
            
if __name__ == "__main__":
  s = process()
  part1(s)
  part2(s)