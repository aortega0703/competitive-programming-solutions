def to_list(N):
    if N == 0:
        return [0]
    ans = []
    while N > 0:
        N, d = divmod(N, 10)
        ans.append(d)
    return ans

def to_int(L):
    ans = 0
    shift = 1
    for k in L:
        ans += k * shift
        shift *= 10
    return ans

def flat(N):
    N_list = to_list(N)
    ans = 9 * (len(N_list) - 1)
    for d in range(1, 10):
        if to_int([d] * len(N_list)) <= N:
            ans += 1
        else:
            break
    return ans

def dp_inc(N, memo):
    N_list = to_list(N)
    old_memo_len = len(memo)
    # [index][start_digit]
    for _ in range(old_memo_len, len(N_list)):
        memo.append([0] * 10)
    if old_memo_len == 0:
        for d in range(10):
            memo[0][d] = 1

    for i in range(max(1, old_memo_len), len(N_list)):
        for d in range(10):
            for next_d in range(d, 10):
                memo[i][d] += memo[i - 1][next_d]
        
    ans = 0
    for i in range(len(N_list) - 1):
        for d in range(1, 10):
            ans += memo[i][d]

    last_d = 1
    for i in reversed(range(len(N_list))):
        curr_d = N_list[i]
        for d in range(last_d, curr_d):
            ans += memo[i][d]
        if curr_d < last_d:
            break
        if i == 0:
            ans += 1
        last_d = curr_d
    return ans

def dp_dec(N, memo):
    N_list = to_list(N)
    old_memo_len = len(memo)
    # [is_nonzero][is_tight][last_digit][index]
    for _ in range(old_memo_len, len(N_list)):
        memo.append([0] * 10)
    if old_memo_len == 0:
        for d in range(10):
            memo[0][d] = 1

    for i in range(max(1, old_memo_len), len(N_list)):
        for d in range(10):
            for next_d in range(0, d + 1):
                memo[i][d] += memo[i - 1][next_d]
        
    ans = 0
    for i in range(len(N_list) - 1):
        for d in range(1, 10):
            ans += memo[i][d]

    last_d = 9
    for i in reversed(range(len(N_list))):
        curr_d = N_list[i]
        for d in range(1, min(curr_d, last_d + 1)):
            ans += memo[i][d]
        ans += i < len(N_list) - 1
        if curr_d == 0 or curr_d > last_d:
            break
        if i == 0:
            ans += 1
        last_d = curr_d
    return ans

def dp(N, memo_inc, memo_dec):
    return dp_inc(N, memo_inc) + dp_dec(N, memo_dec) - flat(N)
       
N = 10**100 - 1
memo_inc = []
memo_dec = []
print(dp(N, memo_inc, memo_dec))
