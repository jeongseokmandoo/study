N, M = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(M)]

package = list()
for i in range(M):
    package.append(info[i][0])
min_p = min(package)

extra = list()
for i in range(M):
    extra.append(info[i][1])
min_e = min(extra)

result = list()
result.append((N // 6 * min_p) + (N % 6 * min_e))
result.append((N // 6 + 1) * min_p)
result.append(N * min_e)

print(min(result))
