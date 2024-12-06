l = []
with open("d6big.txt", "r") as fin:
    lines = fin.readlines()
    for x in lines:
        l.append(list(x.strip()))

startI = 0
startJ = 0
for i in range(len(l)):
    for j in range(len(l[i])):
        if (l[i][j] == "^"):
            startI = i
            startJ = j

# part 1

i = startI
j = startJ
dirY = -1
dirX = 0
visited = set()
while ((i >= 0 and i < len(l)) and (j >= 0 and j < len(l[i]))):
    if (l[i][j] == "#"):
        # turn
        if (dirY == 0 and dirX == 1): # facing right
            i += 1 # go down
            j -= 1
            dirY = 1
            dirX = 0
        elif (dirY == 1 and dirX == 0): # facing down
            i -= 1 # go left
            j -= 1
            dirY = 0
            dirX = -1
        elif (dirY == -1 and dirX == 0): # facing up
            i += 1 # go right
            j += 1
            dirY = 0
            dirX = 1
        elif (dirY == 0 and dirX == -1): # facing left
            i += -1 # go up
            j += 1
            dirY = -1
            dirX = 0
    else:
        visited.add((i, j))
        # move forward
        i += dirY
        j += dirX

print(len(visited))

# part 2

def testLoop(i, j, dirY, dirX, blockI, blockJ):
    steps = 0
    while ((i >= 0 and i < len(l)) and (j >= 0 and j < len(l[i]))):
        if (steps > 10000):
            return True
        
        if ((i == blockI and j == blockJ) or l[i][j] == "#"):
            # turn
            if (dirY == 0 and dirX == 1): # facing right
                i += 1 # go down
                j -= 1
                dirY = 1
                dirX = 0
            elif (dirY == 1 and dirX == 0): # facing down
                i -= 1 # go left
                j -= 1
                dirY = 0
                dirX = -1
            elif (dirY == -1 and dirX == 0): # facing up
                i += 1 # go right
                j += 1
                dirY = 0
                dirX = 1
            elif (dirY == 0 and dirX == -1): # facing left
                i += -1 # go up
                j += 1
                dirY = -1
                dirX = 0
        else:
            # move forward
            i += dirY
            j += dirX
        steps += 1
    return False

uniquePos = set()
for pos in visited:
    if (testLoop(startI, startJ, -1, 0, pos[0], pos[1])):
        uniquePos.add((pos[0], pos[1]))

print(len(uniquePos))