import collections
from collections import deque, defaultdict
import sys
from functools import lru_cache, cache, cmp_to_key
from itertools import zip_longest, product
import heapq
import math
import re
import time
from utils import *

def process():
    s = []
    for line in sys.stdin:
        s.append(line.strip())
    return s

def part1(grid, part2=False):
    m, n = len(grid), len(grid[0])

    x, y = 0, 0
    vecs = ["^", ">", "v", "<"]
    dirs = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
    for i in range(m):
        for j in range(n):
            if grid[i][j] not in [".", "#"]:
                x, y = i, j
                dir = vecs.index(grid[i][j])    
    
    vis = set([(x, y, dir)])
    seen = set([(x, y)])
    q = deque([(x, y, dir)])
    loop = True
    while q:
        cx, cy, d = q.popleft()
        dx, dy = dirs[vecs[d]]
        while 0 <= cx+dx < m and 0 <= cy+dy < n and grid[cx+dx][cy+dy] != "#":
            cx, cy = cx+dx, cy+dy
            seen.add((cx, cy))
        if not (0 <= cx+dx < m and 0 <= cy+dy < n):
            loop = False
            break
        d = (d+1) % 4
        if (cx, cy, d) not in vis:
            vis.add((cx, cy, d))
            q.append((cx, cy, d))
    
    if not part2:
        print(len(seen))
    return 1 if loop else 0
                
def part2(grid):
    res = 0
    grid = [list(x) for x in grid]

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] in ".":
                grid[i][j] = "#"
                res += part1(grid, True)
                grid[i][j] = "."

    print(res)
            
if __name__ == "__main__":
    s = process()
    part1(s)
    part2(s)