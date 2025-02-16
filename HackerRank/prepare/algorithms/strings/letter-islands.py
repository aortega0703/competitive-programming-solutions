class AVL:
    def __init__(self, key):
        self.key = key
        self.left = self.right = self.parent = None
        self.height = 1
        self.weight = 0
        self.count = 0
        self.pred = self.suc = None

    def get_child(self, side):
        return self.right if side else self.left

    def set_child(self, child, side):
        if side:
            self.right = child
        else:
            self.left = child
        if child != None:
            child.parent = self
        self.height = 1 + max(AVL.get_height(self.left), AVL.get_height(self.right))
        self.weight = self.count + AVL.get_weight(self.left) + AVL.get_weight(self.right)

    def search(tree, key):
        if tree == None:
            return None
        if key < tree.key:
            return AVL.search(tree.left, key)
        if key > tree.key:
            return AVL.search(tree.right, key)
        return tree

    def extreme(tree, side):
        if tree == None:
            return None
        if tree.get_child(side) != None:
            return AVL.extreme(tree.get_child(side), side)
        return tree

    def adjacent(tree, key, side):
        if tree == None:
            return None
        if key < tree.key:
            adj = AVL.adjacent(tree.left, key, side)
            if adj == None and side:
                return tree
            return adj
        if key > tree.key:
            adj = AVL.adjacent(tree.right, key, side)
            if adj == None and not side:
                return tree
            return adj
        return AVL.adjacent(tree.get_child(side), key, side)

    def get_height(tree):
        if tree == None:
            return 0
        return tree.height

    def get_balance(tree):
        if tree == None:
            return 0
        return AVL.get_height(tree.right) - AVL.get_height(tree.left)

    def rotate(self, side):
        child = self.get_child(not side)
        self.set_child(child.get_child(side), not side)
        child.set_child(self, side)
        return child

    def rebalance(tree):
        if AVL.get_balance(tree) < -1:
            if AVL.get_balance(tree.left) > 0:
                child = tree.left.rotate(False)
                tree.set_child(child, False)
            return tree.rotate(True)
        if AVL.get_balance(tree) > 1:
            if AVL.get_balance(tree.right) < 0:
                child = tree.right.rotate(True)
                tree.set_child(child, True)
            return tree.rotate(False)
        return tree

    def join(left, right, tree):
        balance = AVL.get_height(right) - AVL.get_height(left)
        if balance < -1:
            child = AVL.join(left.right, right, tree)
            left.set_child(child, True)
            return AVL.rebalance(left)
        if balance > 1:
            child = AVL.join(left, right.left, tree)
            right.set_child(child, False)
            return AVL.rebalance(right)
        tree.set_child(left, False)
        tree.set_child(right, True)
        return tree

    def split(tree, key):
        if tree == None:
            return None, None, None
        if key < tree.key:
            left, mid, found = AVL.split(tree.left, key)
            return left, AVL.join(mid, tree.right, tree), found
        if key > tree.key:
            mid, right, found = AVL.split(tree.right, key)
            return AVL.join(tree.left, mid, tree), right, found
        return tree.left, tree.right, tree

    def split_last(tree):
        if tree.right == None:
            return tree.left, tree
        right, last = AVL.split_last(tree.right)
        return AVL.join(tree.left, right, tree), last

    def join2(left, right):
        if left == None:
            return right
        if right == None:
            return left
        left, last = AVL.split_last(left)
        return AVL.join(left, right, last)

    def insert(tree, key):
        if tree == None:
            return AVL(key)
        if key < tree.key:
            left = AVL.insert(tree.left, key)
            tree = AVL.join(left, tree.right, tree)
        if key > tree.key:
            right = AVL.insert(tree.right, key)
            tree = AVL.join(tree.left, right, tree)
        return tree

    def delete(tree, key):
        if tree == None:
            return None
        left, right, item = AVL.split(tree, key)
        return AVL.join2(left, right)

    def union(t1, t2):
        if t1 == None:
            return t2
        if t2 == None:
            return t1
        t2_left, t2_right, found = AVL.split(t2, t1.key)
        left = AVL.union(t2_left, t1.left)
        right = AVL.union(t2_right, t1.right)
        return AVL.join(left, right, t1)

    def union_indices(t1, t2, diffs):
        if t1 == None:
            return t2
        if t2 == None:
            return t1
        t2_left, t2_right, found = AVL.split(t2, t1.key)
        left = AVL.union(t2_left, t1.left)
        right = AVL.union(t2_right, t1.right)
        return AVL.join(left, right, t1)

    def union_diffs(t1, t2):
        if t1 == None:
            return t2
        if t2 == None:
            return t1
        t2_left, t2_right, found = AVL.split(t2, t1.key)
        left = AVL.union(t2_left, t1.left)
        right = AVL.union(t2_right, t1.right)
        if found:
            t1.count += found.count
        return AVL.join(left, right, t1)

    def join_indices(left, right, tree, diffs):
        balance = AVL.get_height(right) - AVL.get_height(left)
        if balance < -1:
            child = AVL.join_indices(left.right, right, tree)
            left.set_child(child, True)
            return AVL.rebalance(left)
        if balance > 1:
            child = AVL.join_indices(left, right.left, tree)
            right.set_child(child, False)
            return AVL.rebalance(right)
        pred = AVL.extreme(left, True)
        succ = AVL.extreme(right, False)
        if pred != None:
            diffs = AVL.insert(diffs, tree.key - pred.key)
            AVL.add_count(diffs, tree.key - pred.key, 1)
        if succ != None:
            diffs = AVL.insert(diffs, succ.key - tree.key)
            AVL.add_count(diffs, succ.key - tree.key, 1)
        tree.set_child(left, False)
        tree.set_child(right, True)
        return tree

    def add_count(tree, key, amount):
        if tree == None:
            return
        if key < tree.key:
            AVL.add_count(tree.left, key, amount)
        elif key > tree.key:
            AVL.add_count(tree.right, key, amount)
        else:
            tree.count += amount
        tree.weight += amount

    def get_weight(tree):
        if tree == None:
            return 0
        return tree.weight

    def acum(tree, key, side):
        if tree == None:
            return 0
        if key < tree.key:
            curr = tree.count + AVL.get_weight(tree.right) if side else 0
            return curr + AVL.acum(tree.left, key, side)
        if key > tree.key:
            curr = tree.count + AVL.get_weight(tree.left) if not side else 0
            return curr + AVL.acum(tree.right, key, side)
        return tree.count + AVL.get_weight(tree.get_child(side))

    def inorder(tree):
        if tree == None:
            return []
        return AVL.inorder(tree.left) + [tree.key] + AVL.inorder(tree.right)

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
import subprocess
def debug(tree, filename):
    def helper(tree, names):
        ans = ""
        if tree == None:
            return ans
        names[tree] = len(names)
        ans += f"{names[tree]} [label=\"{tree.key}, {tree.weight}\"]\n"
        if tree.parent != None:
            ans += f"{names[tree.parent]} -> {names[tree]}\n"
        return ans + helper(tree.left, names) + helper(tree.right, names)
    ans = "strict digraph tree {\n"
    ans += helper(tree, {})
    ans += "}"
    process = ["dot", "-Tpng", f"-o{filename}.png"]
    subprocess.run(process, text = True, input=ans)

