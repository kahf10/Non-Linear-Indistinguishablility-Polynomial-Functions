import math
import random

s = 2  # NUMBER OF TUPLES TO SHOW
d = 2  # NUMBER OF ATTRIBUTES TO SHOW


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


def find_h(f, d=2, iter=10, show=False):
    # Showing default tuples

    i_star = getI_star(f)

    hBound = [0, 1]
    tupleSet = [[0, 1], [1, 0]]
    count = 0

    while(count < iter):
        shownTuple = []
        chi = []
        for j in range(d):

            # if j == i_star:
            #     continue
            chi_j = hBound[0] + ((j+1)*(hBound[1]-hBound[0]))/s

            chi.append(chi_j)

            t = [chi_j, tupleSet[j][i_star]]

            shownTuple.append(t)

        # shownTuple[1][0] = 1
        # shownTuple[0][1] = 1

        max_score_index = getUtilityScore(f, shownTuple)
        if(max_score_index == 0):
            hBound[1] = chi[0]
        else:
            hBound[0] = chi[0]

        # hBound[max_score_index] = chi_j
        count += 1
        if(show):
            print('=========== Round', count, '===========')
            print(shownTuple)
            print('USER PICKED TUPLE', max_score_index+1)
            print('------- New Bound for H --------')
            print(hBound)
            print('                                      ')
            print('                                      ')

    return hBound


def find_l(hBound, f, d=2, iter=10, show=False):
    # Showing default tuples

    s1 = [1, 1]  # Control Tuple
    s2 = [2, sum(hBound) / len(hBound)]  # Given Tuple
    i_star = getI_star(f)
    lBound = [s1[0], s2[0]]
    tupleSet = [s1, s2]
    count = 0

    while(count < iter):
        shownTuple = []
        chi = []
        for j in range(d):

            # if j == i_star:
            #     continue
            chi_j = float(lBound[0] + (j*(
                lBound[1]-lBound[0]))/s)
            chi.append(chi_j)
            t = [chi_j, tupleSet[j][i_star]]
            shownTuple.append(t)

        shownTuple[0][0] = 1

        max_score_index = getUtilityScore(f, shownTuple)

        if(max_score_index == 0):
            lBound[0] = chi_j
        else:
            lBound[1] = chi_j
        count += 1
        if(show):
            print('=========== Round', count, '===========')
            print(shownTuple)
            print('USER PICKED TUPLE', max_score_index+1)
            print('------- New Bound for L --------')
            print(lBound)
            print('                                      ')
            print('                                      ')
    return lBound


def find_z(f, d=2, iter=10, show=False):
    # Showing default tuples

    s1 = [1, 0]  # Control Tuple
    s2 = [0, 1]  # Given Tuple
    i_star = getI_star(f)
    i = 0
    zBound = [s1[1], s2[1]]
    tupleSet = [s1, s2]
    count = 0

    while(count < iter):
        shownTuple = []
        chi = []
        for j in range(d):

            # if j == i_star:
            #     continue
            chi_j = zBound[0] + (j*(
                zBound[1]-zBound[0]))/s
            chi.append(chi_j)
            t = [chi_j, tupleSet[j][i_star]]
            t = [tupleSet[j][i], chi_j]
            shownTuple.append(t)

        shownTuple[0][1] = 0

        max_score_index = getUtilityScore(f, shownTuple)

        zBound[max_score_index] = chi_j

        count += 1
        if(show):
            print('=========== Round', count, '===========')
            print(shownTuple)
            print('USER PICKED TUPLE', max_score_index+1)
            print('------- New Bound for Z --------')
            print(zBound)
            print('                                      ')
            print('                                      ')
    return zBound


def find_a(f, hB, hL, Hz, d=2, iter=10, show=False):
    # Showing default tuples
    lowerBounda = float(2/getMiStar(get_ave(hL)))

    s1 = [1, 0]  # Control Tuple
    s2 = [0, get_ave(hL)]  # Given Tuple
    i_star = getI_star(f)
    i = 0
    aBound = [lowerBounda, 1]
    tupleSet = [s1, s2]
    count = 0

    while(count < iter):
        shownTuple = []
        chi = []
        for j in range(d):

            # if j == i_star:
            #     continue
            chi_j = aBound[0] + (j*(
                aBound[1]-aBound[0]))/s
            chi.append(chi_j)
            t = [chi_j, tupleSet[j][i_star]]
            t = [tupleSet[j][i], chi_j]
            shownTuple.append(t)

        shownTuple[1][0] = 0
        shownTuple[1][1] = get_ave(hL)

        max_score_index = getUtilityScore(f, shownTuple)

        aBound[max_score_index] = chi_j

        count += 1
        if(show):
            print('=========== Round', count, '===========')
            print(shownTuple)
            print('USER PICKED TUPLE', max_score_index+1)
            print('------- New Bound for a --------')
            print(aBound)
            print('                                      ')
            print('                                      ')
    return aBound