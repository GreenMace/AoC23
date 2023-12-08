from aoccommon import *

def solve(test: bool = False):
    lines = getInput(test)

    output1 = 0
    output2 = 0

    instr = lines[0]

    directions = {}
    positions = []
    for line in lines[2:]:
        split = separateString(line, [" = (", ", ", ")"])
        directions[split[0]] = [split[1], split[2]]
        if split[0].endswith("A"):
            positions.append(split[0])

    ends = []
    for pos in positions:
        i = 0
        o1 = pos == "AAA"
        while not pos.endswith("Z"):
            pos = directions[pos][instr[i % len(instr)] == "R"]
            i += 1

        output1 += i * o1
        ends.append(i)

    output2 = lcm(ends)

    outputSolution(test, output1, output2)
    
if __name__ == '__main__':
    t0 = time.time()
    solve(test=True)
    solve(test=False)
    print("Time: %.4f" %(time.time()-t0))