import math

def recurse(factors, product, summ):
    for new_factor in range(factors[-1], (2 * N // product) + 1):
        new_product = product * new_factor
        new_summ = summ + new_factor
        ones = new_product - new_summ
        terms = len(factors) + 1 + ones 
        if terms > N:
            break
        ans[terms] = min(ans[terms], new_product)
        recurse(factors + [new_factor], new_product, new_summ)

N = int(input())
ans = [math.inf for k in range(N + 1)]

for least_factor in range(2, N + 1):
    recurse([least_factor], least_factor, least_factor)

print(sum(set(ans[2:])))
