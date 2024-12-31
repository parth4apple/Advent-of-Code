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
    return s

MOD = 16777216

@cache
def getNext(num):
    num = (num ^ (num*64)) % MOD
    num = (num ^ (num//32)) % MOD
    num = (num ^ (num * 2048)) % MOD
    return num

def part1(input):
    ans = 0
    for i, num in enumerate(input):
        num = int(num)
        for _ in range(2000):
            num = getNext(num)
        ans += num

    print(ans)

def part2(input):
    ans = 0
    totals = defaultdict(int)
    for i, num in enumerate(input):
        num = int(num)
        prices = [int(str(num)[-1])]
        for _ in range(2000):
            num = getNext(num)
            prices.append(int(str(num)[-1]))

        changes = [prices[i]-prices[i-1] for i in range(1, len(prices))]
        seen = set()
        for i in range(len(changes)-4):
            state = tuple(changes[i:i+4])
            if state not in seen:
                totals[state] += prices[i+4]
            seen.add(state)
            
        ans += num

    maxVal = None
    for key, val in totals.items():
        if maxVal is None or val > maxVal:
            maxVal = val
    print(maxVal)
            
if __name__ == "__main__":
  s = process()
  part1(s)
  part2(s)