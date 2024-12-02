l1 = []
with open("d2.txt", "r") as fin:
    lines = fin.readlines()
    for x in lines:
        l1.append(list(map(int, x.strip().split())))

c = 0
for i in range(len(l1)):
    prev = l1[i][0]
    incr = (l1[i][1] - prev > 0)
    tolerance = 0
    for j in range(1, len(l1[i])):
        if (l1[i][j] - prev) > 0 and not incr:
            tolerance += 1
            continue
        elif (l1[i][j] - prev) < 0 and incr:
            tolerance += 1
            continue
        elif (l1[i][j] - prev) == 0:
            tolerance += 1
            continue

        if (l1[i][j] - prev > 3 and incr):
            tolerance += 1
            continue
        elif (l1[i][j] - prev < -3 and not incr):
            tolerance += 1
            continue

        prev = l1[i][j]
    
    # same code, but remove 1st element

    prev = l1[i][1]
    incr = (l1[i][2] - prev > 0)
    tolerance2 = 0
    for j in range(2, len(l1[i])):
        if (l1[i][j] - prev) > 0 and not incr:
            tolerance2 += 1
            continue
        elif (l1[i][j] - prev) < 0 and incr:
            tolerance2 += 1
            continue
        elif (l1[i][j] - prev) == 0:
            tolerance2 += 1
            continue

        if (abs(l1[i][j] - prev) > 3):
            tolerance2 += 1
            continue

        prev = l1[i][j]
    
    # same code, but remove 2nd element

    prev = l1[i][0]
    incr = (l1[i][2] - prev > 0)
    tolerance3 = 0
    for j in range(2, len(l1[i])):
        if (l1[i][j] - prev) > 0 and not incr:
            tolerance3 += 1
            continue
        elif (l1[i][j] - prev) < 0 and incr:
            tolerance3 += 1
            continue
        elif (l1[i][j] - prev) == 0:
            tolerance3 += 1
            continue

        if (abs(l1[i][j] - prev) > 3):
            tolerance3 += 1
            continue

        prev = l1[i][j]
    
    if (tolerance <= 1 or tolerance2 == 0 or tolerance3 == 0):
        c += 1

print(c)