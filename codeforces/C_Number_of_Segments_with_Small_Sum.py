n, s = map(int, input().split())

a = list(map(int, input().split()))

# we check the sum and if it's > s we shrink
# else we grow the window if its it's <= s
left = summ = nb_seg = 0
for right in range(n):
    summ += a[right]

    while summ > s:
        summ -= a[left]
        left += 1
    
    nb_seg += right - left + 1

print(nb_seg)
