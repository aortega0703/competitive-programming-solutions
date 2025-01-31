#https://www.hackerrank.com/challenges/angry-children/
n = int(input())
k = int(input()) - 1
arr = []
for _ in range(n):
    arr.append(int(input()))
arr = sorted(arr)
ans = arr[-1]
for i in range(n - k):
    ans = min(ans, arr[i + k] - arr[i])
print(ans)
