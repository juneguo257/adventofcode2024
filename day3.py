import re

# part 1

# regex: mul\(\d+,\d+\)
s1 = ""
with open("d3.txt", "r") as fin:
    lines = fin.readlines()
    s1 = "".join(lines)

p1matches = re.findall("mul\\((\\d+),(\\d+)\\)", s1)

total = 0
for x, y in p1matches:
    total += int(x) * int(y)

print(total)

# part 2

# regex: do\(\)|don't\(\)|mul\((\d+),(\d+)\)

p2matches = re.findall("do\\(\\)|don't\\(\\)|mul\\(\\d+,\\d+\)", s1)

total2 = 0
on = True
for match in p2matches:
    if (match == "do()"):
        on = True
    elif (match == "don't()"):
        on = False
    elif (on):
        x, y = re.findall("mul\\((\\d+),(\\d+)\\)", match)[0]
        total2 += int(x) * int(y)

print(total2)