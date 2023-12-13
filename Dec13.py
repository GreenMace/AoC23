from aoccommon import *

def findMirror(map, allowFix):
    output = 0
    for start in range(len(map[:-1])):
        maxVert = min(start+1, len(map)-start-1)
        usedFix = False
        mirror = True
        for i in range(maxVert):
            for j in range(len(map[0])):
                if map[start-i][j] != map[start + i + 1][j]:
                    if usedFix or not allowFix:
                        mirror = False
                        break
                    usedFix = True

            if not mirror:
                mirror = False
                break
        
        if mirror and (usedFix or not allowFix):
            return start + 1
        
    return output

def solve(test: bool = False):
    lines = getInput(test)

    output1 = 0
    output2 = 0

    while lines:
        if "" in lines:
            splitIndex = lines.index("")
        else:
            splitIndex = len(lines)

        lines1 = lines[:splitIndex]
        lines = lines[splitIndex+1:]

        horizontal1 = findMirror(lines1, False)
        horizontal2 = findMirror(lines1, True)

        swapped = []
        for x in range(len(lines1[0])):
            temp = []
            for y in range(len(lines1)):
                temp.append(lines1[y][x])
            swapped.append(temp)

        vertical1 = findMirror(swapped, False)
        vertical2 = findMirror(swapped, True)

        output1 += 100 * horizontal1 + vertical1
        output2 += 100 * horizontal2
        if not horizontal2:
            output2 += vertical2

    outputSolution(test, output1, output2)
    
if __name__ == '__main__':
    t0 = time.time()
    solve(test=True)
    solve(test=False)
    print("Time: %.4f" %(time.time()-t0))