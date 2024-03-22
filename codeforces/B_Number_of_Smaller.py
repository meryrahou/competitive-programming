n , m = map(int , input().split())
a = list(map(int , input().split()))
b = list(map(int , input().split()))

res = []

ptr_a = 0
for elem in b:
    count = ptr_a
    while ptr_a < n and a[ptr_a] < elem:
        count += 1
        ptr_a += 1
    res.append(count)

print(*res)