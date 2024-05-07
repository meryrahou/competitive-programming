n = int(input())
dict = {}
for _ in range(n):
    name, phone = input().split()
    dict[name] = phone
    
try:
    while True:
        name = input()
        if name.lower() == 'exit':
            break  # Break the loop if 'exit' is entered
        elif name in dict:
            print(f"{name}={dict[name]}")
        else:
            print('Not found')
except EOFError:
    pass