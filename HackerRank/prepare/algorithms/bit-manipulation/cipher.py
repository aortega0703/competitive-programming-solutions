# https://www.hackerrank.com/challenges/cipher/

def get(arr, i):
    if i < 0:
        return 0
    return arr[i]

n, k = map(int, input().split())
k -= 1
msg = list(map(int, list(input())))

column = False
ans = []
for i in range(len(msg) - k):
    bit = int(msg[i] != column)
    column = not column if get(ans, i - k) != bit else column
    ans.append(bit)
print(*ans, sep="")
