with open('input.txt') as f:
    data = f.readlines()

data = [d.strip('\n').split() for d in data]

def move_tail(h, tails):
    more_than_one_tail = False

    if type(tails[0]) == list:
        more_than_one_tail = True

    if more_than_one_tail == True:
        head = h
        tail = tails[0]
    else:
        head = h
        tail = tails

    for i in range(len(tails)):
        if head == tail:
            return

        if head[0] - tail[0] == 2 and head[1] - tail[1] == 2:
            tail[0] += 1
            tail[1] += 1
        elif head[0] - tail[0] == 2 and tail[1] - head[1] == 2:
            tail[0] += 1
            tail[1] -= 1
        elif tail[0] - head[0] == 2 and head[1] - tail[1] == 2:
            tail[0] -= 1
            tail[1] += 1
        elif tail[0] - head[0] == 2 and tail[1] - head[1] == 2:
            tail[0] -= 1
            tail[1] -= 1
        elif head[0] - tail[0] == 2 and head[1] - tail[1] == 1:
            tail[0] += 1
            tail[1] += 1
        elif head[0] - tail[0] == 2 and tail[1] - head[1] == 1:
            tail[0] += 1
            tail[1] -= 1
        elif tail[0] - head[0] == 2 and head[1] - tail[1] == 1:
            tail[0] -= 1
            tail[1] += 1
        elif tail[0] - head[0] == 2 and tail[1] - head[1] == 1:
            tail[0] -= 1
            tail[1] -= 1
        elif head[0] - tail[0] == 1 and head[1] - tail[1] == 2:
            tail[0] += 1
            tail[1] += 1
        elif head[0] - tail[0] == 1 and tail[1] - head[1] == 2:
            tail[0] += 1
            tail[1] -= 1
        elif tail[0] - head[0] == 1 and head[1] - tail[1] == 2:
            tail[0] -= 1
            tail[1] += 1
        elif tail[0] - head[0] == 1 and tail[1] - head[1] == 2:
            tail[0] -= 1
            tail[1] -= 1
        elif head[0] - tail[0] == 2:
            tail[0] += 1
        elif tail[0] - head[0] == 2:
            tail[0] -= 1
        elif head[1] - tail[1] == 2:
            tail[1] += 1
        elif tail[1] - head[1] == 2:
            tail[1] -= 1

        if more_than_one_tail == True and i != (len(tails) - 1):
            tails[i] = tail
            head = tails[i]
            tail = tails[i + 1]
        elif i == (len(tails) - 1):
            tails[i] = tail
        else:
            return;

def move_rope(head, tail, t):
    for i in range(len(data)):
        if data[i][0] == 'R':
            for _ in range(int(data[i][1])):
                head[1] += 1
                move_tail(head, tail)
                visited_at_least_once.add(tuple(t))
        elif data[i][0] == 'L':
            for _ in range(int(data[i][1])):
                head[1] -= 1
                move_tail(head, tail)
                visited_at_least_once.add(tuple(t))
        elif data[i][0] == 'U':
            for _ in range(int(data[i][1])):
                head[0] += 1
                move_tail(head, tail)
                visited_at_least_once.add(tuple(t))
        elif data[i][0] == 'D':
            for _ in range(int(data[i][1])):
                head[0] -= 1
                move_tail(head, tail)
                visited_at_least_once.add(tuple(t))

# ---------- A ---------- #

head = [0, 0]
tail = [0, 0]
visited_at_least_once = set()
visited_at_least_once.add((0,0))

move_rope(head, tail, tail)
print(len(visited_at_least_once))

# ---------- B ---------- #

head = [0, 0]
tails = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
visited_at_least_once = set()
visited_at_least_once.add((0,0))

move_rope(head, tails, tails[-1])
print(len(visited_at_least_once))