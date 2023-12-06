from aoccommon import *

def getWinningWays(time, dist):
    start = time / 2 - math.sqrt(time * time / 4 - dist)
    end = time / 2 + math.sqrt(time * time / 4 - dist)

    if int(start) == start:
        start += 1
        end -= 1

    start = math.ceil(start)
    end = math.floor(end)
    
    return end - start + 1

def solve(test: bool = False):
    lines = getInput(test)

    output1 = 1
    output2 = 1

    times = intList(lines[0].split()[1:])
    distances = intList(lines[1].split()[1:])

    for index, time in enumerate(times):
        dist = distances[index]
        output1 *= getWinningWays(time, dist)

    time = int(separateString(lines[0], [":"])[1].replace(" ", ""))
    dist = int(separateString(lines[1], [":"])[1].replace(" ", ""))

    output2 *= getWinningWays(time, dist)

    outputSolution(test, output1, output2)
    
if __name__ == '__main__':
    t0 = time.time()
    solve(test=True)
    solve(test=False)
    print("Time: %.4f" %(time.time()-t0))