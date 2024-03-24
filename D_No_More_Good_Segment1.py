n , s = map(int , input().split())

case1 = []
case2 = []
case1.append(int(input()))
case2.append(int(input()))
for i in range(n-2):
    gem = int(input())
    # difference between the gem and each elem of case 1 must be less or equal to s
    possible = True
    for elem in case1:
        if abs(gem - elem) > s:
            possible = False
            break
    if possible:
        case1.append(gem)
    else:
        p2 = True
        for elem in case2:
            if abs(gem - elem) > s:
                p2 = False
                break
        if p2:
            case2.append(gem)

print(len(case1)+len(case2))




