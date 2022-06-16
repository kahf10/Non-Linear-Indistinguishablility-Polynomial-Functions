import math
import random


def randomPoly(lowestDeg, highestDeg, n=2):
    coefficents = [random.random() for i in range(n)]
    powers = [random.randint(lowestDeg, highestDeg) for i in range(n)]
    return [coefficents, powers]


def getMiStar(l):
    # Calculate the value of Mi*
    return math.log(2, l)


def getUi(h, l, z, a):
    # Calculate the value of Ui
    miStar = getMiStar(l)
    return math.pow(z, miStar)


def getUtilityScore(function, tuple):
    score = 0
    for i in range(len(function)):
        score += float((math.pow(tuple[i], function[1][i]))*function[0][i])
    return score


def getMi(h, l, z, a):
    # Calculate the value of Mi
    ui = getUi(h, l, z, a)
    return math.log(a, float(2/ui))


def getI_star(function):
    return function[0].index(max(function[0]))


# def calc_a(function, s, iter, d=2, show=False):
#     i_star = getI_star(function)
#     # tuplesSet = [[0 for i in range(d)]for j in range(s)]
#     s1 = [2, 0]  # Control Tuple
#     s2 = [1, 1]  # Given Tuple
#     tupleSet = [s1, s2]
#     aBound = [s1[0], s1[0]]
#     scoreSet = []
#     """The following loop calculates a loose lower bound for a wrt the user"""
#     count = 0
#     while(count < iter):  # While the user does not find his bound, the loop keeps running
#         # Takes input from user regarding their choice

#         # Creating tuples
#         for i in range(d):
#             if i == i_star:
#                 continue
#             chi_j = aBound[0] + (i(aBound[1]-aBound[0]))/s
#             tupleSet.append[chi_j]


#         for tuple in tupleSet:
#             scoreSet.append(getScore(function, tuple))

#         if(scoreSet[0] > scoreSet[1]):  # If the user choose the first tuple
#             tupleSet[0][0] = tupleSet[0][0]*2
#             aBound[0] = tupleSet[0][0]  # Set the lower bound
#             count += 1
#         else:  # if the user chooses the second tuple, we can narrow down i

#             #     if(s == '2'):
#             #         choice = True  # If the user found their bound, we break the loop
#             #         break
#             #     else:
#             #         # Otherwise we increase the value for the given attribute
#             #         s1[atr1] = s1[atr1] * 2
#             #         # Appending all the possible values we parsed through for the user
#             #         seta.append(s1[atr1])

#             #     print()
#             #     # Repeatedly gives the user to make a choice as long as they do not find their upper bound
#             #     print("1.", s1)
#             #     print("2.", s2)

#             # """Once the Loop is over, we get a loose lower bound on the a"""
#             # a = float(s1[atr1])

#             # """The following loop narrows down the value of a by a half everytime as long as the user wants"""
#             # while(choice == True):  # We narrow down the value atleast once before the uesr chooses
#             #     # Because we are narrowing it down by 2, we only keep the iteration from 1 to 2
#             #     for chi in range(1, 3):
#             #         # Partitions the range into ndp equal parts to narrow down better
#             #         chi_j = seta[-2] + (chi*(a - seta[-2])/ndp)
#             #         # Creates the new tuple using the partitioned values
#             #         temp = {atr1: chi_j, atr2: 0}
#             #         print()
#             #         if(chi_j != a):  # Removes the reduntant case when the partitioned value is equal to the current value of a
#             #             print("1.", temp)
#             #             print("2.", s2)
#             #             s = input("Choose between the given tuples: ")
#             #             if(s == '1'):
#             #                 a = chi_j  # If the user chooses a lower bound for a, we update it and break the FOR loop
#             #                 break
#             #             else:
#             #                 # Otherwise we update our lower bound in the seta for the next iteration
#             #                 seta[-2] = chi_j

#             #     print("Your current value for the attribute", atr1,
#             #           "is", a)  # Prints the latest value of a
#             #     # Asks the user if they want to narrow down the value of a further or not
#             #     s = input(
#             #         "Would you like to narrow down the value of a? Press 0 for no. Anything else for yes. ")
#             #     if(s == '0'):
#             #         choice = False  # Helps break the loop if the user chooses not to narrow down any further

#     return a  # Returns the value of a

# def calc_a(atr1, atr2, iter=10, ndp=2):
#     s1 = [2, 0]  # Control Tuple
#     s2 = [1, 1]  # Given Tuple
#     seta = [1, 2]
#     tupleSet = [s1, s2]
#     aBound = [s2[0], s1[0]]

#     func = randomPoly(1, 10)
#     """The following loop calculates a loose lower bound for a wrt the user"""
#     count = 0  # We set the choice as False
#     while(count < iter):
#         scoreSet = []  # While the user does not find his bound, the loop keeps running
#         for tuple in tupleSet:
#             scoreSet.append(getScore(func, tuple))

#         # Takes input from user regarding their choice
#         if(scoreSet[0] > scoreSet[1]):

#             choice = True  # If the user found their bound, we break the loop
#             break
#         else:
#             # Otherwise we increase the value for the given attribute
#             s1[atr1] = s1[atr1] * 2
#             # Appending all the possible values we parsed through for the user
#             aBound[s1[atr1]]
#     """Once the Loop is over, we get a loose lower bound on the a"""
#     a = float(s1[atr1])
#     scoreSet = []

#     """The following loop narrows down the value of a by a half everytime as long as the user wants"""
#     while(choice == True):  # We narrow down the value atleast once before the uesr chooses
#         # Because we are narrowing it down by 2, we only keep the iteration from 1 to 2
#         for chi in range(ndp):
#             # Partitions the range into ndp equal parts to narrow down better
#             chi_j = aBound[0] + ((chi)*(aBound[1] - aBound[0])/ndp)
#             # Creates the new tuple using the partitioned values
#             tupleSet[chi][0] = chi_j

#         for tuple in tupleSet:
#             scoreSet.append(getScore(func, tuple))

#         if(scoreSet[0] > scoreSet[1]):


# return a  # Returns the value of a
