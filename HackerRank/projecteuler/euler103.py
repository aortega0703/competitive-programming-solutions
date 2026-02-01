# Solution in O(N)
# S_(n)(0)
# = S_(n-1)(n//2)
# = S_(n-1)(0) + S_(n-2)(n//2 - 1)
# = S_(n-1)(0) + S_(n-2)(0) + S_(n-3)(n//2 - 2)
# ...
# = S_(n-1)(0) + S_(n-2)(0) + ... + S_(n - n//2)(0)
# with the same logic
# S_(n-1)(0)
# = S_(n-2)(0) + ... + S_(n - (n-1)//2)(0)
# = S_(n-2)(0) + ... + S_(n - n//2)(0) for n odd
# or
# = S_(n-2)(0) + ... + S_(n - n//2 - 1)(0) for n even
# then
# S_(n)(0) = 2 * S_(n-1)(0) for n odd
# or 
# S_(n)(0) = 2 * S_(n-1)(0) - S_(n - n//2 - 1)(0) for n odd
#
#
# S_(n)(k)
# = S_(n)(0) + S_(n-1)(k-1)
# = S_(n)(0) + S_(n-1)(0) + S_(n-2)(k-2)
# ...
# = S_(n)(0) + ... + S_(n-k)(0)

def main():
    N = int(input())
    mod = 715_827_881
    set_N_0 = [0, 1, 1]
    for n in range(3, N + 1):
        next = 2*set_N_0[-1]
        if n % 2 == 0:
            next -= set_N_0[n//2 - 1]
        set_N_0.append(next % mod)
    set_N = [set_N_0[-1]]
    for k in range(N-1, 0, -1):
        next = set_N[-1] + set_N_0[k]
        set_N.append(next % mod)
    print(*set_N)

main()
