import math
import random
from intial_variables import *


s = 2  # NUMBER OF TUPLES TO SHOW
d = 2  # NUMBER OF ATTRIBUTES TO SHOW


def getRand():
    """
    Use: The function randomly calculates a value for 'a' and then checks if it is within the scaling range or not.
        If not within the range, it adjusts accordingly.
    Arguments: None
    Return: Returns the value of a (adjusted if need be)
    """
    a = random.random()
    if(a > 0.1 and a < 0.9):
        return a
    elif(a > 0.9):
        return a - 0.1
    else:
        return a + 0.1


def randomPoly(lowestDeg, highestDeg, n=2):
    """
    Use: Creates a random polynomial functino for testing
    Arguments:
        lowestDeg: The lowest degree of power for the polynomial function
        highestDeg: The highest degree of power for the polynomial function
        n: The number of terms in the function where each represents one attribute
    Return: Retuns a list of lists that contain the coefficients in the first inner list and the powers in the second.
        Each of them have the most significant attribute / i^star attribute at the very end.
    """
    coefficents = [getRand() for i in range(n)] # Randomly creates coefficents each term in the function
    powers = [random.randint(lowestDeg, highestDeg) for i in range(n)] # Randomly creates powers for each term in the function within the given range
    coefficents[1] = 1  # Setting iStar 

    return [coefficents, powers]


def revCalc(ui, uis, mi, mis):
    """
    Use: Reverse calculates the values of h, z, l for the given function in order to cross check the actual and calculated value
        of each and prints them
    Arguments:
        ui: Contains the coefficient value for the non-most-significant terms in the function
        uis: Contains the coefficient value for the most-significant term in the function
        mi: Contains the power value for the non-most-significant terms in the function
        mis: Contains the power value for the most-significant term in the function
    Return: None
    """
    # h:
    h = math.pow((1/ui), (1/mi))
    print("h = ", h)

    # z:
    z = math.pow(ui, (1/mis))
    print("z = ", z)

    # l:
    l = math.pow(2, (1/mis))
    print("l = ", l)


def getMiStar(l):
    """
    Use: Calculates the mi_star value for the function using the value of l
    Arguments: 
        l: The 'l' value we found for that attribute of the function    
    Return: Returns the calculated mi_star value for the function
    """
    # Calculate the value of Mi*
    return math.log(2, l)


def getUi(h, l, z):
    """
    Use: Calculates the ui value for the function using the value of l and z and mi_star
    Arguments: 
        h: The 'h' value we found for that attribute of the function
        l: The 'l' value we found for that attribute of the function    
        z" The 'z' value we found for that atrribute of the function
    Return: Returns the calculated ui value for the function
    """
    # Calculate the value of Ui
    miStar = getMiStar(l) # Calculating the value of mi_star 
    return math.pow(z, miStar)


def getMi(h, ui):
    """
    Use: Calculates the mi value for the function using the value of h and ui
    Arguments: 
        h: The 'h' value we found for that attribute of the function
        l: The 'l' value we found for that attribute of the function    
        z" The 'z' value we found for that atrribute of the function
    Return: Returns the calculated mi value for the function
    """
    if(ui == 0): # In the case where we find out that the attribute does not matter at all to the user
        print('-------', 'ui is 0', '-------')
        return 1.0
    return -math.log(ui, h) 


def getUtilityScore(function, tupleSet):
    """
    Use: Calculates the utility score for the given tuples when inserted in the function and returns the one with the most
    Arguments: 
        function: Stores the function that was randomly created
        tupleSet: Stores the tuple set 
    Return: Returns the calculated score value for the tuple set
    """
    score = 0
    scoreSet = []
    for tuple in tupleSet: # Goes through tuple in the tuple set
        score = 0
        for i in range(len(function)): # Goes through each value in the function: the coefficients and the powers
            score += float((math.pow(tuple[i], function[1][i]))*function[0][i]) # Calculates the score
        scoreSet.append(score)

    return scoreSet.index(max(scoreSet)) # Returns the tuple with the maximum score


def getI_star(function):
    """
    Use: Finds out the most important attribute to the user
    Arguments:
        function: Consists of the function that was randomly created
    Returns: Returns the attribute that is most important
    """
    return function[0].index(max(function[0])) # Calculates the term with highest coefficient to find the most important attribute


def get_ave(bound):
    """
    Use: Calculates the average bound for the range
    Arguments: 
        bound: A list consisting of the upper and lower bound for any, one particular value
    Return: Returns the average bound
    """
    return float(sum(bound)/len(bound)) 


def find_h(f, d, iter, show=False):
    # Showing default tuples

    i_star = getI_star(f)

    hBound = [1, H_INITIAL_UPPER_BOUND]
    tupleSet = [[2, 0], [0, 1]]
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

        shownTuple[1][0] = 0
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
            print('================================')
            print('USER PICKED TUPLE', max_score_index+1)
            print('--------------------------------')
            print('------- New Bound for H --------')
            print(hBound)
            print('                                      ')
            print('                                      ')

    return hBound


def find_l(hBound, f, d=2, iter=10, show=False):
    # Showing default tuples

    s1 = [get_ave(hBound), 1]  # Control Tuple
    s2 = [0, 2]  # Given Tuple
    i_star = getI_star(f)
    lBound = [1, 2]
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
            t = [tupleSet[j][0], chi_j]
            shownTuple.append(t)

        shownTuple[0][0] = get_ave(hBound)
        shownTuple[0][1] = 1

        max_score_index = getUtilityScore(f, shownTuple)

        if(max_score_index == 0):
            lBound[0] = chi_j
        else:
            lBound[1] = chi_j
        count += 1
        if(show):
            print('=========== Round', count, '===========')
            print(shownTuple)
            print('================================')
            print('USER PICKED TUPLE', max_score_index+1)
            print('--------------------------------')
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
            print('================================')
            print('USER PICKED TUPLE', max_score_index+1)
            print('--------------------------------')
            print('------- New Bound for Z --------')
            print(zBound)
            print('                                      ')
            print('                                      ')
    return zBound


def find_a(f, hB, hL, Hz, d=2, iter=10, show=False):
    # Showing default tuples
    upperBounda = float(2/(math.pow(get_ave(Hz), math.log(2, get_ave(hL)))))
    s1 = [1, 0]  # Control Tuple
    s2 = [0, get_ave(hL)]  # Given Tuple
    i_star = getI_star(f)
    i = 0
    aBound = [1, upperBounda]

    print("INTITAL BOUND OF A: ", aBound)

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
            t = [chi_j, 0]
            # t = [chi_j, tupleSet[j][i]]
            shownTuple.append(t)

        shownTuple[0][0] = chi_j
        shownTuple[1][0] = 0
        shownTuple[1][1] = get_ave(hL)

        max_score_index = getUtilityScore(f, shownTuple)

        aBound[max_score_index] = chi_j

        count += 1
        if(show):
            print('=========== Round', count, '===========')
            print(shownTuple)
            print('================================')
            print('USER PICKED TUPLE', max_score_index+1)
            print('--------------------------------')
            print('------- New Bound for a --------')
            print(aBound)
            print('                                      ')
            print('                                      ')
    return aBound
