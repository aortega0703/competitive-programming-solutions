# https://www.hackerrank.com/challenges/jim-and-the-orders/
arr = []
for i in range(int(input())):
    order, prep = map(int, input().split())
    arr.append((i + 1, order + prep))
arr.sort(key=lambda i: i[0])
arr.sort(key=lambda i: i[1])
print(*map(lambda i: i[0], arr))
