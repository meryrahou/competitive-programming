from collections import deque


s = input().strip()


t = deque()
u = []

frequency = [0] * 26

for char in s:
    frequency[ord(char) - ord('a')] += 1

def smallest_char_index(frequency):
    for i in range(26):
        if frequency[i] > 0:
            return i
    return -1


for char in s:
    t.append(char)
    frequency[ord(char) - ord('a')] -= 1
    
    while t and ord(t[-1]) - ord('a') <= smallest_char_index(frequency):
        u.append(t.pop())

print(''.join(u))