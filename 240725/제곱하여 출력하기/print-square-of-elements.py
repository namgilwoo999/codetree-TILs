n = int(input())

arr = list(map(int,input().split()))

list_ = [i**2 for i in arr]

print(f'{list_[0]} {list_[1]} {list_[2]}')