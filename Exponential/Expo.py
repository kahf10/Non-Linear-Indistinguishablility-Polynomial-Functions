import math
import random
from intial_variables import *

def randomExpo(highestCo):
    """
    Use: Creates a random exponential function for testing
    Arguments:
        highestCo: The highest coefficient for the exponential function
    Return: Retuns a randomly generalted coefficient between 1 and the highestCo or the upper bound of h
    """

    coef1 = random.random() * (highestCo - 1) + 1
    coefs = random.random() * (highestCo - coef1) + coef1

    f = [coef1, coefs]
    return f


def getUtilityScore(function, tupleSet):
    """
    Use: Calculates the utility score for the given tuples when inserted in the function and returns the one with the most
    Arguments: 
        function: Stores the function that was randomly created
        tupleSet: Stores the tuple set 
    Return: Returns the calculated score value for the tuple set
    """
    scoreSet = []
    for tuple in tupleSet: # Goes through tuple in the tuple set
        score = 0
        for i in range(len(function)): # Goes through each value in the function: the coefficients and the powers
            score = score + 
        scoreSet.append(score)

    return scoreSet.index(max(scoreSet)) # Returns the tuple with the maximum score

def find_h(f, d, iter, show=False):
    """
    Use: Narrows down the value of h
    Arguments:
        f: The function we are testing h on
        d: The factor by which we want to factor down h in each iteration
        iter: The number of iterations we will narrow down h. The more iterations, the more accurate is the value of h.
    Return: Returns the final upper and lower bound for h
    """
    # Showing default tuples

    i_star = getI_star(f) # Finds the most important attribute

    hBound = [1, H_INITIAL_UPPER_BOUND] # Sets the inital bounds
    tupleSet = [[2, 0], [0, 1]] # The tuples we will be comparing at all times
    count = 0

    while(count < iter): # Loop for the number of iterations
        shownTuple = []
        chi = []
        for j in range(d):

            # if j == i_star:
            #     continue
            chi_j = hBound[0] + ((j+1)*(hBound[1]-hBound[0]))/s # Narrows down the bound into s equal divisions

            chi.append(chi_j) # Stores all the bounds for the iteration

            t = [chi_j, tupleSet[j][i_star]] # Cretes new tuples using the new bounds

            shownTuple.append(t)

        shownTuple[1][0] = 0
        # shownTuple[0][1] = 1

        max_score_index = getUtilityScore(f, shownTuple)
        if(max_score_index == 0): # Checking which tuple has the highest score in the utility function
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


