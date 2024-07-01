n = int(input())
A = list(map(int, input().split()))
A.sort

m = int(input())
M = list(map(int, input().split()))
M.sort

for i in M:
    if i in A:
        print(1)
    else:
        print(0)
         