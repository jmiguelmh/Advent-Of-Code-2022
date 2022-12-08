def visibilityScore(map, i, j):
    value = map[i][j]

    up = 0
    down = 0
    left = 0
    right = 0

    for k in range(i-1, -1, -1):
        up += 1
        if map[k][j] >= value:
            break
    
    for k in range(i+1, len(map)):
        down += 1
        if map[k][j] >= value:
            break
    
    for k in range(j-1, -1, -1):
        left += 1
        if map[i][k] >= value:
            break
    
    for k in range(j+1, len(map[i])):
        right +=1
        if map[i][k] >= value:
            break

    return (up * down * left * right)

def bestVisibilityScore(map):
    result = 0

    for i in range(1, len(map)-1):
        for j in range(1, len(map[i])-1):
            score = visibilityScore(map, i, j)
            if score > result:
                result = score


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

print(bestVisibilityScore(map))