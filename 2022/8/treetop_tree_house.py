with open('input.txt') as f:
    trees = f.readlines()

trees = [t.strip('\n') for t in trees]
trees = [[*t] for t in trees]

visible_trees = len(trees) * 4 - 4
max_score = 1

for i in range(1, len(trees) - 1):
    for j in range(1, len(trees) - 1):
        is_visible_L = True
        is_visible_R = True
        is_visible_U = True
        is_visible_D = True

        scenic_score = 1
        sight_R = 0
        sight_L = 0
        sight_U = 0
        sight_D = 0

        for k in range(j + 1, len(trees), 1):
            if trees[i][j] <= trees[i][k]:
                is_visible_R = False
                sight_R += 1
                break
            else:
                sight_R += 1
        for k in range(j - 1, -1, -1):
            if trees[i][j] <= trees[i][k]:
                is_visible_L = False
                sight_L += 1
                break
            else:
                sight_L += 1
        for k in range(i - 1, -1, -1):
            if trees[i][j] <= trees[k][j]:
                is_visible_U = False
                sight_U += 1
                break
            else:
                sight_U += 1
        for k in range(i + 1, len(trees), 1):
            if trees[i][j] <= trees[k][j]:
                is_visible_D = False
                sight_D += 1
                break
            else:
                sight_D += 1

        scenic_score = sight_R * sight_L * sight_U * sight_D

        if max_score < scenic_score:
            max_score = scenic_score
        scenic_score = 1

        if is_visible_U or is_visible_D or is_visible_L or is_visible_R == True:
            visible_trees += 1

print(visible_trees)
print(max_score)