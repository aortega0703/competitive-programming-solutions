# https://www.hackerrank.com/challenges/luck-balance/
n, k = map(int, input().split())
arr = []
ans = 0
for _ in range(n):
    luck, important = map(int, input().split())
    if important == 0:
        ans += luck
    else:
        arr.append(luck)
arr = sorted(arr, reverse=True)
for i in range(len(arr)):
    if i < k:
        ans += arr[i]
    else:
        ans -= arr[i]
print(ans)
