# www.hackerrank.com/contests/projecteuler/challenges/euler082/
# Dynamic Programming problem O(N^2)
import math
N = int(input())
M = [list(map(int, input().split())) for _ in range(N)]
ans = [[math.inf for _ in range(N)] for _ in range(N)]

# Left movements are not allowed, so the problem can be solved incrementally
# column by column from right to left, getting the minimal cost from that
# point onwards.
for col in reversed(range(N)):
    for row in reversed(range(N)):
        # Each cell is initialized with the cost of jumping right
        # (0 for the final column)
        jump = ans[row][col + 1] if col < N-1 else 0 # jump right
        # Then down-jump costs are propagated from bottom to top,
        if row < N-1: # jump down
            jump = min(jump, ans[row + 1][col])
        ans[row][col] = min(ans[row][col], M[row][col] + jump)
    for row in range(N):
        jump = math.inf
        # And up-jump costs are propagated from top to bottom.
        if row > 0: # jump up
            jump = min(jump, ans[row - 1][col])
        ans[row][col] = min(ans[row][col], M[row][col] + jump)
# The minimal path cost is the minimum entry on the first column
print(min([ans[row][0] for row in range(N)]))
