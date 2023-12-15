from aoccommon import *

def solve(test: bool = False):
    lines = getInput(test)

    output1 = 0
    output2 = 0

    boxes = {}
    splits = ",".join(lines).split(",")
    for split in splits:
        current = 0
        for i, char in enumerate(split):
            if char == "-" and current in boxes and split[:i] in boxes[current]:
                del boxes[current][split[:i]]
            elif char == "=":
                if current not in boxes:
                    boxes[current] = {}
                boxes[current][split[:i]] = int(split[i+1:])

            current = (current + ord(char)) * 17 % 256
        output1 += current

    for box, labels in boxes.items():
        i = 1
        for focal in labels.values():
            output2 += (box+1) * focal * i
            i += 1

    outputSolution(test, output1, output2)
    
if __name__ == '__main__':
    t0 = time.time()
    solve(test=True)
    solve(test=False)
    print("Time: %.4f" %(time.time()-t0))
