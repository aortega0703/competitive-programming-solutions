# https://www.hackerrank.com/challenges/sum-vs-xor/
def make_ans(n):
    if n == 0:
        return 1
    count = 0
    length = math.floor(math.log2(n)) + 1
    while n > 0:
        count += 1
        n &= ~(n & -n)
    return 2**(length - count)

import math
n = int(input())
print(make_ans(n))
