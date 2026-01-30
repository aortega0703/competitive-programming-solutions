import math

# The problem asks to find a and b such that
# 10^k * a + b = (a + b)^2 < 10^16
# we can simply check for m = a + b < 10*8 if m^2 can be split in such a way.
#
# It's not necessary to check all splits of n^2, splitting down the middle (
# or the middle-adjacent for odd lengths) sufices:
# For m^2 with even length 2L, m has length L so both a and b have to have
# length L too (moving the split would result in either a > m or b > m).
# For m^2 with odd length 2L + 1, m has length L + 1 so we have to check the
# split on L and on L + 1. This means 
#
# We only need to check for m = 9q or m = 9q + 1:
# With some modular arithmetic on the statement
# 10^k * a + b = (a + b)^2
# a + b = (a + b)^2 (mod 9)
# which is only true for a + b = 0 or a + b = 1 (mod 9)

def count_digits(n):
    return int(math.log10(n)) + 1

def split(root, square, square_digits):
    root_digits = (square_digits + 1) // 2

    a_shift = 10**root_digits
    a, b = divmod(square, a_shift)
    if root == a + b and b >= a_shift // 10:
        return (a, b)
    # Apparently when ||m^2|| = 2L + 1 we only have to check one split, being
    # ||a|| = L and ||b|| = L + 1.
    # I think this is because if 'a' were the greater one then
    # a = c_0.c_1 c_2... x10^L
    # b =   0.d_1 d_1... x10^L
    # and
    # a + b =       d_0.e_1 e_2... x10^L
    # or    = (c_0 + 1).e_1 e_2... x 10^L
    # m   = (d_0 + 0.e_1 e_2...) x 10^L
    # m^2 = (d_0^2 + 2 d_0 * 0.e_1 e_2... + (0.e_1 e_2...)^2) x 10^(2L)
    # as (a + b)^2 and a have to start with the same digits, squaring (a + b)
    # ruins those digits.
    return None

def main():
    max_digits = int(input())

    ans = 0

    root = 9 
    square = root * root
    square_digits = count_digits(square)
    while square_digits <= max_digits:
        # (a + b) % 9 = 0
        m = split(root, square, square_digits)
        if m != None:
            print(f"{square} = {root}^2 = ({m[0]} + {m[1]})^2")
            ans += square

        # (a + b) % 9 = 1
        root += 1
        square = root * root
        square_digits = count_digits(square)

        m = split(root, square, square_digits)
        if m != None:
            print(f"{square} = {root}^2 = ({m[0]} + {m[1]})^2")
            ans += square

        # (a + b) % 9 = 0 again
        root += 8
        square = root * root
        square_digits = count_digits(square)
    print()
    print(ans)
        
main()
