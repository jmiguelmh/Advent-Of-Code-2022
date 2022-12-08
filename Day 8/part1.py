def isVisible(map, i, j):
    value = map[i][j]

    up = True
    down = True
    left = True
    right = True

    for k in range(i):
        if map[k][j] >= value:
            up = False
            break
    
    for k in range(i+1, len(map)):
        if map[k][j] >= value:
            down = False
            break
    
    for k in range(j):
        if map[i][k] >= value:
            left = False
            break
    
    for k in range(j+1, len(map[i])):
        if map[i][k] >= value:
            right = False
            break
    
    return (up or down or left or right)

def calculateVisibleTrees(map):
    result = 0

    # count trees from the interior
    for i in range(1, len(map)-1):
        for j in range(1, len(map[i])-1):
            if isVisible(map, i, j):
                result += 1

    # count surrounding trees
    result += 2 * len(map)
    result += 2 * (len(map[0]) - 2)

    return result

with open('input.txt') as file:
    lines = file.readlines()

map = []

for line in lines:
    trees = line[:-1]
    row = []
    for i in trees:
        row.append(int(i))
    
    map.append(row)

print(calculateVisibleTrees(map))