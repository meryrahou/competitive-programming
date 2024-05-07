if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

l = []
r = 0
for i in arr:
    if i not in l:
        l.append(i)

l.sort()
print(l[-2])
