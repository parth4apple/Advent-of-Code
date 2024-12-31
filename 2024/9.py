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
    queue = deque()
    gaps = deque()
    counter = 0
    result = []
    for i, num in enumerate(input[0]):
        num = int(num)

        if i % 2 == 0:
            for _ in range(num):
                result.append(i // 2)
                queue.append((counter, i // 2))
                counter += 1
        else:
            for _ in range(num):
                gaps.append(counter)
                result.append(None)
                counter += 1

    result = result[:len(queue)]
    while gaps[0] < queue[-1][0]:
        result[gaps[0]] = queue[-1][1]
        queue.pop()
        gaps.popleft()

    tot = sum(i * num for i, num in enumerate(result))
    print(tot)

def part2(input):
    queue = deque()
    gaps = deque()
    counter = 0
    result = []
    for i, num in enumerate(input[0]):
        num = int(num)

        if i % 2 == 0:
            queue.append((counter, num, i // 2))
            for _ in range(num):
                result.append(i // 2)
                counter += 1
        else:
            gaps.append((counter, num))
            for _ in range(num):
                result.append(None)
                counter += 1

    for (counter, size, file) in reversed(queue):
        for i, (gapCounter, gapSize) in enumerate(gaps):
            if gapCounter < counter and size <= gapSize:
                for j in range(size):
                    result[counter+j] = None
                    result[gapCounter+j] = file
                gaps[i] = (gapCounter+size, gapSize-size)
                break
    
    tot = sum(i * num for i, num in enumerate(result) if num is not None)
    print(tot)

    # print(tot)

            
if __name__ == "__main__":
  s = process()
  part1(s)
  part2(s)