from aoccommon import *

def solve(test: bool = False):
    lines = getInput(test)

    output1 = 0
    output2 = 0

    copies = [1 for _ in lines]

    for i, line in enumerate(lines):
        split = separateString(line, [":", "|"])
        winning = split[1].split()
        numbers = split[2].split()
        
        tot1 = 0
        tot2 = 0
        for num in numbers:
            if num in winning:
                tot1 = pow(2, tot2)
                tot2 += 1

        for x in range(i+1, i+tot2+1):
            copies[x] += copies[i]

        output1 += tot1

    output2 = sum(copies)

    outputSolution(test, output1, output2)
    
if __name__ == '__main__':
    t0 = time.time()
    solve(test=True)
    solve(test=False)
    print("Time: %.4f" %(time.time()-t0))