l = []
with open("d4.txt", "r") as fin:
    lines = fin.readlines()
    for x in lines:
        l.append(list(x.strip()))

searchStr = "XMAS"
def dfsSearch(i, j, ind, dirX, dirY):
    if (ind >= len(searchStr)):
        return 0
    
    if (i < 0 or i >= len(l)):
        return 0
    elif (j < 0 or j >= len(l[i])):
        return 0
    elif (l[i][j] == searchStr[ind]):
        if (ind == len(searchStr) - 1):
            return 1

        return dfsSearch(i + dirX, j + dirY, ind + 1, dirX, dirY)
    
    return 0

# part 1
total = 0
for i in range(len(l)):
    for j in range(len(l[i])):
        total += dfsSearch(i, j, 0, -1, 0) # left
        total += dfsSearch(i, j, 0, 1, 0) # right
        total += dfsSearch(i, j, 0, 0, -1) # up
        total += dfsSearch(i, j, 0, 0, 1) # down

        total += dfsSearch(i, j, 0, -1, 1) # left up
        total += dfsSearch(i, j, 0, -1, -1) # left down
        total += dfsSearch(i, j, 0, 1, 1) # right up
        total += dfsSearch(i, j , 0, 1, -1) # right down

print(total)

# part 2

def verifyX_MAS(i, j):
    if (i < 1 or i >= len(l) - 1):
        return 0
    elif (j < 1 or j >= len(l[i]) - 1):
        return 0
    elif (l[i][j] == "A"):
        if (l[i - 1][j + 1] == "M" and l[i + 1][j - 1] == "S"):
            if (l[i - 1][j - 1] == "M" and l[i + 1][j + 1] == "S"):
                return 1
            elif (l[i - 1][j - 1] == "S" and l[i + 1][j + 1] == "M"):
                return 1
        elif (l[i - 1][j + 1] == "S" and l[i + 1][j - 1] == "M"):
            if (l[i - 1][j - 1] == "M" and l[i + 1][j + 1] == "S"):
                return 1
            elif (l[i - 1][j - 1] == "S" and l[i + 1][j + 1] == "M"):
                return 1
    
    return 0

# part 2
total2 = 0
for i in range(len(l)):
    for j in range(len(l[i])):
        total2 += verifyX_MAS(i, j)

print(total2)