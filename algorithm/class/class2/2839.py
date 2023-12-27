n = int(input())

result = 0
a = 0
while True:
    if n < a * 5:
        result = -1
        break
    if (n % 5 + a * 5) % 3 == 0:
        result += (n // 5 - a) + (n % 5 + a * 5) // 3
        break
    a += 1

print(result)