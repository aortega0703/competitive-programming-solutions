#https://www.hackerrank.com/challenges/counter-game/
import math

for _ in range(int(input())):
    n = int(input())
    richard = True
    while n != 1:
        power = 1 << int(math.log2(n))
        if power == n:
            n >>= 1
        else:
            n -= power
        richard = not richard
    print("Richard" if richard else "Louise")
