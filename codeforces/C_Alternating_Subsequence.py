testcases = int(input())

for _ in range(testcases):
    m = int(input())
    a = list(map(int , input().split()))

    s = 0
    ptr1 = 0
    pos = (a[0] > 0)
    while ptr1 < m:
        if pos:
            # Find the maximum positive 
            p = a[ptr1]
            while ptr1 < m and a[ptr1] > 0:
                p = max(p , a[ptr1])
                ptr1 += 1
            s += p
            pos = False
        else:
            # Find the minimum negative
            n = a[ptr1]
            while ptr1 < m and a[ptr1] < 0:
                n = max(n , a[ptr1])
                ptr1 += 1
            s += n
            pos = True
        
    print(s)