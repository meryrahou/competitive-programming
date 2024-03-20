# Read input
M, N = map(int, input().split())

# Calculate the total number of squares on the board
total_squares = M * N

# Calculate the maximum number of dominoes that can be placed
max_dominoes = total_squares // 2

# Output the result
print(max_dominoes)
