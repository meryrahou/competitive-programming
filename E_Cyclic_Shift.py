rows , columns = map(int, input().split())
matrix = []
for _ in range(rows):
    row = input()
    if '1' not in row:
        print(-1)
        exit()
    else:
        matrix.append(row)

# count the max nums of 1s in a column
max_j = 0
for j in range(columns):
    count = sum(matrix[i][j] == '1' for i in range(rows))
    max_j = max(max_j, count)

# For each row that doesn't have 1 in the max_j columns, count how many shifts are needed to get 1
shifts = 0
for i in range(rows):
    if matrix[i][max_j] != '1':
        # Count number of shifts until we get 1
        # For that, we get the index of the first 1 we meet in the string
        # Then we check if that index is closer to 0 or to len(string)
        # Then we add that to shifts
        string = matrix[i]
        index = 0
        for t1 in range(len(string)):
            if string[t1] == '1':
                index = t1
                break
        shifts += min(index, len(string) - index)

print(shifts)