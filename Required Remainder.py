#Codeforces Round 653 (Div. 3)
n = int(input())
def func(a,b,c):
    if c-(c%a)+b <= c:
        return c-(c%a)+b
    else:
         return c-(c%a)+b-a
for i in range(n):
    x,y,n = [int(x) for x in input().split()]
    d = func(x,y,n)
    print(d)
