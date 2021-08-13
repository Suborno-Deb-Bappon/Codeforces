n = int(input())
a = [int(x) for x in input().split()]
maxi = max(a)
c = 0
if len(a) == 1:
    print(0)
    exit()
for i in range(len(a)):
    if a[i] == maxi:
        continue
    z = maxi - a[i]
    c += z
print(c)