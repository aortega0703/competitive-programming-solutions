import math
from collections import deque

N = int(input())
M = [list(map(int, input().split())) for _ in range(N)]
ans = [[math.inf for _ in range(N)] for _ in range(N)]
ans[N-1][N-1] = M[N-1][N-1]

def ans_get(row, col):
    if row >= N or col >= N:
        return math.inf
    return ans[row][col]
    
queue = deque([])
row, col = N-1, N-1
if row > 0:
    queue.append((row - 1, col))
if col > 0:
    queue.append((row, col - 1))
while len(queue) > 0:
    (row, col) = queue.popleft()
    if ans[row][col] != math.inf:
        continue
    down = ans_get(row + 1, col)
    right = ans_get(row, col + 1)
    ans[row][col] = M[row][col] + min(down, right)
    if row > 0:
        queue.append((row - 1, col))
    if col > 0:
        queue.append((row, col - 1))
print(ans[0][0])
