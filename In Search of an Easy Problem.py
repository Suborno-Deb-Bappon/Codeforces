n = int(input())
lst = [int(x) for x in input().split()]

for i in range(len(lst)):
    if lst[i] == 1:
        print("HARD")
        exit()
print("EASY")