T = int(input())
N = [input() for _ in range(T)]

roman_digits = "IVXLCDM"
roman_to_index = {digit: index for (index, digit) in enumerate(roman_digits)}
roman_to_value = [1, 5, 10, 50, 100, 500, 1000]
huehue = [-1, [0], [0, 0], [0, 0, 0], [0, 1], [1], [1, 0], [1, 0, 0], [1, 0, 0, 0], [0, 2]]

def roman_to_dec(roman_str):
    roman_indices = list(map(roman_to_index.get, roman_str))
    str_id = len(roman_str) - 2
    roman_value = [roman_to_value[roman_indices[-1]]]
    while str_id >= 0: 
        curr_id = roman_indices[str_id]
        if curr_id < roman_indices[str_id + 1]:
            roman_value[-1] -= roman_to_value[curr_id]
        else:
            roman_value.append(roman_to_value[curr_id])
        str_id -= 1
    # print(roman_value)
    return sum(roman_value)

def dec_to_roman(dec):
    # roman = "M" * (dec // 1000)
    # dec %= 1000 
    roman = ""
    if dec % 10 != 0:
        roman = "".join([roman_digits[k] for k in huehue[dec % 10]]) + roman
    dec //= 10
    if dec % 10 != 0:
        roman = "".join([roman_digits[k + 2] for k in huehue[dec % 10]]) + roman
    dec //= 10
    if dec % 10 != 0:
        roman = "".join([roman_digits[k + 4] for k in huehue[dec % 10]]) + roman
    dec //= 10
    roman = "M" * dec + roman
    return roman

for roman_str in N:
    # print(roman_str)
    dec = roman_to_dec(roman_str)
    # print(dec)
    roman = dec_to_roman(dec)
    print(roman)
    # print()
