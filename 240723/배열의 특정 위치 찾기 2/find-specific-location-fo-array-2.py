a = list(map(int,input().split()))
b = 0
c = 0
for i in range(10):
    if i % 2 == 0:
        b += a[i]
    else:
        c += a[i]
if b > c:
    print(b-c)
else:
    print(c-b)