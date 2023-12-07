from aoccommon import *

def sortCards(card):
    if card[0] == "J":
        return 6
    
    return 6-card[1]

def checkHand(hand, handType, allowJokers):
    jokersUsed = 0
    for k, v in hand.items():
        availJokers = hand.get("J", 0) - jokersUsed
        
        if k == "J":
            if availJokers in handType:
                handType.remove(v)
        elif v in handType:
            handType.remove(v)
        elif allowJokers:
            for x in range(availJokers, 0, -1):
                if v+x in handType:
                    handType.remove(v+x)
                    jokersUsed += x
                    break

    return not handType

def compHands(hand1, hand2, jokers = False):
    handStrength = [[5], [4], [3, 2], [3], [2, 2], [2], [1]]
    cardStrength = ['A', 'K', 'Q', "T", "9", "8", "7", "6", "5", "4", "3", "2"]

    if jokers:
        cardStrength.append("J")
    else:
        cardStrength.insert(3, "J")

    cards1 = {k: v for k, v in sorted(countOcc(hand1).items(), key=sortCards)}
    cards2 = {k: v for k, v in sorted(countOcc(hand2).items(), key=sortCards)}

    strength1 = 0
    strength2 = 0
    for i, s in enumerate(handStrength):
        if not strength1 and checkHand(cards1, s.copy(), allowJokers=jokers):
            strength1 = i+1

        if not strength2 and checkHand(cards2, s.copy(), allowJokers=jokers):
            strength2 = i+1

    if not strength1 == strength2:
        return (strength1 < strength2) * 2 - 1
    
    for i in range(len(hand1)):
        index1 = cardStrength.index(hand1[i])
        index2 = cardStrength.index(hand2[i])
        if not index1 == index2:
            return (index1 < index2) * 2 - 1

    return 0

def solve(test: bool = False):
    lines = getInput(test)

    output1 = 0
    output2 = 0

    bids = {}
    hands = []
    for line in lines:
        splits = line.split()
        hands.append(splits[0])
        bids[splits[0]] = int(splits[1])
    
    hands1 = sorted(hands, key = cmp_to_key(lambda c1, c2, j = False: compHands(c1, c2, j)))
    
    for i, hand in enumerate(hands1):
        output1 += bids[hand]*(i+1)

    hands2 = sorted(hands, key = cmp_to_key(lambda c1, c2, j = True: compHands(c1, c2, j)))
    
    for i, hand in enumerate(hands2):
        output2 += bids[hand]*(i+1)

    outputSolution(test, output1, output2)
    
if __name__ == '__main__':
    t0 = time.time()
    solve(test=True)
    solve(test=False)
    print("Time: %.4f" %(time.time()-t0))