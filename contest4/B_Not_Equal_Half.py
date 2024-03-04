l = int(input())
array = list(map(int, input().split()))

array.sort()
if sum(array[:l//2]) > sum(array[l//2:]):
    print(-1)
else:
    print(*array)