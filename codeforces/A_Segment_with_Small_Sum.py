n, s = map(int, input().split())

a = list(map(int, input().split()))

right = left = length = max_len = summ = 0

# while right < n:
#     if summ <= s:
#         length = max(length , right - left)
#         summ += a[right]
#         right += 1
#     else:
#         summ -= a[left]
#         left += 1

# # check for the last window
# if summ <= s:
#     length = max(length , right - left)    

# print(length)


for right in range(n):
    summ += a[right]

    while left < n and summ > s:
        summ -= a[left]
        left+= 1
  
    max_len = max( max_len , right - left + 1)

print(max_len)