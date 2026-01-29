import math
from math import pi

N = int(input())
triangles = [list(map(int, input().split())) for _ in range(N)]

def covers_origin(triangle):
    angles = []
    for (x, y) in zip(triangle[::2], triangle[1::2]):
        angles.append(math.atan2(y, x))
    deltas = []
    for angle_k in range(len(angles)):
        angle_delta = (angles[angle_k] - angles[angle_k - 1]) % (2 * pi) - pi
        deltas.append(angle_delta)
    return all(t >= 0 for t in deltas) or all(t <= 0 for t in deltas)

print(sum(covers_origin(t) for t in triangles))

