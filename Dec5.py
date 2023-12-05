from aoccommon import *

def newIntervals(start1, end1, start2, end2, vStart, vEnd):
    output = []
    if not inInterval(start2, end2, start1):
        if start1 > end2 or end1 < start2:
            return []
        
        output.append([start1, start2-1])
        start1 = vStart
    else:
        start1 = vStart + start1 - start2
    
    if not inInterval(start2, end2, end1):
        output.append([end2+1, end1])
        end1 = vEnd
    else:
        end1 = vEnd + end1 - end2

    output.append([start1, end1])
    return output

def updateIntervals(intervals, maps):
    output = []
    for inter in intervals:
        start = inter[0]
        end = inter[1]

        untranslated = [] if maps else [inter]
        for map in maps:
            newInts = newIntervals(start, end, map[0], map[1], map[2],  map[3])
            if not newInts:
                untranslated.append(inter)
                continue

            for interval in newInts[:-1]:
                untranslated.append(interval)

            if len(newInts) == 1:
                untranslated.append([])

            output.append(newInts[-1])

        untranslated = intervalIntersect(untranslated)
        if untranslated:
            output.append(untranslated)

    return output

def solve(test: bool = False):
    lines = getInput(test)

    output1 = 0
    output2 = 0

    current = {}

    seeds = intList(lines[0].split()[1:])
    for seed in seeds:
        current[seed] = seed

    for line in lines[1:]:
        if not line:
            current = {v: v for k, v in current.items()}
            continue

        splits = line.split()
        if splits[1] == "map:":
            continue

        value, index, length = intList(splits)
        for k, v in current.items():
            if k in range(index, index+length):
                current[k] = value + k - index
                
    output1 = min(current.values())

    intervals = []
    maps = []

    seeds = intList(lines[0].split()[1:])
    for seedIndex in range(0, len(seeds), 2):
        intervals.append([seeds[seedIndex], seeds[seedIndex] + seeds[seedIndex+1]-1])

    for line in lines[1:]:
        if not line:
            intervals = updateIntervals(intervals, maps)
            maps = []
            continue

        splits = line.split()
        if splits[1] == "map:":
            continue

        value, index, length = intList(splits)
        maps.append([index, index + length - 1, value, value + length - 1])
    
    intervals = updateIntervals(intervals, maps)

    minimum = intervals[0][0]
    for inter in intervals:
        if inter[0] < minimum:
            minimum = inter[0]

    output2 = minimum

    outputSolution(test, output1, output2)
    
if __name__ == '__main__':
    t0 = time.time()
    solve(test=True)
    solve(test=False)
    print("Time: %.4f" %(time.time()-t0))