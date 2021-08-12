n,m = [int(x) for x in input().split()]
lst = [int(x) for x in input().split()]
t = 1
c = 0
for i in range(len(lst)):
    if lst[i] >= t :
        z = lst[i] - t
        t = lst[i]
        c += z
    else:
        p = (n-t) + (lst[i] - 1) +1
        t = lst[i]
        c += p
print(c)