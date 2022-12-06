with open('input.txt') as f:
    data = f.readlines()

data = [d.strip('\n').split(',') for d in data]
data = [d.split('-') for i in data for d in i]

def part_one():
    pairs_fully_contain = 0

    for j,d in enumerate(data):
        if j % 2 == 0:
            s_1 = set(i for i in range(int(d[0]), int(d[1]) + 1))
        else:
            s_2 = set(i for i in range(int(d[0]), int(d[1]) + 1))
        
            if s_1.issubset(s_2) or s_2.issubset(s_1):
                pairs_fully_contain += 1
    return pairs_fully_contain

def part_two():
    pairs_overlap_at_all = 0

    for j,d in enumerate(data):
        if j % 2 == 0:
            s_1 = set(i for i in range(int(d[0]), int(d[1]) + 1))
        else:
            s_2 = set(i for i in range(int(d[0]), int(d[1]) + 1))
        
            if s_1.isdisjoint(s_2) == False:
                pairs_overlap_at_all += 1
    return pairs_overlap_at_all

print(part_one())
print(part_two())
