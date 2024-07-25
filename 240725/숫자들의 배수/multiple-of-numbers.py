n = int(input())
m = 1
a = []
while True:
    result = n*m
    print(result,end = ' ')
    m+=1
    if result % 5 == 0:
        a.append(result)
    if len(a) == 2:
        break