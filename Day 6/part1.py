def validMarker(marker):
    result = True
    for i in range(4):
        for j in range(i+1, 4):
            if marker[i] == marker[j]:
                result = False
    
    return result

with open('input.txt') as file:
    lines = file.readlines()

buffer = lines[0][:-1]
position = -1

for i in range(len(buffer) - 3):
    marker = buffer[i:i+4]
    if validMarker(marker):
        position = i + 4
        break

print(position)