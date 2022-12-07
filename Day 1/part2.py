with open('input.txt') as file:
    lines = file.readlines()

totalCalories = []
sumOfCalories = 0

for line in lines:
    if (line != '\n'):
        sumOfCalories += int(line)
    else:
        totalCalories.append(sumOfCalories)
        sumOfCalories = 0

totalCalories.sort()

print(totalCalories[-1] + totalCalories[-2] + totalCalories[-3])