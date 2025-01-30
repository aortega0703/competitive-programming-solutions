# https://www.hackerrank.com/challenges/greedy-florist/
n, k = map(int, input().split())
arr = sorted(list(map(int, input().split())), reverse = True)
ans = 0
for i, item in enumerate(arr):
    ans += item * (i // k + 1)
print(ans)
