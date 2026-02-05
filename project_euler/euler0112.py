goal_percent = float(input())
not_bouncy = 9
N = 9
while 100 * (N - not_bouncy) != N * goal_percent:
    N += 1
    N_ordered =  sorted(str(N))
    if int("".join(N_ordered)) == N or int("".join(reversed(N_ordered))) == N:
        not_bouncy += 1
    # print(N, not_bouncy, 100 * (N - not_bouncy) / N)
print(N)
    
