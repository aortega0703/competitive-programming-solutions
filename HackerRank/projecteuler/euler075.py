# https://www.hackerrank.com/contests/projecteuler/challenges/euler075
# This solutions finds all primitive pythagorean triples (O(N log N)) and marks
# all their multiples similarly to an Eratosthenes Sieve.

# Euclidean Algorithm for gcd. O(log(b))
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
    
T = int(input())
N = [int(input()) for _ in range(T)]
max_N = max(N)
triples_count = [0 for _ in range(max_N + 1)]
m = 2
# For any m > n > 0 and 
# a = m * m - n * n
# b = 2 * m * n
# c = m * m + n * n
# (a, b, c) is a Pythagorean triple, then
# a + b + c = 2m^2 + 2mn <= max_N
# This gives an upper bound on m, m = O(sqrt(N))
while 2 * (m*m + m) <= max_N:
    # (m, n) produce a primitive triple iff only one of them is even
    # n = O(m) = O(sqrt(N))
    for n in reversed(range(m - 1, 0, -2)):
        if 2 * (m * m + m * n) > max_N:
            break
        # and they are coprime. O(log N)
        if gcd(m, n) == 1:
            # this equals a + b + c
            d = 2 * m * (m + n)
            kd = d
            # count all multiples of the triple (by side sum)
            # d's are greater than the sequence of primes (?). So this
            # does N/2 + N/3 + N/5 + ... = O(log log N) operations (?)
            while kd <= max_N:
                triples_count[kd] += 1
                kd += d
    m += 1
# Compute the acumulated count of indices with tiples_count = 1. #O(N)
acum = [0 for _ in range(max_N + 1)]
for index, count in enumerate(triples_count[1:], 1):
    acum[index] = acum[index - 1]
    # print(index, count)
    if count == 1:
        print(index, sep=" ")
        acum[index] += 1
for n in N:
    print(acum[n])
