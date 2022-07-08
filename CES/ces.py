import random 
import math

H_INITIAL_UPPER_BOUND = 5
b = 10
d = 2
s = 2

def randomCES():
    """
    Use: Creates a random exponential function for testing
    Arguments:
        highestCo: The highest coefficient for the exponential function
    Return: Retuns a randomly generalted coefficient between 1 and the highestCo or the upper bound of h
    """

    coef1 = random.random()

    f = [coef1, 1.0]
    return f    

def revCalc(function):
    """
    Use: Reverse calculates the value of h for cross-checking purposes
    Arguments: The function to reverse calculate the values of h
    Return: None
    """
    ui = function[0]
    rh = 1/(math.pow(ui,(1/b)))
    print("Reverse Calculated h = ", rh)

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
            score += function[i] * (math.pow(tuple[i], b)) # Calculates the score
        score = math.pow(score,(1/b))
        scoreSet.append(score)
    return scoreSet.index(max(scoreSet)) # Returns the index of the tuple with the max score. We use index because there are only two tuples to choose from. 

def find_h(f, d, iter, show=True):
    """
    Use: Narrows down the value of h
    Arguments:
        f: The function we are testing h on
        d: The factor by which we want to factor down h in each iteration
        iter: The number of iterations we will narrow down h. The more iterations, the more accurate is the value of h.
    Return: Returns the final upper and lower bound for h
    """
    # Showing default tuples

    i_star = 1 # Finds the most important attribute

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
            print('USER PICKED TUPLE', max_score_index)
            print('--------------------------------')
            print('------- New Bound for H --------')
            print(hBound)
            print('                                      ')
            print('                                      ')

    return hBound

def get_ave(bound):
    """
    Use: Calculates the average bound for the range
    Arguments: 
        bound: A list consisting of the upper and lower bound for any, one particular value
    Return: Returns the average bound
    """
    return float(sum(bound)/len(bound))

def calc_ui(hbound):
    """
    Use: Calculates the bound for ui using the bounds for h we obtained
    Arguments:
        hbound: The upper and lower bound for h for the given utility function
    Return: Returns the ui value we calculated
    """
    h = get_ave(hbound)
    ui = math.pow((1/h), b)
    return ui

def main():
    f = randomCES() # Creates a random exponential function
    print(f) 
    
    hbound = find_h(f, d, 15) # Function to calculate the bounds for h
    print(get_ave(hbound))
    revCalc(f) # Reverse calculates the value of h using the randomly generated function
    finalui = calc_ui(hbound) # Calculates the ui using the h bounds
    
    print(finalui, 1)

main()