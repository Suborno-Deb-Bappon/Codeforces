from itertools import *

def funclist(facs):
    def Average(lst):
        return sum(lst) / len(lst)
    maximum = max(facs)
    for i in range(len(facs)): 
        if facs[i] == maximum :
            facs.remove(maximum)
            break
    a = Average(facs)
    fin = maximum + a
    return fin

p = []
n = int(input())
for i in range(n):
    m = int(input())
    lst = [int(z) for z in input().split()]
    p.append(funclist(lst))
for r in range(len(p)):
    print(format(p[r],".9f"))