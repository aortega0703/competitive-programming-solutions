import sys

def is_special(A):
    memo = {0: 0}
    memo_delta = {}
    # Are all sums different?
    for new_elem in A:
        for (elem_sum, elem_count) in memo.items():
            new_sum = elem_sum + new_elem
            # print(f"{new_sum} = {elem_sum} + {new_elem}")
            if new_sum in memo:
                return False
            memo_delta[new_sum] = elem_count + 1
        memo.update(memo_delta)
    # Are sums of more elements greater?
    count_max = 0
    for (elem_sum, elem_count) in sorted(memo.items(), key=lambda item: item[0]):
        # print(f"{elem_count} <? {count_max} for {elem_sum}")
        if elem_count < count_max:
            return False
        count_max = max(count_max, elem_count)
    return True

def main():
    ans = 0
    for line in sys.stdin:
        A = list(map(int, line.split(",")))
        if is_special(A):
            ans += sum(A)
    print(ans)

main()
