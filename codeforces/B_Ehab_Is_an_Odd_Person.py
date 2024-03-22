n = int(input())
a = list(map(int, input().split()))

verif = all(elem % 2 == 0 for elem in a) or all(elem % 2 != 0 for elem in a)

if verif:
    print(*a)
else:
    print(*sorted(a))
