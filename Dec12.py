from aoccommon import *
from functools import cache

def recPlace(record, nums):
    if not nums:
        if "#" in record:
            return 0
        return 1
    
    length = nums[0]
    possible = 0
    for i, char in enumerate(record):
        if char in "#?" and i+length <= len(record):
            if i+length < len(record) and all(x in "#?" for x in record[i:i + length]):
                if record[i+length] in ".?":
                    possible += recPlace(record[i+length + 1:], nums[1:])
            elif len(nums) == 1 and all(x in "#?" for x in record[i:i + length]):
                return possible + 1
            
            if char in "#":
                return possible

    return possible

def solve(test: bool = False):
    lines = getInput(test)

    output1 = 0
    output2 = 0

    for line in lines:
        splits = line.split()
        nums = intList(splits[1].split(","))

        input = splits[0] + "."

        @cache
        def permutations(pos, num):
            record = input[pos:]
            if num == len(nums):
                if "#" in record:
                    return 0
                return 1
            
            length = nums[num]
            possible = 0
            for i, char in enumerate(record):
                if char in "#?" and i+length <= len(record):
                    if i + length < len(record) and all(x in "#?" for x in record[i:i + length]):
                        if record[i+length] in ".?":
                            possible += permutations(pos + i + length + 1, num + 1)
                    elif len(nums) == num + 1 and all(x in "#?" for x in record[i:i + length]):
                        return possible + 1
                    
                    if char in "#":
                        return possible

            return possible

        output1 += permutations(0, 0)


        permutations.cache_clear()
        input = "?".join([splits[0]]*5)
        nums = nums*5

        output2 += permutations(0,0)

        

    outputSolution(test, output1, output2)
    
if __name__ == '__main__':
    t0 = time.time()
    solve(test=True)
    solve(test=False)
    print("Time: %.4f" %(time.time()-t0))