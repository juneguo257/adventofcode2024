import copy

d1 = {} # in-degree
d2 = {} # out-degree
l2 = []
readL1 = True
with open("d5.txt", "r") as fin:
    lines = fin.readlines()
    for x in lines:
        if (x.strip() == ""):
            readL1 = False
        elif (readL1):
            y, z = x.strip().split("|")
            y = int(y)
            z = int(z)
            if (z in d1):
                d1[z].append(y)
            else:
                d1[z] = [y]

            if (y in d2):
                d2[y].append(z)
            else:
                d2[y] = [z]
        else:
            l2.append(list(map(int, x.strip().split(","))))

# part 1

curVisited = set()
midSum = 0
part2 = []
for i in range(len(l2)):
    verified = True
    for j in range(len(l2[i])):
        if (l2[i][j] in curVisited):
            verified = False
            break

        if (l2[i][j] in d1):
            for x in d1[l2[i][j]]:
                curVisited.add(x)

    if (verified):
        midSum += l2[i][len(l2[i]) // 2]
    else:
        part2.append(l2[i])
    curVisited = set()

# print(midSum)
print(part2)

# part 2

visited = set()
midSum2 = 0

def topoSort(visited, curNodes, curNode):
    visited.add(curNode)

    if (curNode not in d2):
        return [curNode]
    
    res = []
    for node in d2[curNode]:
        if (node in curNodes and node not in visited):
            res = topoSort(visited, curNodes, node) + res
    
    res.insert(0, curNode)
    return res

midSum2 = 0
for i in range(len(part2)):
    res2 = []
    visited = set()
    nodes = set()
    for j in range(len(part2[i])):
        nodes.add(part2[i][j])

    for j in range(len(part2[i])):
        if (part2[i][j] not in visited):
            res2 = topoSort(visited, nodes, part2[i][j]) + res2

    midSum2 += res2[len(res2) // 2]

print(midSum2)
