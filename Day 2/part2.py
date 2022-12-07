def calculateScore(rival, me):
    if rival == 'A':
        if me == 'X':
            score = lose + scissors
        
        if me == 'Y':
            score = draw + rock
        
        if me == 'Z':
            score = win + paper
    
    if rival == 'B':
        if me == 'X':
            score = lose + rock
        
        if me == 'Y':
            score = draw + paper
        
        if me == 'Z':
            score = win + scissors
    
    if rival == 'C':
        if me == 'X':
            score = lose + paper
        
        if me == 'Y':
            score = draw + scissors
        
        if me == 'Z':
            score = win + rock

    return score

with open('input.txt') as file:
    lines = file.readlines()

win = 6
draw = 3
lose = 0

rock = 1
paper = 2
scissors = 3

totalScore = 0

for line in lines:
    rival = line.split(' ')[0]
    me = line.split(' ')[1].strip(line[-1])
    totalScore += calculateScore(rival, me)
    
print(totalScore)