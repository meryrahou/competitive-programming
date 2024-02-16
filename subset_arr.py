
def isSubset( a1, a2, n, m):
    a1set = set(a1)
    return 'Yes' if all (elem in a1set for elem in a2 ) else 'No'
    