import sys
input = sys.stdin.readline

def square(arr, n, count):
    if n == 1:
        if arr[0][0] == 0:
            count[0] += 1
        else:
            count[1] += 1
        return

    if all(arr[i][j] == 0 for i in range(n) for j in range(n)):
        count[0] += 1
        return
    if all(arr[i][j] == 1 for i in range(n) for j in range(n)):
        count[1] += 1
        return

    half_n = n // 2
    square([row[:half_n] for row in arr[:half_n]], half_n, count)
    square([row[half_n:] for row in arr[:half_n]], half_n, count)
    square([row[:half_n] for row in arr[half_n:]], half_n, count)
    square([row[half_n:] for row in arr[half_n:]], half_n, count)

n = int(input().strip())
arr = [list(map(int, input().strip().split())) for _ in range(n)]
count = [0, 0]

square(arr, n, count)
print(count[0])    
print(count[1])
