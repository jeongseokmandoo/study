import sys
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    dp_list = [0] * (n + 1)
    if n == 1:
        print(1)
        continue
    if n == 2:
        print(2)
        continue
    if n == 3:
        print(4)
        continue
    dp_list[1] = 1
    dp_list[2] = 2
    dp_list[3] = 4
    cnt = 0
    for i in range(4, n + 1):
        dp_list[i] = dp_list[i - 1] + dp_list[i - 2] + dp_list[i - 3]
    print(dp_list[n])
