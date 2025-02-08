# https://www.hackerrank.com/challenges/beautiful-pairs/
n = int(input())
available = {}
for item in map(int, input().split()):
    if item not in available:
        available[item] = 1
    else:
        available[item] += 1
ans = 0
for item in map(int, input().split()):
    if item not in available:
        continue
    ans += 1
    available[item] -= 1
    if available[item] == 0:
        available.pop(item)
if ans == n:
    print(ans - 1)
else:
    print(ans + 1)
