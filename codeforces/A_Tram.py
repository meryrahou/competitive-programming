n = int(input())

max = 0
p = 0

for _ in range(n):
    a, b = map(int, input().split())
    p = p - a + b
    if p > max:
        max = p

print(max)