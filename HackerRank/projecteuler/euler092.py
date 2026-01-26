max_digits = int(input())
mod = 10**9 + 7

sums = [0 for _ in range(max_digits * 9**2 + 1)]
for digit in range(0, 10):
    sums[digit**2] += 1

for digits in range(2, max_digits + 1):
    for chain_next in range(digits * 9**2, 0, -1):
        for digit in range(1, 10):
            if digit**2 > chain_next:
                break
            sums[chain_next] += sums[chain_next - digit**2]
            sums[chain_next] %= mod

ans = 0
for digit in range(1, max_digits * 9**2 + 1):
    chain_next = digit
    while chain_next != 1 and chain_next != 89:
        chain_next = sum(map(lambda d: int(d)**2, str(chain_next)))
    if chain_next == 89:
        ans += sums[digit]
        ans %= mod
print(ans)
