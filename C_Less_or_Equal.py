n , k = map(int , input().split())
a = list(map(int , input().split()))

a.sort()
if a[k-1] == a[k]:
    print(-1)
else:
    if a[k-1] + 1 >= 1 and a[k-1] + 1 <= 1000000000:
        print(a[k-1]+1)
    else:
        print(-1)