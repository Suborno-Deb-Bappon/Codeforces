#Codeforces Round 713 (Div. 3)

t = int(input())
for i in range(t):
    n = int(input())
    lst = [int(x) for x in input().split()]
    for j in range(len(lst)-1):
        if j == 0:
            if lst[j] != lst[j+1] and lst[j+1] == lst[j+2]:
                print(j+1)
                break
            if lst[j] != lst[j+1] and lst[j+1] != lst[j+2]:
                print(j+2)
                break
        if lst[j+1] - lst[j] != 0:
            print(j+2)
            break