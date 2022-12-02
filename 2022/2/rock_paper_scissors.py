with open('input.txt') as f:
    strategy = f.readlines()

strategy = [s.strip('\n').split() for s in strategy]

total_score = 0

for s in strategy:
    if s[1] == 'X':
        total_score += 0

        if s[0] == 'A':
            total_score += 3
        elif s[0] == 'B':
            total_score += 1
        else:
            total_score += 2

    elif s[1] == 'Y':
        total_score += 3

        if s[0] == 'A':
            total_score += 1
        elif s[0] == 'B':
            total_score += 2
        else:
            total_score += 3

    else:
        total_score += 6
    
        if s[0] == 'A':
            total_score += 2
        elif s[0] == 'B':
            total_score += 3
        else:
            total_score += 1

print(total_score)