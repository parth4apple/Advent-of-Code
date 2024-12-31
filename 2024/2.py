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

def isSafe(nums):
    if sorted(nums) != nums and sorted(nums, reverse=True) != nums:
        return False
    
    safe = True 

    for i in range(1, len(nums)):
        diff = abs(nums[i]-nums[i-1])
        if diff > 3 or diff == 0:
            safe = False

    return safe

def part1(input):
    ans = 0
    for line in input:
        nums = scanNums(line)
        ans += isSafe(nums)

    print(ans)

def part2(input):
    ans = 0
    for line in input:
        nums = scanNums(line)
        safe = isSafe(nums)
        for i in range(len(nums)):
            pruned = nums[:i] + nums[i+1:]
            safe = safe or isSafe(pruned)
        ans += safe

    print(ans)
            
if __name__ == "__main__":
  s = process()
  part1(s)
  part2(s)