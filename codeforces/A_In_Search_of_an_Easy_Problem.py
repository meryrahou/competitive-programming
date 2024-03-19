n = int(input())
k = list(map(int, input().split()))

print( 'EASY' if sum(k) == 0 else 'HARD')