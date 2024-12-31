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
import random
sys.setrecursionlimit(100000)

def process():
    s = []
    for line in sys.stdin:
        s.append(line.strip())
    adj = defaultdict(set)
    for line in s:
        x, y = line.split("-")
        adj[x].add(y)
        adj[y].add(x)

    return adj

def part1(adj):
    seen = set()
    for key in adj:
        if key[0] != "t":
            continue
        
        ls = list(adj[key])
        for i in range(len(ls)):
            for j in range(1, len(ls)):
                if ls[i] not in adj[ls[j]]:
                    continue
                cur = sorted([ls[i], ls[j], key])
                if len(set(cur)) == 3:
                    seen.add(tuple(cur))

    print(len(seen))
    
def part2(adj):
    keys = list(adj.keys())

    best = None
    for _ in range(5000):
        random.shuffle(keys)
        clique = []
        for x in keys:
            good = True
            for n in clique:
                if n not in adj[x]:
                    good = False
            
            if good:
                clique.append(x)
        
        if best is None or len(clique) > len(best):
            best = clique

    print(",".join(sorted(best)))

        

            
if __name__ == "__main__":
  s = process()
  part1(s)
  part2(s)