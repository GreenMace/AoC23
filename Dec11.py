from aoccommon import *

def solve(test: bool = False):
    lines = getInput(test)

    output1 = 0
    output2 = 0

    filledRows = set()
    filledColumns = set()
    galaxies = []
    for y, line in enumerate(lines):
        for x, val in enumerate(line):
            if val == "#":
                galaxies.append([y, x])
                filledColumns.add(x)
                filledRows.add(y)

    for i, galaxy in enumerate(galaxies):
        for other in galaxies[i+1:]:
            minY = min(galaxy[0], other[0])
            minX = min(galaxy[1], other[1])

            maxY = max(galaxy[0], other[0])
            maxX = max(galaxy[1], other[1])

            output1 +=  maxX - minX + maxY - minY + sum(1 for elem in range(minX, maxX) if  elem not in filledColumns) + \
                                        sum(1 for elem in range(minY, maxY) if  elem not in filledRows)

            output2 += maxX - minX + maxY - minY + sum(999999 for elem in range(minX, maxX) if  elem not in filledColumns) + \
                                        sum(999999 for elem in range(minY, maxY) if  elem not in filledRows)

    outputSolution(test, output1, output2)
    
if __name__ == '__main__':
    t0 = time.time()
    solve(test=True)
    solve(test=False)
    print("Time: %.4f" %(time.time()-t0))