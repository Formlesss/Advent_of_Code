from string import ascii_lowercase

with open('input.txt') as f:
    rucksacks = f.readlines()

priorities = dict()
for i,j in enumerate(ascii_lowercase):
    priorities[j] = i + 1
    priorities[j.upper()] = i + 27

rucksacks = [r.strip('\n') for r in rucksacks]

same_occurences  = [set(rucksacks[i]).intersection(rucksacks[i+1], rucksacks[i+2]) for i in range(0,len(rucksacks) - 2,3)]

sum_of_priorities = 0
for s in same_occurences:
    for i in s:
        sum_of_priorities += priorities[i]

print(sum_of_priorities)