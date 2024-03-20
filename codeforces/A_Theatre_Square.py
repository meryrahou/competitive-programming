import math

# Read input
n, m, a = map(int, input().split())

# Calculate the number of rows of flagstones needed
rows = math.ceil(n / a)

# Calculate the number of columns of flagstones needed
columns = math.ceil(m / a)

# Calculate the total number of flagstones needed
total_flagstones = rows * columns

# Output the result
print(total_flagstones)
