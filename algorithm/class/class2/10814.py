import sys
input = sys.stdin.readline
output = sys.stdout.write

n = int(input().strip())
data_list = [tuple(input().strip().split()) for _ in range(n)]

data_list.sort(key=lambda x: int(x[0]))

print('\n'.join(f"{x} {y}" for x, y in data_list))