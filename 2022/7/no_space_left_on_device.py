with open('input.txt') as f:
    data = f.readlines()

data = [d.strip('\n') for d in data]

current_dir = None
directories = {}
directory_size = {}
subdirectories = []

for j, d in enumerate(data):
    if d[0] == '$':
        c = d.strip('$')
        command, *args = c.split()

        if command == 'cd':
            if args[0] == '/':
                current_dir = '/'
                if current_dir not in directories:
                    directories[current_dir] = []
                    directory_size[current_dir] = 0
            elif args[0] == '..':
                for subdir in directories.values():
                    for s in subdir:
                        if s == current_dir:
                            current_dir = list(directories.keys())[list(directories.values()).index(subdir)]
            else:
                current_dir = args[0]
                subdirectories = []

        elif command == 'ls':
            for i in data[j + 1:]:
                if i[0] == '$':
                    directories[current_dir] = subdirectories
                    break
                elif i[0] == 'd':
                    _, dir_name = i.split()
                    directories[dir_name] = []
                    directory_size[dir_name] = 0
                    subdirectories.append(dir_name)
                else:
                    size, filename = i.split()
                    directory_size[current_dir] += int(size)

                directories[current_dir] = subdirectories

def adjust_size(name):
    for v in directories[name]:
        if directories[v] == []:
            directory_size[name] += directory_size[v]
        else:
            adjust_size(v)
            directory_size[name] += directory_size[v]

def sum_1():
    sum = 0
    for k in directory_size.keys():
        if directory_size[k] <= 100000:
            sum += directory_size[k]
    return sum

adjust_size('/')
print(sum_1())

