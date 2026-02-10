def remove_id(N, id):
    right = N % 10**id
    left = N // 10**(id + 1)
    return left * 10**id + right

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

N, K = map(int, input().split())
ans_num = 1
ans_den = 1
for den in range(10**(N - 1), 10**N):
    for num in range(10**(N - 1), den):
        for den_id, d in enumerate(str(den)):
            if d == '0':
                continue
            num_id = str(num).find(d)
            den_id = len(str(den)) - den_id - 1
            num_id = len(str(num)) - num_id - 1
            # print(f"{num}, {den}, {d}, {num_id}")
            if num_id == -1:
                continue
            new_num = remove_id(num, num_id)
            new_den = remove_id(den, den_id)
            if num * new_den == den * new_num:
                ans_num *= new_num
                ans_den *= new_den
                print(f"{num} / {den} = {new_num} / {new_den}, ")
                # print(f"!!!!!!")
g = gcd(ans_num, ans_den)
print("-" * 10)
print(f"{ans_num // g} / {ans_den // g}")
