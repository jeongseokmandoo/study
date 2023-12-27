n = int(input())
num = list(map(int, input().split()))

result = 0
for i in num:
    div = 0
    divisor = i
    while divisor > 0:
        if i % divisor == 0:
            div += 1
        if div > 2:
            break
        divisor -= 1
    if div == 2:
        result += 1

print(result)