h, m = map(int, input().split())
n = int(input())

m += n

m2 = m % 60
h2 = h + m // 60
if h2 > 23:
    h2 -= 24

print(h2, m2)