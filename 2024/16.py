import collections
from collections import deque, defaultdict
import sys
from functools import lru_cache, cache, cmp_to_key
from itertools import zip_longest, product
import heapq
import math
import re
import sys
sys.setrecursionlimit(100000)
from utils import *

def process():
    s = []
    for line in sys.stdin:
        s.append(line.strip())
    return s

def part1(input, part2=False):
    grid = [list(x) for x in input]

    m, n = len(grid), len(grid[0])
    sx, sy = None, None

    d = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == "S":
                sx, sy = i, j

    pq = [(0, sx, sy, 1)]

    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    best = defaultdict(lambda: 10**20)
    prev = defaultdict(list)

    t1 = set()
    vis = set()
    def populate(x, y, d):
        if (x, y, d) in t1:
            return
        vis.add((x, y))
        t1.add((x, y, d))

        for nx, ny, nd in prev[(x, y, d)]:
            populate(nx, ny, nd)

    while pq:
        w, x, y, d = heapq.heappop(pq)

        if best[(x, y, d)] < w:
            continue
        best[(x, y, d)] = w

        if grid[x][y] == "E":
            if part2:
                populate(x, y, d)
            else:
                print(w)
            break

        for off in range(4):
            nw = w + (off % 2)*1000+1
            nd = (d+off) % 4
            ndx, ndy = dirs[nd]
            nx, ny = x+ndx, y+ndy
            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] in ".E":
                if best[(nx, ny, nd)] > nw:
                    heapq.heappush(pq, (nw, nx, ny, nd))
                    prev[(nx, ny, nd)] = [(x, y, d)]
                    best[(nx, ny, nd)] = nw
                elif best[(nx, ny, nd)] == nw:
                    heapq.heappush(pq, (nw, nx, ny, nd))
                    prev[(nx, ny, nd)].append((x, y, d))

    if part2:
        print(len(vis))
            
def part2(input):
    part1(input, True)
            
if __name__ == "__main__":
  s = process()
  part1(s)
  part2(s)