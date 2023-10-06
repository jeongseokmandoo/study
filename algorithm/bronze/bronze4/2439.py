n = int(input())

for i in range(1, n + 1):
    m = n - i
    result = ' ' * m + '*' * i
    print(result)
