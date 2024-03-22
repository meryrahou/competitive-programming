n = int(input())
a = list(map(int, input().split()))

# check if all the elememnts are even or all the elements are odd 
verif = (a[0] % 2 == 0 ) # check if the first element is even or odd
for elem in a:
    if elem % 2 != 0:
        verif = False
        break

if verif:
    print(*a)
else:
    print(*sorted(a))
