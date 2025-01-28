# https://www.hackerrank.com/challenges/largest-permutation/
L, K = map(int, input().split())
arr = list(map(lambda x: int(x) - 1, input().split()))
inv = arr.copy()
for i, item in enumerate(arr):
    inv[item] = i
count = 0
i = 0
while i < L and count < K:
    if arr[i] != L - i - 1:
        count += 1
        next_index = inv[L - i - 1]
        arr[next_index] = arr[i]
        inv[arr[i]] = next_index
        arr[i] = L - i - 1
        inv[L - i - 1] = arr[i]
    i += 1
print(*map(lambda a: a + 1, arr))
