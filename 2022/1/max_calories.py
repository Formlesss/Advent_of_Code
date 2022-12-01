with open('input.txt') as f:
    calories = f.readlines()

calories = [c.rstrip('\n') for c in calories]

result = 0
sum_calories = 0
elf = 0
calories_list = []

for c in calories:
    if c == '':
        elf += 1
        calories_list.append(sum_calories)
        sum_calories = 0
    else:
        sum_calories += int(c)

calories_list.sort(reverse=True)
top = calories_list[0]
top_three = calories_list[0] + calories_list[1] + calories_list[2]

print(top)
print(top_three)