def make_isles(lens, diffs, isles):
    for l in lens:
        suc = AVL.adjacent(diffs, l, True)
        if suc != None:
            gaps = AVL.acum(diffs, suc.key, True) + 1
        else:
            gaps = 1
        isles[gaps] = isles.get(gaps, 0) + 1

def add_index(curr_indices, new_indices, diffs, flag):
    for j, i in enumerate(new_indices):
        # print(i, AVL.inorder(curr_indices))
        curr_indices = AVL.insert(curr_indices, i)
        pred = curr_indices.adjacent(i, False)
        suc = curr_indices.adjacent(i, True)
        # print(pred.key if pred != None else None, suc.key if suc != None else None)
        if pred != None and suc != None:
            old_diff = suc.key - pred.key
            diffs.add_count(old_diff, -1)
            if AVL.search(diffs, old_diff) == 0:
                diffs = diffs.delete(old_diff)
        if suc != None:
            new_diff = suc.key - i
            diffs = AVL.insert(diffs, new_diff)
            diffs.add_count(new_diff, 1)
        if pred != None:
            new_diff = i - pred.key
            diffs = AVL.insert(diffs, new_diff)
            diffs.add_count(new_diff, 1)
        if flag >= 0:
            curr_indices.parent = None
            debug(curr_indices, f"{flag}-{j}-i-{i}-{new_indices}")
            if diffs != None:
                diffs.parent = None
                debug(diffs, f"{flag}-{j}-j-{i}-{new_indices}")
    return curr_indices, diffs

import math
def make_ans(suffix, lcp):
    stack = [(0, 0, None, None)]
    isles = {}
    i = 1
    while i < len(lcp):
        last = i
        temp = last
        indices = None
        diffs = None
        count = -math.inf

        while lcp[i] < stack[-1][1]:
            last, common, indices, diffs = stack.pop()
            indices, diffs = add_index(indices, suffix[last - 1 : temp], diffs, count)
            if count >= 0:
                print(suffix[last - 1 : i])
                print(suffix[last - 1 : temp])
            # debug(indices, f"{i}-{count}-0-{suffix[curr - 1 : last]}-{suffix[curr - 1 : i]}")
            # debug(diffs, f"{i}-{count}-1-{suffix[curr - 1 : last]}-{suffix[curr - 1 : i]}")
            count += 1
            lens = range(max(stack[-1][1] + 1, lcp[i] + 1), common + 1)
            make_isles(lens, diffs, isles)
            temp = last - 1
        if lcp[i] > stack[-1][1]:
            stack.append((last, lcp[i], indices, diffs))
        lone = len(lcp) - (suffix[i - 1] + max(lcp[i], lcp[i - 1]))
        isles[1] = isles.get(1, 0) + lone
        # if 5 in isles:
        #     print(i)
        i += 1
    indices = None
    diffs = None
    temp = i
    while len(stack) > 1:
        last, common = stack.pop()
        indices, diffs = add_index(indices, suffix[last - 1 : temp], diffs, -1)
        lens = range(stack[-1][1] + 1, common + 1)
        make_isles(lens, diffs, isles)
        temp = last - 1
    lone = len(lcp) - (suffix[i - 1] + lcp[i - 1])
    isles[1] = isles.get(1, 0) + lone
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
