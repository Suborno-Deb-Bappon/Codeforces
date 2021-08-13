#Codeforces Round 109 (Div. 2)

n = int(input())
lst = [int(x) for x in input().split()]
c = 0
for i in range(len(lst)):
    if i != 0:
        lst1 = lst[:i]
        mini = min(lst1)
        maxi = max(lst1)
        if lst[i] > maxi or lst[i] < mini:
            c += 1
print(c)
