h, m = map(int, input().split())

if m - 45 < 0:
    m = 60 + (m - 45)
    h = h - 1
    if h < 0:
        h = 23
else:
    m = m - 45

print(h, m)
