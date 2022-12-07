def isFullyContained(first, second):
    result = False

    startFirst = int(first.split('-')[0])
    endFirst = int(first.split('-')[1])

    startSecond = int(second.split('-')[0])
    endSecond = int(second.split('-')[1])

    if startFirst <= startSecond and endFirst >= endSecond:
        result = True
    elif startSecond <= startFirst and endSecond >= endFirst:
        result = True
    
    return result

with open('input.txt') as file:
    lines = file.readlines()

counter = 0

for line in lines:
    firstAssignment = line.split(',')[0]
    secondAssignment = line.split(',')[1].strip(line[-1])
    
    if isFullyContained(firstAssignment, secondAssignment):
        counter += 1
    
print(counter)