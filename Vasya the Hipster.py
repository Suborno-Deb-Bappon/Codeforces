a,b =[int(x) for x in input().split()]
if a>0 and b>0:
    s = min(a,b)
else:
    s = 0
p = abs(a-b)
if p>1:
    r = int(p/2)
else:
    r = 0
print(s,r)