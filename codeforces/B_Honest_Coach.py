testcase = int(input())

for _ in range(testcase):
    n = int(input())
    s = list(map(int, input().split()))
    s.sort()
    
    min_difference = float('inf')
    
    for i in range(1, n):
        difference = abs(s[i] - s[i - 1])
        min_difference = min(min_difference, difference)
    
    print(min_difference)
