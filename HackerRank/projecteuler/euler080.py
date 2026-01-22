import decimal
import math
import sys

#f(x) = x^2 - s
def sqrt_newton(s, tolerance):
    x_n_prev = s
    f = lambda x: x * x - s
    Df = lambda x: 2 * x
    digit_error = 0
    while digit_error < tolerance:
        x_n_curr = x_n_prev - f(x_n_prev) / Df(x_n_prev)
        abs_error = abs(x_n_curr - x_n_prev)
        digit_error = -math.log10(abs_error)
        print(x_n_prev, x_n_curr, abs_error, digit_error)
        x_n_prev = x_n_curr
    return x_n_curr

N = int(input())
P = int(input())
decimal.getcontext().prec = P + 10
sys.set_int_max_str_digits(10000)
last_root = 2
acum = 0
ten_power = 10**P
for x in range(2, N + 1):
    if last_root * last_root == x:
        last_root += 1
        continue
    root = decimal.Decimal(x).sqrt()
    truncated = math.floor(root * ten_power)
    digit_sum = sum(int(c) for c in str(truncated)[:P])
    acum += digit_sum
    # print(digit_sum)
print(acum)
