n, m = map(int, input().split())
board = list(input() for _ in range(n))

t_n = n - 7
t_m = m - 7

result = list()

for i in range(t_n):
    for j in range(t_m):
        d1 = 0
        d2 = 0

        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if (k + j) % 2 == 0:
                    if board[k][j] == 'B':
                        d2 += 1
                    else:
                        d1 += 1
                else:
                    if board[k][j] == 'W':
                        d2 += 1
                    else:
                        d1 += 1
        result.append(min(d1, d2))

print(min(result))

