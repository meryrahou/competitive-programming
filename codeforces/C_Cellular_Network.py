n , m = map(int , input().split())

cities = list(map(int , input().split()))
towers = list(map(int , input().split()))

cities.sort()
towers.sort()

ptr_c = ptr_t = 0

'''
for each city , we get min distance from current tower or next tower
'''
r = 0

for ptr_c in range(n):
    while ptr_t < m - 1 and abs(cities[ptr_c] - towers[ptr_t + 1]) <= abs(cities[ptr_c] - towers[ptr_t]):
        ptr_t += 1
    r = max(r, abs(cities[ptr_c] - towers[ptr_t]))

print(r)
