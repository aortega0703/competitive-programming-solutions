# https://www.hackerrank.com/challenges/the-great-xor/
import math

for _ in range(int(input())):
    n = int(input())
    mask = (1 << int(math.log2(n) + 1)) - 1
    ans = 0
    zeros = ~ n & mask
    while zeros != 0:
        ans += zeros & -zeros
        zeros &= ~ (zeros & -zeros)
    print(ans)
