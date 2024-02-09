n = int(input())
res = 0

for i in range(n):
    k = list(map(int, input().split()))
    if k[1] > k[0]:
        res = res + k[1] - k[0]

print(res)
