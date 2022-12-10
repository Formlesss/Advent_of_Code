with open('input.txt') as f:
    data = f.readlines()

data = [d.strip('\n') for d in data]

stacks = []
number_of_stacks = 0
line = 0

for j,d in enumerate(data):
    if any(char.isdigit() for char in d) == True:
        for c in d:
            if c.isdigit():
                number_of_stacks = int(c)
        line = j
        break

for _ in range(number_of_stacks):
    stacks.append([])

for d in data[:line]:
    nr = 0
    for i in range(len(d)):
        if i % 4 == 0:
            if d[i] == ' ':
                nr += 1
            elif d[i] == '[':
                stacks[nr].append(d[i+1])
                nr += 1
            else:
                stacks[nr].append(d[i])
                nr += 1

for d in data[line + 2:]:
    procedure = []

    for i in range(len(d)):
        if d[i].isdigit() == True:
                procedure.append(int(d[i]))

    if len(procedure) > 3:
        procedure[0] = int(str(procedure[0]) + str(procedure[1]))
        procedure.pop(1)

    for i in range(procedure[0],0 , -1):
        stack_to_move = stacks[procedure[1] - 1].pop(i-1)
        stacks[procedure[2] - 1].insert(0, stack_to_move)

result = [stacks[i][0] for i in range(number_of_stacks)]
print(''.join(result))
