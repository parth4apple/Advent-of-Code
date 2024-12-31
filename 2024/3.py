import collections
import sys
from functools import lru_cache, cache, cmp_to_key
from itertools import zip_longest, product
import heapq
import math
import re
from utils import *

def parseMul(s, idx):
  if s[idx] != "(":
    return 0
  idx += 1
  
  if not s[idx].isdigit():
    return 0

  num1 = int(s[idx])
  idx += 1
  
  for i in range(2):
    if s[idx].isdigit():
      num1 *= 10
      num1 += int(s[idx])
      idx += 1
  
  if s[idx] != ",":
    return 0
  idx += 1
  
  if not s[idx].isdigit():
    return 0
  
  num2 = int(s[idx])
  idx += 1
  
  for i in range(2):
    if s[idx].isdigit():
      num2 *= 10
      num2 += int(s[idx])
      idx += 1
      
  if s[idx] != ")":
    return 0
  idx +=1
  return num1*num2
  

def process():
  s = []
  for line in sys.stdin:
      s += list(line)
  return s
      
def part1(s):
  tot = 0
  
  for i in range(0, len(s)):
    if "".join(s[i:i+3]) == "mul":
      tot += parseMul(s, i+3)
  print(tot)


def part2(s):
  tot = 0
  skip = False
  for i in range(0, len(s)):
    if "".join(s[i:i+4]) == "do()":
      skip = False
    elif "".join(s[i:i+7]) == "don't()":
      skip = True
    elif "".join(s[i:i+3]) == "mul":
      if skip:
        continue
      tot += parseMul(s, i+3)
  print(tot)



if __name__ == "__main__":
  s = process()
  part1(s)
  part2(s)