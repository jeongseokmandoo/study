point = input()
col_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
row_list = ['1', '2', '3', '4', '5', '6', '7', '8']
x, y = col_list.index(point[0]) + 1, row_list.index(point[1]) + 1

if x >= 3 and x <= 6:
    if y >= 3 and y <=6:
        print(8)
    elif y == 2 or y == 7:
        print(6)
    else:
        print(4)
elif x == 2 and x == 2:
    if y >= 3 and y <=6:
        print(6)
    elif y == 2 or y == 7:
        print(4)
    else:
        print(3)
else:
    if y >= 3 and y <=6:
        print(4)
    elif y == 2 or y == 7:
        print(3)
    else:
        print(2)

# input_data = input()
# row = int(input_data[1])
# column = int(ord(input_data[0])) - int(ord('a')) + 1

# steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# result = 0
# for step in steps:
#     next_row = row + step[0]
#     next_column = column +  step[1]
#     if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
#         result += 1

# print(result)
