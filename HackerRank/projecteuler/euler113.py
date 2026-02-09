mod = 10**9 + 7

def flat(len_N):
    return (9 * len_N) % mod

def dp_inc(len_N, memo):
    old_memo_len = len(memo)
    # [index][start_digit]
    for _ in range(old_memo_len, len_N + 1):
        memo.append([0] * 10)
    if old_memo_len == 0:
        for d in range(10):
            memo[0][d] = 1

    for i in range(max(1, old_memo_len), len_N + 1):
        for d in range(10):
            for next_d in range(d, 10):
                memo[i][d] += memo[i - 1][next_d]
                memo[i][d] %= mod
        
    ans = memo[len_N][0] - 1

    return ans

def dp_dec(len_N, memo):
    old_memo_len = len(memo)
    # [is_nonzero][is_tight][last_digit][index]
    for _ in range(old_memo_len, len_N + 1):
        memo.append([0] * 10)
    if old_memo_len == 0:
        for d in range(10):
            memo[0][d] = 1

    for i in range(max(1, old_memo_len), len_N + 1):
        for d in range(10):
            for next_d in range(0, d + 1):
                memo[i][d] += memo[i - 1][next_d]
                memo[i][d] %= mod
        
    ans = 0
    for i in range(len_N + 1):
        ans += memo[i][9] - 1
        ans %= mod
    return ans

def dp(len_N, memo_inc, memo_dec):
    inc = dp_inc(len_N, memo_inc)
    dec = dp_dec(len_N, memo_dec)
    return (inc + dec - flat(len_N)) % mod

T = int(input())
memo_inc = []
memo_dec = []
for _ in range(T):
    k = int(input())
    ans = dp(k, memo_inc, memo_dec)
    print(ans)
