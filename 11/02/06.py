commands = {'write': 'W', 'read': 'R', 'execute': 'X'}
files = {}
for i in range(int(input())):
    file = input().split()
    files[file[0]] = file[1:]
for i in range(int(input())):
    command = input().split()
    if commands[command[0]] in files[command[1]]:
        print('OK')
    else:
        print('Access denied')
