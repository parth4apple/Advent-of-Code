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
    s = []
    for line in sys.stdin:
        s.append(tuple(scanNums(line)))

    return s

def simulate(grid):
    size = 70
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    queue = deque([(0, 0)])
    seen = set([(0, 0)])
    steps = 0
    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()

            if x == size and y == size:
                return steps
            
            for dx, dy in dirs:
                xx, yy = x+dx, y+dy
                if 0 <= xx < size+1 and 0 <= yy < size+1 and grid[xx][yy] == "." and (xx, yy) not in seen:
                    seen.add((xx, yy))
                    queue.append((xx, yy))

        steps += 1

    return 10**20
    
def part1(blocked):
    size = 70
    grid = [["."] * (size+1) for _ in range(size+1)]
    for i in range(1024):
        x, y = blocked[i]
        grid[y][x] = "#"
    ans = simulate(grid)
    print(ans)

def part2(blocked):
    size = 70
    grid = [["."] * (size+1) for _ in range(size+1)]
    for i, (x, y) in enumerate(blocked):
        grid[y][x] = "#"
        if simulate(grid) == 10**20:
            print(f"{x},{y}")
            break
            
if __name__ == "__main__":
  s = process()
  part1(s)
  part2(s)