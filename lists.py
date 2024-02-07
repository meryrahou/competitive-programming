if __name__ == '__main__':
    l = []
    N = int(input())
    for i in range(N):
        cmd, *args = input().split()
        
        if cmd == 'insert': 
            index, value = map(int, args)
            l.insert(index, value)
        if cmd == 'print':   print(l)
        if cmd == 'remove':  l.remove(int(args[0]))
        if cmd == 'append':  l.append(int(args[0]))
        if cmd == 'sort':    l.sort()
        if cmd == 'pop':     l.pop()
        if cmd == 'reverse': l.reverse()
