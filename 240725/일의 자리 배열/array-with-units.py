import copy
arr = list(map(int,input().split()))
a = arr.copy()
for i in range(2,10):
    a.append((a[-1]+a[-2])%10)

print(*a)