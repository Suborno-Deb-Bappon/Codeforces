n = int(input())
lst = [int(x) for x in input().split()]
total = sum(lst)
r = total / len(lst)
print("{:.12f}".format(r))