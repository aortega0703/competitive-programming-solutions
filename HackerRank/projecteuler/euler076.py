T = int(input())
N = [int(input()) for _ in range(T)]
max_N = max(N) + 1
ans = [0 for _ in range(max_N)]
ans[0] = 1
for n in range(1, max_N):
    for i in range(n, max_N):
        ans[i] = (ans[i] + ans[i - n]) % (10**9 + 7)
for n in N:
    print(ans[n] - 1)
