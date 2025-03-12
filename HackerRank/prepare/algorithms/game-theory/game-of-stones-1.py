# https://www.hackerrank.com/challenges/game-of-stones-1/
def make_ans(win, q):
    if q < len(win):
        return win[q]
    while len(win) <= q:
        i = len(win)
        win.append(any([not win[i - 2], not win[i - 3], not win[i - 5]]))
    return win[q]

win = [False, False, True, True, True, True]
for _ in range(int(input())):
    q = int(input())
    print("First" if make_ans(win, q) else "Second")
