import collections
from collections import deque, defaultdict, Counter
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
    return s

def part1(input):
    l, r = [], []
    for line in input:
        x, y = scanNums(line)
        l.append(x)
        r.append(y)

    l.sort()
    r.sort()
    ans = 0

    for i in range(len(l)):
        ans += abs(l[i]-r[i])
    
    print(ans)

def part2(input):
    l, r = [], []
    for line in input:
        x, y = scanNums(line)
        l.append(x)
        r.append(y)

    r = Counter(r)
    ans = 0

    for i in range(len(l)):
        ans += l[i]*r[l[i]]
    
    print(ans)
            
if __name__ == "__main__":
  s = process()
  part1(s)
  part2(s)