import re
import math


file = open("5.txt", "r")
lines = file.readlines()

ids = []

for l in lines:
    lh = 0
    uh = 127
    rows = l[:7]
    col = l[7:]

    for c in rows:
        diff = (uh-lh) / 2
        if (c == "F"):
            uh = math.floor(uh-diff)
        elif (c == "B"):
            lh = math.ceil(lh + diff)

        # print(lh," : ",uh)

    if (lh == uh):
        rowNum = lh
        print("Row is: ", rowNum)

    lh = 0
    uh = 7
    for c in col:
        diff = (uh-lh) / 2
        if (c == "L"):
            uh = math.floor(uh-diff)
        elif(c == "R"):
            lh = math.ceil(lh+diff)
        # print(lh," : ",uh)

    if (lh == uh):
        colNum = lh
        print("Column is: ", colNum)

    id = (rowNum * 8) + colNum
    print("ID: ", id)
    ids.append(id)


print(max(ids))
