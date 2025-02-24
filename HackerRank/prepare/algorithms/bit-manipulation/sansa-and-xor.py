# https://www.hackerrank.com/challenges/sansa-and-xor/

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    repeats = [0 for _ in arr]
    repeats[0] = repeats[-1] = n
    for i in range(1, n // 2 + 1):
        repeats[i] = repeats[i - 1] + n - 2 * i
        repeats[n - i - 1] = repeats[i]
    ans = 0
    for i in range(n):
        if repeats[i] % 2 != 0:
            ans ^= arr[i]
    print(ans)
