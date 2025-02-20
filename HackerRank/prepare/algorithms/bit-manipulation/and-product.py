# https://www.hackerrank.com/challenges/and-product/
import math

for _ in range(int(input())):
    l, r = map(int, input().split())
    if r == 0:
        print(0)
        continue
    ans = 1 << (int(math.log2(l ^ r)) + 1)
    ans -= 1
    ans = r & ~ans
    print(ans)
