import math
import random


def randomPoly(lowestDeg, highestDeg, n=2):
    coefficents = [random.random() for i in range(n)]
    powers = [random.randint(lowestDeg, highestDeg) for i in range(n)]
    coefficents[1] = 1  # Setting iStar
    return [coefficents, powers]


def getMiStar(l):
    # Calculate the value of Mi*
    return math.log(2, l)


def getUi(h, l, z):
    # Calculate the value of Ui
    miStar = getMiStar(l)
    return math.pow(z, miStar)


def getUtilityScore(function, tupleSet):
    score = 0
    scoreSet = []
    for tuple in tupleSet:
        score = 0
        for i in range(len(function)):
            score += float((math.pow(tuple[i], function[1][i]))*function[0][i])
        scoreSet.append(score)

    return scoreSet.index(max(scoreSet))


def getMi(h, l, z, a):
    # Calculate the value of Mi
    ui = getUi(h, l, z)
    return math.log(a, float(2/ui))


def getI_star(function):
    return function[0].index(max(function[0]))


def get_ave(bound):
    return (sum(bound)/len(bound))
