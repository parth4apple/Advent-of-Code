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
        s.append(line.strip())

    return [list(x) for x in s]

def part1(grid, part2=False):
    m, n = len(grid), len(grid[0])
    grid = [[grid[i][j] for j in range(n)] for i in range(m)]

    sx = sy = ex = ey = None
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "S":
                sx, sy = i, j
                grid[i][j] = "."
            elif grid[i][j] == "E":
                ex, ey = i, j
                grid[i][j] = "."

    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    # mark best distance from tx, ty to every cell that is "."
    def mark(tx, ty):
        dist = defaultdict(lambda: 10**20)
        dist[(tx, ty)] = 0
        queue = deque([(tx, ty)])
        time = 0
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()

                for dx, dy in dirs:
                    xx, yy = x+dx, y+dy
                    if 0 <= xx < m and 0 <= yy < n and (xx, yy) not in dist and grid[xx][yy] == ".":
                        queue.append((xx, yy))
                        dist[(xx, yy)] = time + 1
            time += 1   

        return dist
    
    startDist = mark(sx, sy)
    endDist = mark(ex, ey)
    best = startDist[(ex, ey)]

    queue = deque([(sx, sy)])
    seen = set()
    good = set()
    time = 0
    while queue:
        for _ in range(len(queue)):
            obj = queue.popleft()
            x, y = obj

            for dx, dy in dirs:
                xx, yy = x+dx, y+dy
                if not (0 <= xx < m and 0 <= yy < n):
                    continue

                if grid[xx][yy] == "." and (xx, yy) not in seen:
                    queue.append((xx, yy))
                    seen.add((xx, yy))
                    continue

                for ndx, ndy in dirs:
                    nxx, nyy = xx+ndx, yy+ndy
                    if 0 <= nxx < m and 0 <= nyy < n and (nxx, nyy) != (x, y) and grid[nxx][nyy] == ".":
                        endCost = time + endDist[(nxx, nyy)] + 1 # cheat cost = time already taken + time to end +1
                        if best - endCost >= 100:
                            good.add((x, y, nxx, nyy))
        time += 1

    if not part2:
        print(len(good))
    else:
        ans = 0
        for x, y in startDist.keys():
            for xx, yy in endDist.keys():
                dist = abs(x-xx)+abs(y-yy)
                if dist <= 20:
                    if startDist[(x, y)] + endDist[(xx, yy)] + dist <= best - 100:
                        ans += 1
        print(ans)


def part2(grid):
    part1(grid, True)
            
if __name__ == "__main__":
  s = process()
  part1(s)
  part2(s)