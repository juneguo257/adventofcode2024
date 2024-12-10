import copy

with open("d9big.txt", "r") as fin:
    x = fin.readline().strip()

numbers = []
spaces = []

# part 1
c = 0
for i in range(len(x)):
    if (c % 2 == 0):
        numbers.append([c // 2, int(x[i])])
        c += 1
    else:
        spaces.append([-1, int(x[i])])
        c += 1

# build str
listBuildStr = []
p1 = 0
p2 = 0
curNumbers = True
while (p1 < len(numbers) or p2 < len(spaces)):
    if (curNumbers):
        listBuildStr += [str(numbers[p1][0])] * numbers[p1][1]
        p1 += 1
        curNumbers = False
    else:
        listBuildStr += ["."] * spaces[p2][1]
        p2 += 1
        curNumbers = True

print(listBuildStr)

cpListBuildStr = copy.copy(listBuildStr) # for part 2

# swap "."
p1 = 0
p2 = len(listBuildStr) - 1
while (p1 < p2):
    if (listBuildStr[p1] != "."):
        p1 += 1
    elif (listBuildStr[p2] == "."):
        p2 -= 1
    elif (listBuildStr[p1] == "." and listBuildStr[p2] != "."):
        listBuildStr[p1] = listBuildStr[p2]
        listBuildStr[p2] = "."
        p2 -= 1
        p1 += 1

print(listBuildStr)

# get checksum
checksum = 0
for i in range(len(listBuildStr)):
    if (listBuildStr[i] == "."):
        break
    checksum += int(listBuildStr[i]) * i

print(checksum)

# part 2

listBuildStr = cpListBuildStr
# swap "." part 2
p2 = len(listBuildStr) - 1

while (p2 >= 0):
    # print("".join(list(map(str, listBuildStr))))

    if (listBuildStr[p2] == "."):
        p2 -= 1
    else:
        # listBuildStr[p1] == "." and listBuildStr[p2] != "."
        numCount = 0
        for i in range(p2, -1, -1):
            if (listBuildStr[i] == listBuildStr[p2]):
                numCount += 1
            else:
                break

        ifUpdated = False
        for i in range(0, p2):
            pdCount = 0 # period count
            for j in range(i, p2):
                if (listBuildStr[j] == "."):
                    pdCount += 1
                else:
                    break
            
            if (numCount <= pdCount):
                p1 = i
                for k in range(numCount):
                    listBuildStr[p1] = listBuildStr[p2]
                    listBuildStr[p2] = "."
                    p2 -= 1
                    p1 += 1
                ifUpdated = True
                break
        
        if (not ifUpdated):
            p2 -= numCount

# get checksum
checksum = 0
for i in range(len(listBuildStr)):
    if (listBuildStr[i] != "."):
        checksum += int(listBuildStr[i]) * i

print(checksum)