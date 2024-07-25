n = int(input())

start = [1]
start.append(n)
while True:
    start.append(start[-1]+start[-2])
    if start[-1] >= 100:
        break
for i in start:
    print(i,end=' ')