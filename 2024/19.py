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

    s, e = s.split("\n\n")
    
    return s.split(", "), e.split("\n")

def part1(input):
    chunks, words = input

    @cache
    def possible(idx, word):
        if idx == len(word):
            return 1
        
        res = 0
        for chunk in chunks:
            if word[idx:].startswith(chunk):
                res += possible(idx+len(chunk), word)

        return res

    ans = 0
    for word in words:
        ans += possible(0, word)
        possible.cache_clear()
    print(ans)




def part2(input):
    chunks, words = input

            
if __name__ == "__main__":
  s = process()
  part1(s)
  part2(s)