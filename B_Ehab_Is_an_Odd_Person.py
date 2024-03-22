n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    for j in range(i + 1, n):
        if a[i] > a[j] and a[i]+a[j] % 2 != 0:
            a[i], a[j] = a[j], a[i]

print(*a)