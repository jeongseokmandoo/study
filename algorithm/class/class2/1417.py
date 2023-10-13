n = int(input())
ds = int(input())
can = list(int(input()) for _ in range(n - 1))

can.sort(reverse=True)
result = 0

while True:
    if n == 1 or ds > can[0]:
        print(result)
        break
    if ds <= can[0]:
        ds += 1
        can[0] -= 1
        result += 1
        can.sort(reverse=True)

