import sys
input = sys.stdin.readline
output = sys.stdout.write

n = int(input().strip())

n_list = [tuple(map(int, input().strip().split())) for _ in range(n)]

n_list.sort(key=lambda x: (x[1], x[0]))

output('\n'.join(f"{x} {y}" for x, y in n_list) + '\n')