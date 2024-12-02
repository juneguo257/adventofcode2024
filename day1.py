l1 = []
l2 = []
with open("d1.txt", "r") as fin:
    lines = fin.readlines()
    for x in lines:
        a1, b1 = x.strip().split()
        l1.append(int(a1))
        l2.append(int(b1))

l1.sort()
l2.sort()
similarityScore = 0
for i in range(len(l1)):
    c = 0
    for j in range(len(l2)):
        if (l1[i] == l2[j]):
            c += 1

    similarityScore += l1[i] * c

print(similarityScore)