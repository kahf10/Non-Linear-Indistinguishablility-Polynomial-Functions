import math


def getMiStar(l):
    # Calculate the value of Mi*
    return math.log(2, l)


def getUi(h, l, z, a):
        # Calculate the value of Ui
    miStar = getMiStar(l)
    return math.pow(z, miStar)


def getMi(h, l, z, a):
    # Calculate the value of Mi 
    ui = getUi(h, l, z, a)
    return math.log(a, float(2/ui))
