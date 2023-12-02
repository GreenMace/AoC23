from aoccommon import *

with open('Dec2_input.txt') as f:
    lines = f.readlines()

    maxCubes = {"red": 12, "green": 13, "blue": 14}

    output1 = 0
    output2 = 0

    for line in lines:
        line = line.strip()
        split = separateString(line, [" ", ": "])
        id = int(split[1])
        sets = split[2].split(";")

        fewest = {"green": 0, "red": 0, "blue": 0}
        possible = True
        for draws in sets:
            draws = draws.split(", ")

            tot = {"green": 0, "red": 0, "blue": 0}
            for draw in draws:
                draw = draw.strip().split(" ")
                addToDict(tot, draw[1], int(draw[0]))
            
            for k, v in tot.items():
                if v > maxCubes[k]:
                    possible = False
                
                if fewest[k] < v:
                    fewest[k] = v
                

        if possible:
            output1 += id

        power = fewest["green"] * fewest["red"] * fewest["blue"]
        output2 += power

    
    print(output1)
    print(output2)