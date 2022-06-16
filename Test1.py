from utility_helper import *
# GLOBAL VARIABLES
s = 2  # NUMBER OF TUPLES TO SHOW
d = 2  # NUMBER OF ATTRIBUTES TO SHOW


# def fakeTuple(i, i_star):
#     point = [[]]
#     for j in range(d):
#         if(j == i):
#             # SETTING I
#             p[j][0] = 0
#         elif j == i_star:
#             # SETTING I STAR
#             p[j][0] = 1


def calc_a(atr1, atr2, ndp):
    s1 = {atr1: 2, atr2: 0}  # Control Tuple
    s2 = {atr1: 1, atr2: 1}  # Given Tuple
    seta = [1, 2]

    print("1.", s1)  # Prints the initial choices for the user
    print("2.", s2)

    """The following loop calculates a loose lower bound for a wrt the user"""
    choice = False  # We set the choice as False
    while(choice == False):  # While the user does not find his bound, the loop keeps running
        # Takes input from user regarding their choice
        s = input("Choose between the given tuples: ")
        if(s == '2'):
            choice = True  # If the user found their bound, we break the loop
            break
        else:
            # Otherwise we increase the value for the given attribute
            s1[atr1] = s1[atr1] * 2
            # Appending all the possible values we parsed through for the user
            seta.append(s1[atr1])

        print()
        # Repeatedly gives the user to make a choice as long as they do not find their upper bound
        print("1.", s1)
        print("2.", s2)

    """Once the Loop is over, we get a loose lower bound on the a"""
    a = float(s1[atr1])

    """The following loop narrows down the value of a by a half everytime as long as the user wants"""
    while(choice == True):  # We narrow down the value atleast once before the uesr chooses
        # Because we are narrowing it down by 2, we only keep the iteration from 1 to 2
        for chi in range(1, 3):
            # Partitions the range into ndp equal parts to narrow down better
            chi_j = seta[-2] + (chi*(a - seta[-2])/ndp)
            # Creates the new tuple using the partitioned values
            temp = {atr1: chi_j, atr2: 0}
            print()
            if(chi_j != a):  # Removes the reduntant case when the partitioned value is equal to the current value of a
                print("1.", temp)
                print("2.", s2)
                s = input("Choose between the given tuples: ")
                if(s == '1'):
                    a = chi_j  # If the user chooses a lower bound for a, we update it and break the FOR loop
                    break
                else:
                    # Otherwise we update our lower bound in the seta for the next iteration
                    seta[-2] = chi_j

        print("Your current value for the attribute", atr1,
              "is", a)  # Prints the latest value of a
        # Asks the user if they want to narrow down the value of a further or not
        s = input(
            "Would you like to narrow down the value of a? Press 0 for no. Anything else for yes. ")
        if(s == '0'):
            choice = False  # Helps break the loop if the user chooses not to narrow down any further

    return a  # Returns the value of a

# def calc_b(atr1, atr2, ndp,a):
#     s1 = {atr1: 2, atr2: 0}  # Control Tuple
#     s2 = {atr1: a, atr2: 1}  # Given Tuple
#     seta = [1, 2]

#     print("1.", s1)  # Prints the initial choices for the user
#     print("2.", s2)

#     """The following loop calculates a loose lower bound for a wrt the user"""
#     choice = False  # We set the choice as False
#     while(choice == False):  # While the user does not find his bound, the loop keeps running
#         # Takes input from user regarding their choice
#         s = input("Choose between the given tuples: ")
#         if(s == '2'):
#             choice = True  # If the user found their bound, we break the loop
#             break
#         else:
#             # Otherwise we increase the value for the given attribute
#             s1[atr1] = s1[atr1] * 2
#             # Appending all the possible values we parsed through for the user
#             seta.append(s1[atr1])

#         print()
#         # Repeatedly gives the user to make a choice as long as they do not find their upper bound
#         print("1.", s1)
#         print("2.", s2)

#     """Once the Loop is over, we get a loose lower bound on the a"""
#     a = float(s1[atr1])

#     """The following loop narrows down the value of a by a half everytime as long as the user wants"""
#     while(choice == True):  # We narrow down the value atleast once before the uesr chooses
#         # Because we are narrowing it down by 2, we only keep the iteration from 1 to 2
#         for chi in range(1, 3):
#             # Partitions the range into ndp equal parts to narrow down better
#             chi_j = seta[-2] + (chi*(a - seta[-2])/ndp)
#             # Creates the new tuple using the partitioned values
#             temp = {atr1: chi_j, atr2: 0}
#             print()
#             if(chi_j != a):  # Removes the reduntant case when the partitioned value is equal to the current value of a
#                 print("1.", temp)
#                 print("2.", s2)
#                 s = input("Choose between the given tuples: ")
#                 if(s == '1'):
#                     a = chi_j  # If the user chooses a lower bound for a, we update it and break the FOR loop
#                     break
#                 else:
#                     # Otherwise we update our lower bound in the seta for the next iteration
#                     seta[-2] = chi_j

#         print("Your current value for the attribute", atr1,
#               "is", a)  # Prints the latest value of a
#         # Asks the user if they want to narrow down the value of a further or not
#         s = input(
#             "Would you like to narrow down the value of a? Press 0 for no. Anything else for yes. ")
#         if(s == '0'):
#             choice = False  # Helps break the loop if the user chooses not to narrow down any further

#     return a


def main():
    func = randomPoly(1, 10)
    print(func)
    print(getI_star(func))
    print(calc_a("HP", "MLG", 2))


if __name__ == "__main__":
    main()
