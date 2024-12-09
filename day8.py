l1 = []
with open("d8.txt", "r") as fin:
    lines = fin.readlines()
    for x in lines:
        l1.append(list(x.strip()))

# part 1
antennas = {}
for i in range(len(l1)):
    for j in range(len(l1[i])):
        if l1[i][j] != ".":
            if (l1[i][j] in antennas):
                antennas[l1[i][j]].append((i, j))
            else:
                antennas[l1[i][j]] = [(i, j)]

c = 0
for antenna in antennas:
    positions = antennas[antenna]
    for i in range(len(positions)):
        for j in range(i+1, len(positions)):
            yDiff = positions[j][0] - positions[i][0]
            xDiff = positions[j][1] - positions[i][1]
            
            yPos1 = positions[i][0] - yDiff
            xPos1 = positions[i][1] - xDiff

            yPos2 = positions[j][0] + yDiff
            xPos2 = positions[j][1] + xDiff

            # upper #
            if (yPos1 >= 0 and yPos1 < len(l1)):
                if (xPos1 >= 0 and xPos1 < len(l1[i])):
                    if (l1[yPos1][xPos1] != "#"):
                        c += 1
                        l1[yPos1][xPos1] = "#"
            
            # lower #
            if (yPos2 >= 0 and yPos2 < len(l1)):
                if (xPos2 >= 0 and xPos2 < len(l1[i])):
                    if (l1[yPos2][xPos2] != "#"):
                        c += 1
                        l1[yPos2][xPos2] = "#"

print(c)

# part 2

for antenna in antennas:
    positions = antennas[antenna]
    for i in range(len(positions)):
        for j in range(i+1, len(positions)):
            yDiff = positions[j][0] - positions[i][0]
            xDiff = positions[j][1] - positions[i][1]

            # extend
            for k in range(10000): # arb limit
                yPos1 = positions[i][0] - k * yDiff
                xPos1 = positions[i][1] - k * xDiff

                # upper #
                if (yPos1 >= 0 and yPos1 < len(l1)):
                    if (xPos1 >= 0 and xPos1 < len(l1[i])):
                        if (l1[yPos1][xPos1] != "#"):
                            c += 1
                            l1[yPos1][xPos1] = "#"
                    else:
                        break
                else:
                    break
            
            # extend
            for k in range(10000): # arb limit
                yPos2 = positions[j][0] + k * yDiff
                xPos2 = positions[j][1] + k * xDiff
                
                # lower #
                if (yPos2 >= 0 and yPos2 < len(l1)):
                    if (xPos2 >= 0 and xPos2 < len(l1[i])):
                        if (l1[yPos2][xPos2] != "#"):
                            c += 1
                            l1[yPos2][xPos2] = "#"
                    else:
                        break
                else:
                    break

print(c)