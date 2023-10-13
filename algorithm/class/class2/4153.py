while True:
    n = list(map(int, input().split()))
    m = max(n)
    if m == 0:
        break
    n.remove(m)
    if m ** 2 == n[0] ** 2 + n[1] ** 2:
        print('right')
    else:
        print('wrong')