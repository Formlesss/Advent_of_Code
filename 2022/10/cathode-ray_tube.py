with open('input.txt') as f:
    data = f.readlines()

data = [d.strip('\n') for d in data]

x = 1
values = {}
cycles = 0
result = 0

for d in data:
    if d == 'noop':
        cycles += 1
    else:
        cycles += 2
        _, value = d.split()
        values[cycles + 1] = int(value)

crt_line = list(' ' * 40)
crt = ''
sprite = [1, 2, 3]

j = 1
for i in range(1, cycles + 1):
    old_x = x
    x += values.get(i, 0)

    if old_x != x:
        sprite = [x, x+1, x+2]

    if j in sprite:
        crt_line[j - 1] = '#'
    else:
        crt_line[j - 1] = '.'

    if i == 20:
        result += x * i

    if i >= 60 and i <= 220 and (i - 20) % 40 == 0:
        result += x * i

    if i % 40 == 0 and i <= 240:
        crt += ''.join(crt_line)
        crt_line = list(' ' * 40)
        j = 0

    j += 1

print(result)
print(crt[:40:])
print(crt[40:80:])
print(crt[80:120:])
print(crt[120:160:])
print(crt[160:200:])
print(crt[200:240:])