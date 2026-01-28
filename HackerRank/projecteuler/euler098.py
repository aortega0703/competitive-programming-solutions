N = int(input())

anagram_count = {}
anagram_max = (0, 0)
n = 1
while n*n < 10**N:
    if len(str(n*n)) < N:
        n += 1
        continue
    anagram = "".join(sorted(str(n*n), reverse = True))
    count = anagram_count.get(anagram, 0) + 1
    anagram_count[anagram] = count
    if count >= anagram_max[0]:
        anagram_max = (count, n*n)
    n += 1
print(anagram_max[1])
