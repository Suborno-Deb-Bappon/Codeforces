#Codeforces Round 677 (Div. 3)

t = int(input())
for i in range(t):
    x = input()
    s = 0
    for j in range(len(x)):
        s += j+1
    r = 10 * (int(x[0])-1) + s
    print(r)
