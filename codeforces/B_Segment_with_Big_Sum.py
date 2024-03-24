n, s = map(int, input().split())

a = list(map(int, input().split()))

left = right = summ = 0
min_len = float('inf')

'''  
    if summ < s
        we add to the segment
    if it's summ >= s
        check if it's the shortest segment
        then shrink it

    we shrink if when 
    we remove an elem from seg
    we decrease the summ , 
    the summ stays greater than s
'''

# while right < n:
#     if summ < s:
#         summ += a[right]
#         right += 1
#     else:
#         min_len = min(min_len , right - left)
#         summ -= a[left]
#         left += 1

# while summ >= s:
#     min_len = min(min_len , right - left)
#     summ -= a[left]
#     left += 1
# print(min_len)

for right in range(n):
    summ += a[right]
    while summ >= s:
        min_len = min(min_len, right - left+1)
        summ -= a[left]
        left += 1

if min_len == float('inf'):
    print(-1)
else:
    print(min_len)

