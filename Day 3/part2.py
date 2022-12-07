def priority(letter):
    result = ord(letter)

    if result > 96 and result < 123:
        result -= 96
    else:
        result -= 38

    return result

def sameCharacter(first, second, third):
    result = 0

    for i in range(len(first)):
        if first[i] in second and first[i] in third:
            result = priority(first[i])
            break

    return result

with open('input.txt') as file:
    lines = file.readlines()

sumOfPriorities = 0

for i in range(0, len(lines), 3):
    firstItem = lines[i]
    secondItem = lines[i+1]
    thirdItem = lines[i+2]
    sumOfPriorities += sameCharacter(firstItem, secondItem, thirdItem)

print(sumOfPriorities)