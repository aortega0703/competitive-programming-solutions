# https://www.hackerrank.com/challenges/grid-challenge/
def transpose(grid):
    ans = ["" for _ in range(len(grid[0]))]
    for item in grid:
        for i, char in enumerate(item):
            ans[i] += char
    return ans

for _ in range(int(input())):
    n = int(input())
    grid = []
    for _ in range(n):
        grid.append(input())
    grid = ["".join(sorted(item)) for item in grid]
    grid_t = transpose(grid)
    ans = all(item == "".join(sorted(item)) for item in grid_t)
    print("YES" if ans else "NO")
