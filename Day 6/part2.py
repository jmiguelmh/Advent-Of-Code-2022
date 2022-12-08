def validMarker(marker):
    result = True
    for i in range(14):
        for j in range(i+1, 14):
            if marker[i] == marker[j]:
                result = False
    
    return result

with open('input.txt') as file:
    lines = file.readlines()

buffer = lines[0][:-1]
position = -1

for i in range(len(buffer) - 13):
    marker = buffer[i:i+14]
    if validMarker(marker):
        position = i + 14
        break

print(position)