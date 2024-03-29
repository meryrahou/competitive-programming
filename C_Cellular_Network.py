n , m = map(int , input().split())

cities = list(map(int , input().split()))
towers = list(map(int , input().split()))

cities.sort()
towers.sort()

ptr_c = ptr_t = 0

'''
for each city , we get min distance from current tower or next tower
'''
r = cities[0]
while ptr_t < m and ptr_c < n:
    diff1 = abs(cities[ptr_c] - towers[ptr_t])
    diff2 = abs(cities[ptr_c] - towers[ptr_t+1]) if ptr_t < m-1 else float('inf')

    print(diff1 , diff2 , r , ptr_c , ptr_t)
    if diff1 < diff2:
        ptr_c += 1
        r = max(r , diff1)
    else:
        r = max(r , diff2)
        ptr_t += 1
        ptr_c += 1




print(r)