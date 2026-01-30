import math

def count_digits(n):
    return int(math.log10(n)) + 1

def split(C, S, C_digits):
    if C <= S:
        return C == S
    for b_digits in range(1, C_digits):
        (a, b) = divmod(C, 10**b_digits)
        if split(a, S - b, C_digits - b_digits):
            return True
    return False

def main():
    max_digits = int(input())

    ans = 0

    root = 9 
    square = root * root
    square_digits = count_digits(square)
    while square_digits <= max_digits:
        # (a + b) % 9 = 0
        if split(square, root, square_digits):
            print(f"{square}", square_digits)
            ans += square

        # (a + b) % 9 = 1
        root += 1
        square = root * root
        square_digits = count_digits(square)
        if split(square, root, square_digits):
            print(f"{square}", square_digits)
            ans += square

        # (a + b) % 9 = 0 again
        root += 8
        square = root * root
        square_digits = count_digits(square)
    print()
    print(ans)
        
main()
