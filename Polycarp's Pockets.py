#Codeforces Round 494 (Div. 3)

from collections import Counter
n = int(input())
a = [int(x) for x in input().split()]
l = len(set(a))
c = 0
d = Counter(a)
if l == len(a):
    print(1)
else:
    print(max(d.values()))