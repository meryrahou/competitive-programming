from collections import defaultdict

n, k = map(int, input().split())
a = list(map(int, input().split()))

nb_seg = 0
seg = defaultdict(int)
left = 0

for right in range(n):
    seg[a[right]] += 1
    while max(seg.values()) >= k:
        nb_seg += n - right
        seg[a[left]] -= 1
        left += 1

print(nb_seg)
