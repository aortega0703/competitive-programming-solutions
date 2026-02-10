# https://www.hackerrank.com/contests/projecteuler/challenges/euler034/
def to_list(N):
    ans = []
    while N > 0:
        N, d = divmod(N, 10)
        ans.append(d)
    return ans

fact = [1] * 10
for n in range(1, len(fact)):
    fact[n] = fact[n-1] * n

digits = 2
bound = 10
N = 10
ans = []
# 999...99 (k digits) |-> 9! * k
# when the image is less than the smallest k digit number (10^(k-1)) we stop
# That's k=7 btw
while fact[9] * digits >= bound:
    if N == sum(map(lambda x: fact[x], to_list(N))):
        ans += [N]
    N += 1
    if N == bound * 10:
        digits += 1
        bound *= 10
print(f"{sum(ans)}: {ans}")
