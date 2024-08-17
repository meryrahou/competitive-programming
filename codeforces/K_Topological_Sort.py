from collections import defaultdict

t = int(input())

for _ in range(t):
    n, m = map( int, input().split())
    graph = defaultdict(set)

    for _ in range(m):
        u, v = map(int, input().split())
        graph[v].add(u)

    ans = [i for i in range(1,n+ 1)]
    for i in range(1, n+ 1):
        left = i - 2 
        while left >= 0 :
            if ans[left] in graph[i]:
                ans[left], ans[left+ 1] = ans[left+ 1], ans[left]
                left -= 1
            else:
                break

    print(*ans) 