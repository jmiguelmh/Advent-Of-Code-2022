def isContained(first, second):
    result = False

    startFirst = int(first.split('-')[0])
    endFirst = int(first.split('-')[1])

    startSecond = int(second.split('-')[0])
    endSecond = int(second.split('-')[1])

    firstAssignment = [*range(startFirst, endFirst + 1)]
    secondAssignment = [*range(startSecond, endSecond + 1)]

    for assignment in firstAssignment:
        if assignment in secondAssignment:
            result = True
            break
    
    return result

with open('input.txt') as file:
    lines = file.readlines()

counter = 0

for line in lines:
    firstAssignment = line.split(',')[0]
    secondAssignment = line.split(',')[1].strip(line[-1])
    
    if isContained(firstAssignment, secondAssignment):
        counter += 1
    
print(counter)