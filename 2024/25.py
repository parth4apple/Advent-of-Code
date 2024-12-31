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
    s = ""
    for line in sys.stdin:
        s += line

    blocks = s.split("\n\n")
    locks = []
    keys = []
    for block in blocks:
        sp = block.split("\n")
        # is lock
        if "." not in sp[0]:
            locks.append([list(x) for x in sp])
        else:
            keys.append([list(x) for x in sp])

    return locks, keys

def part1(obj):
    locks, keys = obj
    m, n = len(locks[0]), len(locks[0][0])
    
    ans = 0
    for lock in locks:
        for key in keys:
            good = True
            for i in range(m):
                for j in range(n):
                    if lock[i][j] == "#" and key[i][j] == "#":
                        good = False
        
            if good:
                ans += 1
    print(ans)


def part2(input):
    pass
            
if __name__ == "__main__":
  s = process()
  part1(s)
  part2(s)