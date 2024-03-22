n , m = map(int , input().split())

a = list(map(int , input().split()))
b = list(map(int , input().split()))

ptr_a , ptr_b = 0 , 0

res = []
while ptr_a < n and ptr_b < m:
    if a[ptr_a] < b[ptr_b]:
        res.append(a[ptr_a])
        ptr_a += 1
    else:
        res.append(b[ptr_b])
        ptr_b += 1

if ptr_a < n:
    res.extend(a[ptr_a:])
else:
    res.extend(b[ptr_b:])

print(*res)