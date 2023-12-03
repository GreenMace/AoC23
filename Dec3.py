from aoccommon import *

def compFunc(elem):
    return elem.isdigit()

with open('Dec3_input.txt') as f:
    lines = f.readlines()

    output1 = 0
    output2 = 0

    m = []
    for line in lines:
        m.append(line.strip())

    for y, line in enumerate(lines):
        skip = 0
        for x, v in enumerate(line):
            if skip:
                skip -=1
                continue

            if v.isdigit():
                neighbours = getNeighbours(m, y, x, diagonal=True)
    
                for neigh in neighbours:
                    val = lines[neigh[0]][neigh[1]]
                    if not val.isdigit() and val != ".":
                        num, start, end = completeFromList(line, x, compFunc = compFunc)
                        
                        output1 += int(num)
                        skip = end-x
                        break

    for y in range(len(lines)):
        for x, v in enumerate(lines[y]):
            if v == "*":
                adjacentNums = []

                neighbours = getNeighbours(m, y, x, diagonal=True)
                i = 0
                while i < len(neighbours):
                    neigh = neighbours[i]
                    line = lines[neigh[0]]
                    val = line[neigh[1]]
                    if val.isdigit():
                        num, start, end = completeFromList(line, neigh[1], compFunc = compFunc)

                        for x in range(start, end+1):
                            if [neigh[0], x] in neighbours:
                                neighbours.remove([neigh[0], x])
                                
                        adjacentNums.append(int(num))
                    else:
                        i += 1

                if len(adjacentNums) == 2:
                    output2 += adjacentNums[0]*adjacentNums[1]
                


    print("Part1:", output1)
    print("Part2:", output2)