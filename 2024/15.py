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
    s = ""
    for line in sys.stdin:
        s += line
    return s

def part1(input):
    part2(input, True)
    # grid, moves = input.split("\n\n")
    # grid = [list(x) for x in grid.split("\n")]
    # moves = "".join([x.strip() for x in moves])

    # m, n = len(grid), len(grid[0])
    # sx, sy = None, None
    # for i in range(m):
    #     for j in range(n):
    #         if grid[i][j] == "@":
    #             sx, sy = i, j

    # dirs = {"^": (-1, 0), "v": (1, 0), ">": (0, 1), "<": (0, -1)}

    # for move in moves:
    #     dx, dy = dirs[move]
    #     cx, cy = sx + dx, sy + dy

    #     if grid[cx][cy] == ".":
    #         grid[cx][cy], grid[sx][sy] = grid[sx][sy], grid[cx][cy]
    #         sx, sy = cx, cy
    #     elif grid[cx][cy] != "#":
    #         space = False
    #         while 0 <= cx < m and 0 <= cy < n:
    #             cx, cy = cx + dx, cy + dy

    #             if grid[cx][cy] == ".":
    #                 space = True
    #                 break
    #             elif grid[cx][cy] == "#":
    #                 break
    #         if space:
    #             grid[cx][cy], grid[sx+dx][sy+dy] = grid[sx+dx][sy+dy], grid[cx][cy]
    #             grid[sx][sy], grid[sx+dx][sy+dy] = grid[sx+dx][sy+dy], grid[sx][sy]
    #             sx, sy = sx+dx, sy+dy

    # tot = 0
    # for i in range(m):
    #     for j in range(n):
    #         if grid[i][j] == "O":
    #             tot += i*100+j
    # print(tot)
            

def part2(input, part1):
    grid, moves = input.split("\n\n")
    grid = [list(x) for x in grid.split("\n")]
    moves = "".join([x.strip() for x in moves])
    m, n = len(grid), len(grid[0])
    
    if not part1:
        ng = [[None] * (n*2) for _ in range((m))]
        mp = {"#": "##", "O": "[]", ".": "..", "@": "@."}
        for i in range(m):
            for j in range(n):
                c1, c2 = list(mp[grid[i][j]])
                ng[i][2*j], ng[i][2*j+1] = c1, c2
        n *= 2
        grid = ng

    sx, sy = None, None
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "@":
                sx, sy = i, j

    dirs = {"^": (-1, 0), "v": (1, 0), ">": (0, 1), "<": (0, -1)}
    for move in moves:
        dx, dy = dirs[move]
        toMove = [(sx, sy)]
        seen = set()
        def add(x, y):
            if (x, y) in seen:
                return
            seen.add((x, y))
            toMove.append((x, y))

        i = 0
        good = True
        while i < len(toMove):
            x, y = toMove[i]
            nx, ny = x+dx, y+dy
            if grid[nx][ny] == "#":
                good = False
                break
            elif grid[nx][ny] in "O[]":
                if (nx, ny) not in toMove:
                    add(nx, ny)
                if grid[nx][ny] == "[":
                    add(nx, ny+1)
                elif grid[nx][ny] == "]":
                    add(nx, ny-1)
            
            i += 1
        if not good:
            continue
        grid2 = [[grid[i][j] for j in range(n)] for i in range(m)]
        for x, y in toMove:
            grid2[x][y] = "."

        for x, y in toMove:
            grid2[x+dx][y+dy] = grid[x][y]
        grid = grid2
        sx, sy = sx+dx, sy+dy

    tot = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] in "[O":
                tot += i*100+j
    print(tot)

            
if __name__ == "__main__":
  s = process()
  part1(s)
  part2(s, False)