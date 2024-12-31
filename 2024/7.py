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

def possible(target, nums):
    @cache
    def go(idx, tot):
        if tot == target:
            return True

        pos = False
        if idx < len(nums)-1:
            pos = pos or go(idx+1, tot*nums[idx+1])
            pos = pos or go(idx+1, tot+nums[idx+1])

        return pos

    return go(0, nums[0])

def possible2(target, nums):
    @cache
    def go(idx, tot):
        if tot == target and idx == len(nums)-1:
            return True

        pos = False

        if idx < len(nums)-1:
            pos = pos or go(idx+1, int(str(tot) + str(nums[idx+1])))
        
            pos = pos or go(idx+1, tot*nums[idx+1])
            pos = pos or go(idx+1, tot+nums[idx+1])

        return pos

    return go(0, nums[0])
        

def part1(input):
    tot = 0
    for line in input:
        target, rest = line.split(":")
        target = int(target)
        nums = [int(x) for x in rest.strip().split()]
        tot += target * possible(target, nums)
        
    print(tot)


def part2(input):
    tot = 0
    for line in input:
        target, rest = line.split(":")
        target = int(target)
        nums = [int(x) for x in rest.strip().split()]
        tot += target * possible2(target, nums)
        
    print(tot)
            
if __name__ == "__main__":
  s = process()
  part1(s)
  part2(s)