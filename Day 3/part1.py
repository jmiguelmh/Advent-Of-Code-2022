def priority(letter):
    result = ord(letter)

    if result > 96 and result < 123:
        result -= 96
    else:
        result -= 38

    return result

def sameCharacter(first, second):
    result = 0

    for i in range(len(first)):
        if first[i] in second:
            result = priority(first[i])

    return result

with open('input.txt') as file:
    lines = file.readlines()

sumOfPriorities = 0

for line in lines:
    items = line.rstrip(line[-1])
    firstItem = items[:len(items)//2]
    secondItem = items[len(items)//2:]
    sumOfPriorities += sameCharacter(firstItem, secondItem)

print(sumOfPriorities)