from aoccommon import *

def sortRocks(rock1, rock2, direction):
    if direction == 0:
        return boolToSign(rock1[0] > rock2[0])
    elif direction == 1:
        return boolToSign(rock1[1] > rock2[1])
    elif direction == 2:
        return boolToSign(rock1[0] < rock2[0])
    else:
        return boolToSign(rock1[1] < rock2[1])

def solve(test: bool = False):
    lines = getInput(test)

    output1 = 0
    output2 = 0

    mapSize = [len(lines), len(lines[0])]

    walls = []
    rocks = []
    for y, line in enumerate(lines):
        for x, chr in enumerate(line):
            if chr == "#":
                walls.append([y, x])
            elif chr == "O":
                rocks.append([y, x])

    outputs = []
    for i in range(200*4):
        blocked = [{}, {}]
        for wall in walls:
            y, x = wall
            addToDict(blocked[0], y, x, True)
            addToDict(blocked[1], x, y, True)

        rot = i % 4
        rocks = sorted(rocks, key = cmp_to_key(lambda c1, c2, j = rot: sortRocks(c1, c2, j)))
        for rock in rocks:
            if rot < 2:
                less = list(filter(lambda x: x < rock[rot%2], blocked[1 - i%2].get(rock[1 - i%2], [])))
                notBlocked = 0 if not less else max(less) + 1
            else:
                more = list(filter(lambda x: x > rock[rot%2], blocked[1 - i%2].get(rock[1 - i%2], [])))
                notBlocked = mapSize[i%2]-1 if not more else min(more) - 1

            addToDict(blocked[1 - i%2], rock[1 - i%2], notBlocked, True)
            rock[i%2] = notBlocked

        outputs.append(mapSize[0]*len(rocks) - sum([rock[0] for rock in rocks]))

    output1 += outputs[0]
    output2 = elemInLoopedList(outputs, 1000000000*4-1, listLoopLength(outputs, 4))

    outputSolution(test, output1, output2)
    
if __name__ == '__main__':
    t0 = time.time()
    solve(test=True)
    solve(test=False)
    print("Time: %.4f" %(time.time()-t0))