
def counting_sort(arr, key, max_elem):
    ans = [0 for _ in arr]
    count = [0 for _ in range(max_elem + 1)]
    for item in arr:
        count[key(item)] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    for item in reversed(arr):
        count[key(item)] -= 1
        ans[count[key(item)]] = item
    return ans

def make_rank(suffix, rank_left, rank_right):
    max_rank = 0
    rank = [0 for _ in suffix]
    for i in range(1, len(suffix)):
        left = rank_left(suffix[i]) != rank_left(suffix[i - 1])
        right = rank_right(suffix[i]) != rank_right(suffix[i - 1])
        if left or right:
            max_rank += 1
        rank[suffix[i]] = max_rank
    return rank, max_rank

def make_suffix(text):
    suffix = list(range(len(text)))
    min_elem = ord(min(text))
    rank = [ord(c) - min_elem for c in text]
    max_rank = max(rank)
    prefix = 1
    rank_left = lambda s: rank[s]
    rank_right = lambda s: rank[s + prefix] + 1 if s + prefix < len(rank) else 0
    while prefix < len(text):
        suffix = counting_sort(suffix, rank_right, max_rank + 1)
        suffix = counting_sort(suffix, rank_left, max_rank)
        rank, max_rank = make_rank(suffix, rank_left, rank_right)
        if max_rank == len(rank) - 1:
            break
        prefix *= 2
    return suffix, rank

def make_lcp(text, suffix, rank):
    common = 0
    lcp = [0 for _ in text]
    for i in range(len(text)):
        if rank[i] == 0:
            continue
        j = suffix[rank[i] - 1]
        m = max(i, j)
        while m + common < len(text) and text[i + common] == text[j + common]:
            common += 1
        lcp[rank[i]] = common
        common -= common > 0
    return lcp

def make_isles(indices, lens, isles):
    # # print("indices", sorted(indices))
    # # print("lens", lens)
    diffs = {}
    for i in range(1, len(indices)):
        key = indices[i] - indices[i - 1]
        if key in diffs:
            diffs[key] += 1
        else:
            diffs[key] = 1
    # # print("diffs", diffs)
    keys = sorted(diffs.keys(), reverse=True)
    for i in range(1, len(keys)):
        diffs[keys[i]] += diffs[keys[i - 1]]
    # # print("acum diffs", diffs)
    keys = sorted(diffs.keys())
    k = 0
    for l in lens:
        while k < len(keys) and keys[k] <= l:
            k += 1
        if k < len(keys):
            gaps = diffs[keys[k]] + 1
        else:
            gaps = 1
        isles[gaps] = isles.get(gaps, 0) + 1
    # # print("isles", isles)

def make_ans(suffix, lcp):
    stack = [(0, 0)]
    isles = {}
    for i in range(1, len(lcp)):
        # print(i)
        last = i
        while lcp[i] < stack[-1][1]:
            # print(stack)
            last, common = stack.pop()
            first_index = last - 1
            indices = suffix[first_index : i]
            lens = list(range(max(stack[-1][1] + 1, lcp[i] + 1), common + 1))
            make_isles(sorted(indices), lens, isles)
            # print(indices, isles)
        if lcp[i] > stack[-1][1]:
            stack.append((last, lcp[i]))
        lone = len(lcp) - (suffix[i - 1] + max(lcp[i], lcp[i - 1]))
        isles[1] = isles.get(1, 0) + lone
        # print(suffix[i - 1], isles)
    i += 1
    # # print(stack)
    while len(stack) > 1:
        # print(stack)
        last, common = stack.pop()
        first_index = last - 1
        indices = suffix[first_index : i]
        lens = list(range(stack[-1][1] + 1, common + 1))
        make_isles(sorted(indices), lens, isles)
        # print(indices, isles)
    lone = len(lcp) - (suffix[i - 1] + lcp[i - 1])
    isles[1] = isles.get(1, 0) + lone
    # print(suffix[i - 1], isles)
    return isles

text = input()
n = int(input())
suffix, rank = make_suffix(text)
lcp = make_lcp(text, suffix, rank)
# print("i:", *range(len(text)))
# print("t:", " ".join(list(text)))
# print("s:", *suffix)
# print("l:", *lcp)
ans = make_ans(suffix, lcp)
print(ans.get(n, 0))
# print(sorted(ans.items()))
