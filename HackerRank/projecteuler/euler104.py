import math

def get_digits(n):
    return int(math.log10(n)) + 1

def get_first_last(n, k, first_mask, last_mask):
    first = n // first_mask
    last = n % last_mask
    return first, last

def is_k_pandigital(n, k, expected_hash):
    # Sum of the digits 1...k mod 9 equals 1...k mod 9
    hash = n % 9
    if hash != expected_hash:
        return False
    # Check for the digits 1...k using a bitmask where the i-th bit means the
    # digit 'i' is present
    check = 0
    for _ in range(k):
        n, digit = divmod(n, 10)
        digit_mask = 1 << digit
        # There's an undesired digit: there is no space for 1...k
        if digit > k or check & digit_mask != 0:
            return False
        check |= digit_mask
    return True

def prefix(n, k):
    return int(str(n)[:k])

def add_first(a_pair, b_pair, k):
    a, a_digits = a_pair
    b, b_digits = b_pair
    # a and b should differ by at most 1 order of magnitude, so this aligns
    # the correct digit values
    if get_digits(a) == k and b_digits > a_digits:
        b *= 10
    c = a + b
    c_digits = b_digits
    if get_digits(c) > get_digits(b):
        c_digits += 1
    return (prefix(c, k), c_digits)

def main(a, b, k):
    fib_1 = a
    fib_2 = b
    if k == 1 and (a == 1 or b == 1):
        print(1)
        return
    expected_hash = (k * (k + 1) // 2) % 9 
    first_mask = 1
    last_mask = 10**k
    last_digits = 1
    fib_1_first = (fib_1, 1)
    fib_2_first = (fib_2, 1)
    fib_1_last = fib_1
    fib_2_last = fib_2
    for n in range(3, 2 * 10**6 + 1):
        # The first k digits of a + b can be aproximated using the first k
        # digits of a and b. As k is at most 9, I'm storing the first 18
        # digits so that errors don't accumulate up messing the sum.
        # (This passes the test but I don't know exactly how to get an
        # appropiate limit for this)
        fib_3_first = add_first(fib_1_first, fib_2_first, 18)
        # The last k digits of a + b is simply
        # (a + b) % 10**k
        # = (a % 10**k + b % 10**k) % 10**k
        # So we only need to keep track of the last k digit of each number 
        fib_3_last = (fib_1_last + fib_2_last) % last_mask

        first = prefix(fib_3_first[0], k)
        first_is_pan = is_k_pandigital(first, k, expected_hash)
        last_is_pan = is_k_pandigital(fib_3_last, k, expected_hash)

        if first_is_pan and last_is_pan:
            print(n)
            break
        # Set up the next iteration
        fib_1_first = fib_2_first
        fib_2_first = fib_3_first
        fib_1_last = fib_2_last
        fib_2_last = fib_3_last
    else:
        print("no solution")

a, b, k = (int(input()) for _ in range(3))
main(a, b, k)
