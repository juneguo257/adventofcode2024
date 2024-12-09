l1 = []
l2 = []
with open("d7big.txt", "r") as fin:
    lines = fin.readlines()
    for x in lines:
        splitX = x.strip().split(": ")
        l1.append(int(splitX[0]))
        l2.append(list(map(int, splitX[1].split())))

# brute force soln to parts 1 & 2
sumTestValues = 0
for i in range(len(l2)):
    possibilitiesStack = []
    possibilitiesStack.append(l2[i][0])
    for j in range(1, len(l2[i])):
        tmpStack = []
        while (len(possibilitiesStack) > 0):
            curEle = possibilitiesStack.pop()
            tmpStack.append(curEle * l2[i][j])
            tmpStack.append(curEle + l2[i][j])

            leftShift = 0
            nextNum = l2[i][j]
            while (nextNum > 0):
                nextNum = nextNum // 10
                leftShift += 1
            tmpStack.append((curEle * (10 ** leftShift)) + l2[i][j])
        possibilitiesStack = tmpStack
    
    if (l1[i] in possibilitiesStack):
        sumTestValues += l1[i]

print(sumTestValues)