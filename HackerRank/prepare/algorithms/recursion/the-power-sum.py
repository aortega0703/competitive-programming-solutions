# https://www.hackerrank.com/challenges/the-power-sum/

def make_roots(n, p):
    roots = set()
    i = 1
    while i ** p <= n:
        roots.add(i ** p)
        i += 1
    return roots

def make_ans(n, p, start, roots):
    i = start
    ans = n in roots
    while 2 * (i**p) < n:
        remainder = n - i**p
        ans += make_ans(remainder, p, i + 1, roots)
        i += 1
    return ans

n = int(input())
p = int(input())
roots = make_roots(n, p)
ans = make_ans(n, p, 1, roots)
print(ans)
