n = list(map(int, input().split()))

compare = [1, 2, 3, 4, 5, 6, 7, 8]

if n == compare:
    print('ascending')
elif n == list(reversed(compare)):
    print('descending')
else:
    print('mixed')