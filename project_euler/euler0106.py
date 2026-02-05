import math

def choose(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

def catalan(n):
    return choose(2 * n, n) // (n + 1)

def main(N):
    # We only need to compare sets of equal sizes (because condition 2 gives
    # us the relation between different-sized sets). Then we only consider
    # sets of sizes 2..N/2
    ans = 0
    for k in range(2, N//2 + 1):
        # From N elements pick 2*k elements
        comparables = choose(N, 2 * k)
        # split those 2*k elements in 2 groups of k
        splits = choose(2 * k, k)
        # consider those 2*k elements in order, and let the assignment to
        # "group A" be represented by a "move up" and an assignment to
        # "group B" be represented by a "move down". As there is be an equal
        # number of elements in A and B the "balance" ends at 0. A path
        # that does not cross the axis then represents an "unambigous sum"
        # (e.g. the smallest 4 digits in A and the biggest 4 digits in B does
        # not need a comparison to know which set is bigger). The catalan
        # number C_k counts the number of redundant paths where A < B.
        redundants = catalan(k)
        # 2 * C_k counts the number of redundant paths (in either direction),
        # splits - 2 redundants count the number of "ambiguous splits", and
        # then dividing by 2 accounts for double counting the assignments of
        # A and B (order doesn't matter)
        ans += comparables * (splits - 2 * redundants) // 2
    print(ans)


N = int(input())
main(N)
