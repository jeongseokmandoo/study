# import sys
# input = sys.stdin.readline

# n = int(input().strip())

# def count_func(n, count):
#     if n == 1:
#         print(count)
#         return
#     if n % 3 == 0:
#         count += 1
#         return count_func(n // 3, count)
#     elif n % 2 != 0 or (n - 1) % 3 == 0:
#         count += 1
#         return count_func(n - 1, count)
#     else:
#         count += 1
#         return count_func(n // 2, count)
        
# count_func(n, 0)

import sys
input = sys.stdin.readline

n = int(input().strip())

dp = [0] * (n + 1)

for i in range(2, n + 1):
    data_list = []
    data_list.append(dp[i - 1] + 1)
    if i % 2 == 0:
        data_list.append(dp[i // 2] + 1)
    if i % 3 == 0:
        data_list.append(dp[i // 3] + 1)
    
    dp[i] = min(data_list)

print(dp[n])