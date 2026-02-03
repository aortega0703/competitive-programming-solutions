def is_special(A):
    if len(A) == 1:
        return True
    if len(A) > 25:
        return False
    A = sorted(A)
    # Compare the sum of the smallest k+1 and biggest k elements.
    # This ensures condition 2: |A| > |B| => S(A) > S(B)
    sum_first = A[0]
    sum_last = 0
    for k in range(1, (len(A) + 1) // 2):
        sum_first += A[k]
        sum_last += A[-k]
        if sum_last > sum_first:
            return False

    memo = {0}
    memo_delta = set()
    # Compute all sums of P{A_0}, then P{A_0, A_1}, then ... until P(A)
    # This relies on P(A u {b}) = P(A) u {a u b| a in P(A)}
    # This means O(2^n) operations, but I think I can do half as many
    # operations (still O(2^n) tho) by only considering the sums of subsets
    # of length <= n/2 (because condition 2 guarantees there is no smaller
    # set with the same sum, and there are no disjoint sets with equal or
    # more elements).
    # In reality as inputs are capped at 10^6 sums range from n to n*10^6,
    # but there are 2^n subsets, so this will always fail for
    # 2^n > n 10^6
    # n > log2(n) + log2(10^6)
    # n - log2(n) > 20
    # n ~ 25
    for new_elem in A:
        for elem_sum in memo:
            new_sum = elem_sum + new_elem
            if new_sum in memo:
                return False
            memo_delta.add(new_sum)
        memo.update(memo_delta)
    return True

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        print("YES" if is_special(A) else "NO")

main()
