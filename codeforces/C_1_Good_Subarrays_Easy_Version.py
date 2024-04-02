testcases = int(input())

for _ in range(testcases):
    n = int(input())
    a = list(map(int, input().split()))
    
    nb_good = 0
    left = 0
    '''
        we expand if bi >= i
        i? 
        shrink if the elem is less than the length of the subarr
    '''
    for right in range(n):
        while a[right] < (right - left + 1):
            left += 1

        nb_good += right - left + 1

    
    print(nb_good)
