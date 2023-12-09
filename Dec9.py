from aoccommon import *

def solve(test: bool = False):
    lines = getInput(test)

    output1 = 0
    output2 = 0

    for line in lines:
        splits = intList(line.split())
        mult = 1
        while True:
            output1 += splits[-1]
            output2 += mult*splits[0]

            differences = []
            for i in range(len(splits[:-1])):
                differences.append(splits[i+1]-splits[i])

            if all(elem == 0 for elem in differences):
                break
                
            mult *= -1
            splits = differences

    outputSolution(test, output1, output2)
    
if __name__ == '__main__':
    t0 = time.time()
    solve(test=True)
    solve(test=False)
    print("Time: %.4f" %(time.time()-t0))
