import sys
input = sys.stdin.readline

t = int(input().strip())

def count_func(arr, x, y, M, N):
    if arr[y][x] == 0:
        return
    arr[y][x] = 0
    
    if y + 1 < N and arr[y + 1][x] == 1:
        count_func(arr, x, y + 1, M, N)
    if y - 1 >= 0 and arr[y - 1][x] == 1:
        count_func(arr, x, y - 1, M, N)
    if x + 1 < M and arr[y][x + 1] == 1:
        count_func(arr, x + 1, y, M, N)
    if x - 1 >= 0 and arr[y][x - 1] == 1:
        count_func(arr, x - 1, y, M, N)
    return
    

for _ in range(t):
    M, N, K = map(int, input().strip().split())
    data_list = [[0] * M for _ in range(N)]
    
    for _ in range(K):
        X, Y = map(int, input().strip().split())
        data_list[Y][X] = 1
        
    count = 0
    for i in range(M):
        for j in range(N):
            if data_list[j][i] == 1:
                count += 1
                count_func(data_list, i, j, M, N)
    print(count)
