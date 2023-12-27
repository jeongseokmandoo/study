import sys

m, n = map(int, sys.stdin.readline().strip().split())

for i in range(m, n + 1):
    condition = True
    if i == 2:
        print(i)
        continue
    if i % 2 == 0 or i == 1:
        continue
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            condition = False
            break   
    if condition:
        print(i)