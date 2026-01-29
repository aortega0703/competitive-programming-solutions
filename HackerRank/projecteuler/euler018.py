# https://www.hackerrank.com/contests/projecteuler/challenges/euler018/
def maxsum(i,l):
	if l >= n:
		return list[i]
	else:
		return max(maxsum(i+l,l+1), maxsum(i+l+1,l+1)) + list[i]

tc = int(input().strip())
for i in range(tc):
	n = int(input().strip())
	list = []
	for j in range(n):
		list += [int(i) for i in input().strip().split(" ")]
	print(maxsum(0,1))
