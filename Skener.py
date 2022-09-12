rows, columns, row_val, column_val = map(int,input().split())

matrix = []


for value in range(rows):
    temp_string = ""
    matrix = list(input())
    for char in range(len(matrix)):
            matrix[char] = matrix[char]*column_val
    for char in matrix:
        temp_string = temp_string + char
    for number in range(row_val):
        print(temp_string)
