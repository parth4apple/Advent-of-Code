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

def blink(arr):
    res = []

    for num in arr:
        if num == 0:
            res.append(1)
        elif len(str(num)) % 2 == 0:
            st, n = str(num), len(str(num))
            
            res.append(int(st[:n//2]))
            res.append(int(st[n//2:]))
        else:
            res.append(num * 2024)
    
    return res

@cache
def dp(num, i):
    if i == 0:
        return 1

    if num == 0:
        return dp(1, i-1)
    elif len(str(num)) % 2 == 0:
        st, n = str(num), len(str(num))
        
        return dp(int(st[:n//2]), i-1) + dp(int(st[n//2:]), i-1)
    else:
        return dp(num * 2024, i-1)   

def part1(input):
    nums = [int(x) for x in input[0].split(" ")]

    for i in range(25):
        nums = [x for x in blink(nums)]
    print(len(nums))

        

def part2(input):
    tot = 0
    nums = [int(x) for x in input[0].split(" ")]

    for num in nums:
        tot += dp(num, 75)

    print(tot)
    
            
if __name__ == "__main__":
  s = process()
  part1(s)
  part2(s)