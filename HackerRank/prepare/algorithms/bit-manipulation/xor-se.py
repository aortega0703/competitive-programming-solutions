# https://www.hackerrank.com/challenges/xor-se/

import math

def count_bits(n, b):
    q = n // (b * 2)
    r = n % (b * 2)
    return b * q + max(0, r - b + 1)

for _ in range(int(input())):
    l, r = map(int, input().split())
    ans = 0
    add = (r - l) % 2 == 0
    add = add * 2 - 1
    l -= 1
    countr = (r % 2) * count_bits(r, 1)
    countl = (l % 2) * count_bits(l, 1)
    count = countr + add * countl
    ans += count % 2
    i = 2
    while i <= r:
        countr = count_bits(r // 2, i // 2)
        countl = count_bits(l // 2, i // 2)
        count = countr + add * countl
        ans += i * (count % 2)
        i *= 2
    print(ans)
