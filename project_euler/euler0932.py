import math

def count_digits(n):
    if n == 0:
        return 1
    return int(math.log10(n)) + 1

def main():
    max_digits = int(input())

    ans = 0

    # 4^2 = 16 is the smallest "splitable" square (>= 2 digits)
    root = 4 
    n = root * root
    square_digits = count_digits(n)
    root_digits = count_digits(root)
    root_digit_bound = 10**root_digits

    square_digit_bound = 10 * math.sqrt(10)
    while square_digits <= max_digits:
        a_digits = square_digits - root_digits
        a_shift = root_digit_bound
        # stop once a surpasses root's digit count
        while a_digits <= root_digits:
            a, b = divmod(n, a_shift)

            a_digits += 1
            a_shift //= 10
            # numbers with leading 0s aren't valid for concatenation
            if b < a_shift:
                continue

            if root == a + b:
                # n^2 is a 2025-number
                print(f"{n} = {root}^2 = ({a} + {b})^2")
                ans += n
                break

        root += 1
        n = root * root
        if root >= root_digit_bound:
            root_digits += 1
            root_digit_bound *= 10
            print(f"{square_digits} digits total: {ans}")
            square_digits += 1
        if root > int(square_digit_bound):
            print(f"{square_digits} digits total: {ans}")
            square_digits += 1
            square_digit_bound *= 10
    print()
    print(ans)
        
main()
