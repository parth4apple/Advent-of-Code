import collections
from collections import deque, defaultdict
import sys
from functools import lru_cache, cache, cmp_to_key
from itertools import zip_longest, product
import heapq
import math
import re
import sys
import random
from utils import *
sys.setrecursionlimit(100000)


CUTOFF = 10*20

def process():
    s = ""
    for line in sys.stdin:
        s += line

    starts, ops = s.split("\n\n")
    ops = ops.split("\n")
    starts = starts.split("\n")
    return starts, ops

def simulate(starts, sequence, d=None):
    if d is None:
        d = defaultdict(int)
        for gate in starts:
            name, val = gate.split(": ")
            if int(name[1:])> CUTOFF:
                continue 
            d[name] = int(val)

    queue = deque()
    seen = set()
    for i, (_, g1, g2, _) in enumerate(sequence):
        if g1 in d and g2 in d:
            queue.append(sequence[i])
            seen.add(i)

    # print("---------starting-------")
    # for item in sorted(queue, key=lambda x: x[1][1:] ):
    #     print(item)
    while queue:
        inst, g1, g2, g3 = queue.popleft()
        
        if inst == "AND":
            d[g3] = d[g1] and d[g2]
        elif inst == "XOR":
            d[g3] = d[g1] ^ d[g2]
        elif inst == "OR":
            d[g3] = d[g1] or d[g2]

        for i, (_, g1, g2, g3) in enumerate(sequence):
            if i not in seen and g1 in d and g2 in d:
                # print("adding", sequence[i])
                queue.append(sequence[i])
                seen.add(i)

    pairs = []
    for name, val in d.items():
        if name[0] == "z":
            pairs.append((int(name[1:]), int(val)))
    pairs.sort(reverse=True)
    # print(pairs)
    res = "".join([str(x) for _, x in pairs])
    # print(res)
    return res

def part1(obj):
    starts, ops = obj

    sequence = []
    for op in ops:
        if "AND" in op:
            g1, rest = op.split(" AND ")
            g2, g3 = rest.split(" -> ")
            sequence.append(("AND", g1, g2, g3))
        elif "XOR" in op:
            g1, rest = op.split(" XOR ")
            g2, g3 = rest.split(" -> ")
            sequence.append(("XOR", g1, g2, g3))
        elif "OR" in op:
            g1, rest = op.split(" OR ")
            g2, g3 = rest.split(" -> ")
            sequence.append(("OR", g1, g2, g3))

    p1 = int(simulate(starts, sequence), 2)
    print(p1)


def part2(obj):
    starts, ops = obj

    d = defaultdict(int)
    for gate in starts:
        name, val = gate.split(": ")
        if int(name[1:]) > CUTOFF:
            continue 
        d[name] = int(val)
    pairs = []
    for name, val in d.items():
        if name[0] == "x":
            pairs.append((int(name[1:]), int(val)))
    pairs.sort(reverse=True)
    xval = int("".join([str(x) for _, x in pairs]), 2)

    pairs = []
    for name, val in d.items():
        if name[0] == "y":
            pairs.append((int(name[1:]), int(val)))
    pairs.sort(reverse=True)
    yval = int("".join([str(x) for _, x in pairs]), 2)

    # print("x:", xval, ", y:", yval, ", x+y:", xval+yval)
    sequence = []
    for op in ops:
        if "AND" in op:
            g1, rest = op.split(" AND ")
            g2, g3 = rest.split(" -> ")
            if g1 > g2:
                g1, g2 = g2, g1
            sequence.append(("AND", g1, g2, g3))
        elif "XOR" in op:
            g1, rest = op.split(" XOR ")
            g2, g3 = rest.split(" -> ")
            if g1 > g2:
                g1, g2 = g2, g1
            sequence.append(("XOR", g1, g2, g3))
        elif "OR" in op:
            g1, rest = op.split(" OR ")
            g2, g3 = rest.split(" -> ")
            if g1 > g2:
                g1, g2 = g2, g1
            sequence.append(("OR", g1, g2, g3))

    # p2 = int(simulate(starts, sequence), 2)
    # print("actual", p2)


    # simulate with random values
    # for _ in range(100):
    #     x = random.getrandbits(45)
    #     y = random.getrandbits(45)
    #     starts = []
    #     bx, by = bin(x)[2:].zfill(45), bin(y)[2:].zfill(45)
    #     d = defaultdict(int)
    #     for i, val in enumerate(reversed(bx)):
    #         d[f"x{i:02d}"] = int(val)
    #     for i, val in enumerate(reversed(by)):
    #         d[f"y{i:02d}"] = int(val)

    #     tot = int(simulate(starts, sequence, d), 2)
    #     if tot != x+y:
    #         print(x, y, tot)
    #         print("ERRPRROOROROROOR")
    #         # break
        
    """
    switched 
    vvf <> z19

    fgn <> dck 

    nvh <> z37

    z12 <> qdg
    """

    switched = [("vvf", "z19"), ("fgn", "dck"), ("nvh", "z37"), ("z12", "qdg")]

    joined = []
    for x, y in switched:
        joined.append(x)
        joined.append(y)
    
    p2 = ",".join(sorted(joined))
    print(p2)



            
if __name__ == "__main__":
  s = process()
  part1(s)
  part2(s)