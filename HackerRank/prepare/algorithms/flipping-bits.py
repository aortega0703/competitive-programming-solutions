# https://www.hackerrank.com/challenges/flipping-bits/
for _ in range(int(input())):
    n = ~int(input())
    n &= (1 << 32) - 1
    print(n)
