from collections import deque
import sys

n = int(sys.stdin.readline().strip())

result = deque()

for i in range(n):
    command = list(sys.stdin.readline().strip().split())
    if command[0] == 'push_front':
        result.appendleft(int(command[1]))
    if command[0] == 'push_back':
        result.append(int(command[1]))
    if command[0] == 'pop_front':
        if len(result) == 0:
            print(-1)
        else:
            print(result.popleft())
    if command[0] == 'pop_back':
        if len(result) == 0:
            print(-1)
        else:
            print(result.pop())
    if command[0] == 'size':
        print(len(result))
    if command[0] == 'empty':
        if len(result) == 0:
            print(1)
        else:
            print(0)
    if command[0] == 'front':
        if len(result) == 0:
            print(-1)
        else:
            print(result[0])
    if command[0] == 'back':
        if len(result) == 0:
            print(-1)
        else:
            print(result[-1])
