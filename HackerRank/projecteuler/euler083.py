# www.hackerrank.com/contests/projecteuler/challenges/euler083/
# Graph traversal, solved with Dijkstra's algorithm O(N^2 log(N))

import math
from queue import PriorityQueue
N = int(input())
M = [list(map(int, input().split())) for _ in range(N)]
ans = [[math.inf for _ in range(N)] for _ in range(N)]

queue = PriorityQueue()
queue.put((M[0][0], 0, 0))
while queue.qsize() > 0:
    new_dist, row, col = queue.get()
    if ans[row][col] <= new_dist:
        continue
    ans[row][col] = new_dist
    if row == N-1 and col == N-1:
        break
    if row - 1 >= 0:
        queue.put((new_dist + M[row - 1][col], row - 1, col))
    if row + 1 < N:
        queue.put((new_dist + M[row + 1][col], row + 1, col))
    if col - 1 >= 0:
        queue.put((new_dist + M[row][col - 1], row, col - 1))
    if col + 1 < N:
        queue.put((new_dist + M[row][col + 1], row, col + 1))
print(ans[N-1][N-1])    
