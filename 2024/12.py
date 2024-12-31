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
    grid = [list(x) for x in grid]
    m, n = len(grid), len(grid[0])
    tot = 0
    seen = set()

    def explore(i, j):
        vis, q = set([(i, j)]), deque([(i, j)])

        while q:
            ci, cj = q.popleft()

            for ii, jj in (ci+1, cj), (ci-1, cj), (ci, cj+1), (ci, cj-1):
                if 0 <= ii < m and 0 <= jj < n and (ii, jj) not in vis and grid[ii][jj] == grid[i][j]:
                    q.append((ii, jj))
                    vis.add((ii, jj))
        return vis

    for i in range(m):
        for j in range(n):
            if (i, j) not in seen:
                up = explore(i, j)
                ar = len(up)
                per = 0

                for ci, cj in up:
                    cnt = 0
                    for ii, jj in (ci+1, cj), (ci-1, cj), (ci, cj+1), (ci, cj-1):
                        if (ii, jj) not in up:
                            cnt += 1
                    per += cnt
                seen.update(up)
                tot += ar * per
    print(tot)


def part2(grid):
    grid = [list(x) for x in grid]
    m, n = len(grid), len(grid[0])
    tot = 0
    seen = set()

    def explore(si, sj):
        vis, q = set([(si, sj)]), deque([(si, sj)])

        while q:
            ci, cj = q.popleft()

            for ii, jj in (ci+1, cj), (ci-1, cj), (ci, cj+1), (ci, cj-1):
                if 0 <= ii < m and 0 <= jj < n and (ii, jj) not in vis and grid[ii][jj] == grid[i][j]:
                    q.append((ii, jj))
                    vis.add((ii, jj))
        return vis

    for i in range(m):
        for j in range(n):
            if (i, j) not in seen:
                up = explore(i, j)
                ar = len(up)
                sides = set()

                for ci, cj in up:
                    for di, dj in (1, 0), (-1, 0), (0, -1), (0, 1):
                        ii, jj = ci + di, cj+dj
                        if (ii, jj) not in up:
                            sides.add((ii, jj, di, dj))

                scount = 0
                for x, y, dx, dy in sides:
                    if dx != 0:
                        if (x, y-1, dx, dy) not in sides:
                            scount += 1
                    if dy != 0:
                        if (x-1, y, dx, dy) not in sides:
                            scount += 1
                    
                    
                seen.update(up)
                tot += ar * scount
    print(tot)

            
if __name__ == "__main__":
  s = process()
  part1(s)
  part2(s)