import math
T = int(input())
N = [int(input()) for _ in range(T)]
max_N = max(N)

def sieve(max_N):
    primes = []
    is_prime = [True for _ in range(max_N + 1)]
    is_prime[0] = is_prime[1] = False
    n = 2
    while n * n <= max_N:
        if not is_prime[n]:
            n += 1
            continue
        primes.append(n)
        kn = 2 * n
        while kn <= max_N:
            is_prime[kn] = False
            kn += n
        n += 1
    while n <= max_N:
        if is_prime[n]:
            primes.append(n)
        n += 1
    return primes

primes = sieve(max_N)
def conv(primes, n):
    def add(f, g):
        return list(map(sum, zip(f, g)))
    p_i = 1
    f = [int(k % 2 == 0) for k in range(n + 1)]
    while p_i < len(primes) and primes[p_i] <= n:
        p = primes[p_i]
        print(p_i, p)
        g = [int(k > 1 and k % p == 0) for k in range(n+1)]
        f = [f[x] + sum(g[t] * f[x - t] for t in range(p, x + 1))
                for x in range(n + 1)]
        p_i += 1

    return f
    
ans = conv(primes, max_N)
for n in N:
    print(ans[n])
