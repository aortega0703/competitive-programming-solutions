# https://www.hackerrank.com/challenges/maximizing-xor/

import math

l = int(input())
r = int(input())
print((1 << int(math.log2(l ^ r)) + 1) - 1)
