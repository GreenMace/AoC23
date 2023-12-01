from aoccommon import *

with open('Dec1_input.txt') as f:
    lines = f.readlines()
    
    num = 0
    for line in lines:
        digits = getNumbersInString(line, toDigits=True, textAsDigit=True, destroyIntersect=False)
        num += int(digits[0] + digits[-1])

    print(num)


