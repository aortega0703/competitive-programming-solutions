# https://www.hackerrank.com/contests/projecteuler/challenges/euler025/
import sys
sys.set_int_max_str_digits(5000)

def fill(N):
    i = 2
    fib = [0, 1]
    great = [0, 1]
    d = 1
    while d < N:
        fib.append(fib[i-1] + fib[i-2])
        if len(str(fib[i])) > d:
            d += 1
            great.append(i)
        i += 1
    return great

max_N = 5000
fib = fill(max_N)
for _ in range(int(input())):
    N = int(input())
    print(fib[N])
