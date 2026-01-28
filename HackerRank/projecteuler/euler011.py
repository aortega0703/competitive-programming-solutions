#!/bin/python3

def product(l):
    ans = 1
    for i in l:
        ans *= i
    return ans

def split(l, sep):
    ans = [[]]
    for i in l:
        if i == sep:
            ans.append([])
        else:
            ans[-1].append(i)
    return ans

def max_prod(l, N) -> int:
    if len(l) < N:
        return 0
    ans = product(l[:N])
    curr = ans
    for i in range(N, len(l)):
        curr = curr//l[i-N]*l[i]
        if curr > ans:
            ans = curr
    return ans

def transpose(l):
    ans = [[0]*len(l) for _ in range(len(l[0]))]
    for r in range(len(l)):
        for c in range(len(l[r])):
            ans[c][r] = l[r][c]
    return ans

grid = []
for grid_i in range(20):
    grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
    grid.append(grid_t)

ans = 0

# rows
for i in range(len(grid)):
    h = split(grid[i], 0)
    ans = max(ans, max(map(lambda x: max_prod(x, 4), h)))

# diag 1
grid2 = [[0]*(20) for _ in range(20*2-1)]
for i in range(len(grid)):
    for j in range(i, i+20):
        grid2[j][i] = grid[i][j-i]
for i in range(len(grid2)):
    h = split(grid2[i], 0)
    ans = max(ans, max(map(lambda x: max_prod(x, 4), h)))
# diag 2
grid2 = [[0]*(20) for _ in range(20*2-1)]
grid = list(map(lambda x: list(reversed(x)), grid))
for i in range(len(grid)):
    for j in range(i, i+20):
        grid2[j][i] = grid[i][j-i]
for i in range(len(grid2)):
    h = split(grid2[i], 0)
    h = max(map(lambda x: max_prod(x, 4), h))
    ans = max(ans, h)

# columns
grid = transpose(grid)
for i in range(len(grid)):
    h = split(grid[i], 0)
    ans = max(ans, max(map(lambda x: max_prod(x, 4), h)))

print(ans)
