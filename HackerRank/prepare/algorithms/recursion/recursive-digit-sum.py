# https://www.hackerrank.com/challenges/recursive-digit-sum/

n, k = map(int, input().split())
ans = ((n % 9) * k) % 9
print(ans if ans != 0 else 9)
