import collections
from collections import deque, defaultdict
import sys
from functools import lru_cache, cache, cmp_to_key
from itertools import zip_longest, product
import heapq
import math
import re
import sys
import numpy as np
from math import fmod, lcm, log
from utils import *
sys.setrecursionlimit(100000)


def process():
    s = []
    for line in sys.stdin:
        s.append(line.strip())
    return s


def part1(input, addOffset=False):
    ptr = 0
    tot = 0
    while ptr < len(input):
        _, A = input[ptr].split(": ")
        _, B = input[ptr+1].split(": ")
        _, P = input[ptr+2].split(": ")
        Ax, Ay = A.split(", ")
        Bx, By = B.split(", ")
        Px, Py = P.split(", ")
        Ax, Ay = int(Ax[2:]), int(Ay[2:])
        Bx, By = int(Bx[2:]), int(By[2:])
        Px, Py = int(Px[2:]), int(Py[2:])
        if addOffset:
            Px, Py = Px + 10000000000000, Py + 10000000000000

        ptr += 4
        a = np.array([[Ax, Bx], [Ay, By]])
        b = np.array([Px, Py])
        x = None
        try:
            x = np.linalg.solve(a, b)
        except:
            pass
        if x is not None and abs(round(x[0]) - x[0]) < 10**(-3) and abs(round(x[1]) - x[1]) < 10**(-3):
            tot += (x[0]*3+x[1])
    
    print(int(tot))

def part2(input):
    part1(input, True)
            
if __name__ == "__main__":
  s = process()
  part1(s)
  part2(s)