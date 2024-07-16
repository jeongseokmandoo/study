import sys
input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    if n == 0 :
        print(0)
        continue
    clothes_dict = {}
    for _ in range(n):
        name, kind = input().strip().split()
        if kind in clothes_dict:
            clothes_dict[kind] += 1
        else:
            clothes_dict[kind] = 1
    
    count = 1
    for key in clothes_dict:
        count *= clothes_dict[key] + 1
    
    print(count - 1)
