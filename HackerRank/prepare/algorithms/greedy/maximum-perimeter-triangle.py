# https://www.hackerrank.com/challenges/maximum-perimeter-triangle/
n = int(input())
arr = sorted(list(map(int, input().split())), reverse=True)
ans = [-1]
for i in range(len(arr) - 2):
    if arr[i] < arr[i + 1] + arr[i + 2]:
        ans = reversed(arr[i : i + 3])
        break
print(*ans)
