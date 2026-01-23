import math

def prime_sieve(upper_bound):
    primes = []
    is_prime = [True for _ in range(upper_bound)]
    is_prime[0] = is_prime[1] = False
    for n in range(upper_bound):
        if not is_prime[n]:
            continue
        primes.append(n)
        for kn in range(2*n, upper_bound, n):
            is_prime[kn] = False
    return primes

T = int(input())
N = [int(input()) for _ in range(T)]
max_N = max(N)
primes = prime_sieve(math.floor(math.sqrt(max_N)) + 1)
primes2 = []
primes3 = []
primes4 = []
for p in primes:
    if p * p > max_N:
        break
    primes2.append(p * p)
    if p * p * p > max_N:
        continue
    primes3.append(p * p * p)
    if p * p * p * p > max_N:
        continue
    primes4.append(p * p * p * p)

ans = [0 for _ in range(max_N + 1)]
for p2 in primes2:
    for p3 in primes3:
        if p2 + p3 > max_N:
            break
        for p4 in primes4:
            if p2 + p3 + p4 > max_N:
                break
            ans[p2 + p3 + p4] += 1

for n in range(28, max_N + 1):
    ans[n] = ans[n-1] + int(ans[n] != 0)

for n in N:
    print(ans[n])    
