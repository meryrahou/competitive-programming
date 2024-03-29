n , m = map(int , input().split())
a = list(map(int , input().split()))
b = list(map(int , input().split()))

ptr_a = ptr_b = 0

nb_pair = 0

while ptr_a < n-1 and ptr_b < m-1:
    if a[ptr_a] == b[ptr_b]:
        nb_pair += 1
        # increment the one that has less value in next iteration
        if ptr_a < n-1 and ptr_b < m-1 and a[ptr_a+1] < b[ptr_b+1]:
            ptr_a += 1
        else:
            ptr_b += 1
    if a[ptr_a] < b[ptr_b]:
        ptr_a += 1
    if a[ptr_a] > b[ptr_b]:
        ptr_b += 1

print(nb_pair)
