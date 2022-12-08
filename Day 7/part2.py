from pathlib import Path

def calculateDirSize(path):
    totalSize = 0

    for object in dirTree[path]:
        if isinstance(object, tuple):
            totalSize += object[0]
        
        elif isinstance(object, Path):
            totalSize += calculateDirSize(object)
    
    return totalSize

def getDirSizes():
    return {dir: calculateDirSize(dir) for dir in dirTree}

pointer = Path("")
dirTree = {}

with open('input.txt') as file:
    lines = file.readlines()

for line in lines:
    instruction = line[:-1].split(' ')
    
    if instruction[0] == '$' and instruction[1] == "cd":
        if instruction[2] == "..":
            pointer = pointer.parent
        else:
            pointer = pointer / instruction[2]
            if pointer not in dirTree:
                dirTree[pointer] = []
                
    elif instruction[0] == "dir":
        dirTree[pointer].append(pointer / instruction[1])

    elif instruction[0].isnumeric():
        dirTree[pointer].append((int(instruction[0]), instruction[1]))

dirSizes = getDirSizes()
totalSpace = 70000000
neededSpace = 30000000
spaceUsed = dirSizes[Path("/")]
spaceToClear = neededSpace - (totalSpace - spaceUsed)
dirToClear = next(iter(dirSizes.items()))[1]

for dir in dirSizes:
    if dirSizes[dir] >= spaceToClear and dirSizes[dir] < dirToClear:
        dirToClear = dirSizes[dir]

print(dirToClear)