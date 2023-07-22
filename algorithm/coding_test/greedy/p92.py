n, m, k = map(int, input().split())
num = list(map(int, input().split()))

num.sort(reverse=True)

result = 0
i = 0
kk = 0
mm = 0

while i < m:
    if mm == m:
        break
    if kk < k:
        result += num[0]
        kk += 1
    else:
        result += num[1]
        kk = 0
    mm += 1

print(result)