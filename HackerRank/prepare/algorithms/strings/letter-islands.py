class AVL:
    def __init__(self, key):
        self.key = key
        self.left = self.right = self.parent = None
        self.height = 1
        self.value = None

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

    def search(tree, key):
        while tree != None and key != tree.key:
            side = key > tree.key
            tree = tree.get_child(side)
        return tree

    def extreme(tree, side):
        if tree == None:
            return None
        while tree.get_child(side) != None:
            tree = tree.get_child(side)
        return tree

    def adjacent(tree, key, side):
        if tree == None:
            return None
        if key < tree.key:
            child = adjacent(tree.left, key, side)
            if child == None and side:
                return tree
            return child
        if key > tree.key:
            child = adjacent(tree.right, key, side)
            if child == None and not side:
                return tree
            return child
        return AVL.extreme(tree.get_child(side), not side)

    def get_height(tree):
        if tree == None:
            return 0
        return tree.height

    def get_balance(tree):
        if tree == None:
            return 0
        return AVL.get_height(tree.right) - AVL.get_height(tree.left)

    def rotate(tree, side):
        child = tree.get_child(not side)
        tree.set_child(AVL.get_child(child, side), not side)
        child.set_child(tree, side)
        return child

    def rebalance(tree):
        balance = AVL.get_balance(tree)
        if balance < -1:
            if AVL.get_balance(tree.left) > 0:
                child = tree.left.rotate(False)
                tree.set_child(child, False)
            return tree.rotate(True)
        if balance > 1:
            if AVL.get_balance(tree.right) < 0:
                child = tree.right.rotate(True)
                tree.set_child(child, True)
            return tree.rotate(False)
        return tree

    def join(left, right, key):
        balance = AVL.get_height(right) - AVL.get_height(left)
        if balance < -1:
            child = AVL.join(left.right, right, key)
            left.set_child(child, True)
            return left.rebalance()
        if balance > 1:
            child = AVL.join(left, right.left, key)
            right.set_child(child, False)
            return right.rebalance()
        tree = AVL(key)
        tree.set_child(left, False)
        tree.set_child(right, True)
        return tree

    def split(tree, key):
        if tree == None:
            return None, None, False
        if key < tree.key:
            left, right, found = AVL.split(tree.left, key)
            return left, AVL.join(right, tree.right, tree.key), found
        if key > tree.key:
            left, right, found = AVL.split(tree.right, key)
            return AVL.join(tree.left, left, tree.key), right, found
        return tree.left, tree.right, True

    def insert(tree, key):
        if tree == None:
            return AVL(key)
        if key < tree.key:
            child = AVL.insert(tree.left, key)
            return AVL.join(child, tree.right, tree.key)
        if key > tree.key:
            child = AVL.insert(tree.right, key)
            return AVL.join(tree.left, child, tree.key)
        return tree

    def union(t1, t2):
        if t1 == None:
            return t2
        if t2 == None:
            return t1
        t2_left, t2_right, found = AVL.split(t2, t1.key)
        left = AVL.union(t2_left, t1.left)
        right = AVL.union(t2_right, t1.right)
        return AVL.join(left, right, t1.key)

    def DFS(tree, order):
        if tree == None:
            return []
        ans = [AVL.DFS(tree.left, order), AVL.DFS(tree.right, order)]
        ans.insert(order, [tree])
        return ans[0] + ans[1] + ans[2]

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
    diffs = {}
    for i in range(1, len(indices)):
        key = indices[i] - indices[i - 1]
        if key in diffs:
            diffs[key] += 1
        else:
            diffs[key] = 1
    keys = sorted(diffs.keys())
    for i in range(1, len(keys)):
        diffs[keys[i]] += diffs[keys[i - 1]]
    for l in lens:
        start = end = 0
        for i, k in enumerate(keys):
            if k > l:
                start = end = i
            #TODO

def make_ans(suffix, lcp):
    stack = [0]
    for i in range(1, len(lcp)):
        while lcp[i] < stack[-1]:
            first_index = stack.pop() - 1
            indices = suffix[first_index : i]
            lens = list(range(lcp[first_index] + 1, lcp[first_index + 1] + 1))
            print(sorted(indices), lens)
            make_isles(sorted(indices), lens)
        if lcp[i] > stack[-1]:
            stack.append(i)
    i += 1
    while len(stack) > 1:
        first_index = stack.pop() - 1
        indices = suffix[first_index : i]
        lens = list(range(lcp[first_index] + 1, lcp[first_index + 1] + 1))
        print(sorted(indices), lens)
        make_isles(sorted(indices), lens)

text = input()
suffix, rank = make_suffix(text)
lcp = make_lcp(text, suffix, rank)
print(*range(len(text)))
print(" ".join(list(text)))
print(*suffix)
print(*rank)
print(*lcp)
make_ans(suffix, lcp)
