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

def part1(input):
    adj = defaultdict(list)
    tot = 0

    ptr = 0
    while input[ptr] != "":
        n1, n2 = input[ptr].split("|")
        n1, n2 = int(n1), int(n2)
        adj[n1].append(n2)

        ptr +=1
    
    ptr += 1
    for i in range(ptr, len(input)):
        seq = [int(x) for x in input[i].split(",")]

        seen = set()
        ok = True
        for num in seq:
            if not ok:
                break
            q = deque([num])
            vis = set([num])
            while len(q):
                # print(q)
                cur = q.popleft()
                if cur in seen:
                    ok = False
                    break
                
                for nei in adj[num]:
                    if nei not in vis:
                        vis.add(nei)
                        q.append(nei)
            
            seen.add(num)
        if ok:
            # print(seq)
            mid = len(seq) // 2
            tot += seq[mid]
    print(tot)


        

def part2(input):
    adj = defaultdict(list)
    adj2 = defaultdict(set)
    tot = 0

    ptr = 0
    while input[ptr] != "":
        n1, n2 = input[ptr].split("|")
        n1, n2 = int(n1), int(n2)
        adj[n1].append(n2)
        adj2[n2].add(n1)

        ptr +=1
    
    ptr += 1
    for i in range(ptr, len(input)):
        seq = [int(x) for x in input[i].split(",")]

        seen = set()
        ok = True
        for num in seq:
            if not ok:
                break
            q = deque([num])
            vis = set([num])
            while len(q):
                cur = q.popleft()
                if cur in seen:
                    ok = False
                    break
                
                for nei in adj[num]:
                    if nei not in vis:
                        vis.add(nei)
                        q.append(nei)
            
            seen.add(num)
        if not ok:
            seqs = set(seq)

            ordering = []
            ind = {item: len(set(adj[item]) & seqs) for i, item in enumerate(seq)}
            q = deque()
            vis = set()
            for item in seqs:
                if ind[item] == 0:
                    q.append(item)
            
            while q:
                cur = q.popleft()
                ordering.append(cur)

                for nei in adj2[cur]:
                    if nei in seqs:
                        ind[nei] -= 1
                        if ind[nei] == 0:
                            q.append(nei)

            tot += ordering[len(ordering) // 2]
            
            
    print(tot)
            
if __name__ == "__main__":
  s = process()
  part1(s)
  part2(s)