def executeAction(quantity, start, end):
    for i in range(int(quantity)):
        crateToMove = stacks[int(start) - 1].pop()
        stacks[int(end) - 1].append(crateToMove)
    

def getSolution():
    result = ""

    for stack in stacks:
        result += stack[-1]
    
    return result

with open('input.txt') as file:
    lines = file.readlines()

stacks= [
            ['H', 'T', 'Z', 'D'],
            ['Q', 'R', 'W', 'T', 'G', 'C', 'S'],
            ['P', 'B', 'F', 'Q', 'N', 'R', 'C', 'H'],
            ['L', 'C', 'N', 'F', 'H', 'Z'],
            ['G', 'L', 'F', 'Q', 'S'],
            ['V', 'P', 'W', 'Z', 'B', 'R', 'C', 'S'],
            ['Z', 'F', 'J'],
            ['D', 'L', 'V', 'Z', 'R', 'H', 'Q'],
            ['B', 'H', 'G', 'N', 'F', 'Z', 'L', 'D']
        ]

for i in range(10, len(lines)):
    quantity = lines[i].split(' ')[1]
    start = lines[i].split(' ')[3]
    end = lines[i].split(' ')[5].strip(lines[i][-1])
    executeAction(quantity, start, end)

print(getSolution())