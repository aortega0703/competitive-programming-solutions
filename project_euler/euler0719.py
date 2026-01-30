import math

def count_digits(n):
    return int(math.log10(n)) + 1

def split(square, square_digits, root, root_digits, terms):
    # print(f"{square},  {terms}, {root}")
    if square_digits <= root_digits and root == sum(terms) + square:
        return [square] + terms
    if square_digits < 2:
        return None
    for b_digits in range(1, root_digits + 1):
        (a, b) = divmod(square, 10**b_digits)
        a_digits = square_digits - b_digits
        result = split(a, a_digits, root, root_digits, [b] + terms)
        if result != None:
            return result
    return None

def main():
    max_digits = int(input())

    ans = 0

    root = 9 
    square = root * root
    square_digits = count_digits(square)
    while square_digits <= max_digits:
        # (a + b) % 9 = 0
        root_digits = (square_digits + 1) // 2
        m = split(square, square_digits, root, root_digits, [])
        if m != None:
            print(f"{square} = {root}^2 = ({" + ".join(map(str,m))})^2")
            ans += square

        # (a + b) % 9 = 1
        root += 1
        square = root * root
        square_digits = count_digits(square)
        root_digits = (square_digits + 1) // 2
        m = split(square, square_digits, root, root_digits, [])
        if m != None:
            print(f"{square} = {root}^2 = ({" + ".join(map(str,m))})^2")
            ans += square

        # (a + b) % 9 = 0 again
        root += 8
        square = root * root
        square_digits = count_digits(square)
    print()
    print(ans)
        
main()
