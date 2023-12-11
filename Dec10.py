from aoccommon import *

def solve(test: bool = False):
    lines = getInput(test, year = 2023, day = 10)

    output1 = 0
    output2 = 0

    start = []
    for y, line in enumerate(lines):
        for x, val in enumerate(line):
            if val == "S":
                start = [y, x]
            
            if start:
                break
        if start:
            break
    
    loop = {}
    sReplacement = {"|", "-", "J", "L", "7", "F"}
    neighbours = getNeighbours(lines, start[0], start[1])
    for neigh in neighbours:
        if neigh[0] < start[0]:
            if neigh[1] == start[1] and lines[neigh[0]][neigh[1]] in ["|", "7", "F"]:
                addToDict(loop, toCoord(start), val = neigh, append = True)
                sReplacement &= {"|", "J", "L"}
        elif neigh[0] > start[0]:
            if neigh[1] == start[1] and lines[neigh[0]][neigh[1]] in ["|", "J", "L"]:
                addToDict(loop, toCoord(start), val = neigh, append = True)
                sReplacement &= {"|", "7", "F"}
        else:
            if neigh[1] > start[1]:
                if lines[neigh[0]][neigh[1]] in ["-", "7", "J"]:
                    addToDict(loop, toCoord(start), val = neigh, append = True)
                    sReplacement &= {"-", "L", "F"}
            else:
                if lines[neigh[0]][neigh[1]] in ["-", "L", "F"]:
                    addToDict(loop, toCoord(start), val = neigh, append = True)
                    sReplacement &= {"-", "7", "J"}
    
    pos = loop[toCoord(start)][0]
    while lines[pos[0]][pos[1]] != "S":
        s = lines[pos[0]][pos[1]]
        coord = toCoord(pos)
        if s == "|":
            if toCoord([pos[0]+1, pos[1]]) in loop:
                addToDict(loop, coord, val = [pos[0]-1, pos[1]], append = True)
                addToDict(loop, coord, val = [pos[0]+1, pos[1]], append = True)
            else:
                addToDict(loop, coord, val = [pos[0]+1, pos[1]], append = True)
                addToDict(loop, coord, val = [pos[0]-1, pos[1]], append = True)
        elif s == "-":
            if toCoord([pos[0], pos[1]+1]) in loop:
                addToDict(loop, coord, val = [pos[0], pos[1]-1], append = True)
                addToDict(loop, coord, val = [pos[0], pos[1]+1], append = True)
            else:
                addToDict(loop, coord, val = [pos[0], pos[1]+1], append = True)
                addToDict(loop, coord, val = [pos[0], pos[1]-1], append = True)
        elif s == "L":
            if toCoord([pos[0]-1, pos[1]]) in loop:
                addToDict(loop, coord, val = [pos[0], pos[1]+1], append = True)
                addToDict(loop, coord, val = [pos[0]-1, pos[1]], append = True)
            else:
                addToDict(loop, coord, val = [pos[0]-1, pos[1]], append = True)
                addToDict(loop, coord, val = [pos[0], pos[1]+1], append = True)
        elif s == "J":
            if toCoord([pos[0]-1, pos[1]]) in loop:
                addToDict(loop, coord, val = [pos[0], pos[1]-1], append = True)
                addToDict(loop, coord, val = [pos[0]-1, pos[1]], append = True)
            else:
                addToDict(loop, coord, val = [pos[0]-1, pos[1]], append = True)
                addToDict(loop, coord, val = [pos[0], pos[1]-1], append = True)
        elif s == "7":
            if toCoord([pos[0]+1, pos[1]]) in loop:
                addToDict(loop, coord, val = [pos[0], pos[1]-1], append = True)
                addToDict(loop, coord, val = [pos[0]+1, pos[1]], append = True)
            else:
                addToDict(loop, coord, val = [pos[0]+1, pos[1]], append = True)
                addToDict(loop, coord, val = [pos[0], pos[1]-1], append = True)
        elif s == "F":
            if toCoord([pos[0]+1, pos[1]]) in loop:
                addToDict(loop, coord, val = [pos[0], pos[1]+1], append = True)
                addToDict(loop, coord, val = [pos[0]+1, pos[1]], append = True)
            else:
                addToDict(loop, coord, val = [pos[0]+1, pos[1]], append = True)
                addToDict(loop, coord, val = [pos[0], pos[1]+1], append = True)
        
        pos = loop[coord][0]

    newS, = sReplacement
    lines = [line.replace("S", newS) for line in lines]

    searched = []
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if toCoord([y, x]) not in loop and [y, x] not in searched:
                s, c = getContained(lines, loop, [y, x], traceWalls=True, diagonal=False)
                searched.extend(s)
                output2 += len(s) * c

    output1 = len(loop) // 2

    outputSolution(test, output1, output2)
    
if __name__ == '__main__':
    t0 = time.time()
    solve(test=True)
    solve(test=False)
    print("Time: %.4f" %(time.time()-t0))