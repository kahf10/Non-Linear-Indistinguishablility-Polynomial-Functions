import math
from math_func_helper import *
import pandas as pd


def run():
    data = runSim(TIMES)
    # u_i_df = pd.Series(u_i)
    # m_i_df = pd.Series(m_i)
    # m_istar_df = pd.Series(m_istar)
    pd.set_option('display.max_rows', None)
    df = pd.DataFrame(data).set_index('iteration')
    df = df.sort_values(by=['m_i_diff'], ascending=True)

    return df


def run1time(func=[]):
    if(len(func) == 0):
        f = randomPoly(1, 5)
    else:
        f = func

    # f = [[0.3, 1], [4, 5]]
    hB = find_h(f, 2, ITER_PER_ROUND)
    hZ = find_z(f, 2, ITER_PER_ROUND)
    hL = find_l(hB, f, 2, ITER_PER_ROUND)
    # hA = find_a(f, hB, hL, hZ, 2, ITER_PER_ROUND, True)
    print("Bound for H: ", hB)

    print("Bound for Z: ", hZ)

    print("Bound for L: ", hL)

    # print("Bound for A: ", hA)

    revCalc(f[0][0], f[0][1], f[1][0], f[1][1])

    uI = getUi(get_ave(hB), get_ave(hL), get_ave(hZ))

    mi_star = getMiStar(get_ave(hL))

    m_i = getMi(get_ave(hB), uI)

    # m_i = getMi(get_ave(hB), get_ave(hL), get_ave(hZ), get_ave(hA))
    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    print("Ui is: ", uI)
    print("% error of U_i is:", getDIP(uI, f[0][0]))
    print("---------------------------------------------------------")

    print("M_i is: ", m_i)
    print("% error of M_i is:", getDIP(m_i, f[1][0]))

    print("---------------------------------------------------------")

    print("Mi_star is: ", mi_star)
    print("% error of Mi_star is:", getDIP(mi_star, f[1][1]))
    print("----- Our Function in the form [coefficents, powers] ----")
    # # The form of our function [coefficents, powers]
    print(f)


def getDIP(newNum, ogNum):
    """
    Use: To get the difference in percentage error between the original value and the new value we calculated.
    Arguments:
        newNum - The new value we calculated;
        ogNum - The original value we had;
    Return: Returns the different percentage.
    """
    # print(ogNum)
    # temp =   # Calculates the difference
    # Calculates the difference percentage and returns it
    return round(abs(newNum-ogNum), 6)


def runSim(times, d=2):
    lowestDeg, highestDeg = LOWEST_DEGREE, HIGHEST_DEGREE
    inter = ITER_PER_ROUND
    """
    Use: Runs the simulation of the program
    Arguments:
        times - The number of different utility functions to simulate;
        inter - The number of rounds of questions the users has to answer
        lowestDeg - Lowest degree of the polynomial utility function
        highestDeg - Highest degree of the polynomial utility function
        d - The factor by which we divide while narrowing down each variable
    Return: Returns the calculated u_i, m_i and m_i* after running the simulation.
    """

    count = 0  # Keeps count of the number of simulations ran until now
    u_iL = []  # List to store the values of u_i for the different utility function
    m_iL = []  # List to store the different values of m_i for the different utility function
    m_i_starL = []  # List to store the different valus of m_i_star # for the different utility function

    init_ui = []
    init_mi = []
    init_mi_star = []
    countL = []

    new_ui = []
    new_mi = []
    new_mi_star = []

    while(count < times):  # While we haven't exceeded the number of simulations

        # Creates a random utility function
        f = randomPoly(lowestDeg, highestDeg)
        hB = find_h(f, 2, inter)  # Finds the range for B
        hL = find_l(hB, f, 2, inter)  # Finds the range for L
        hZ = find_z(f, 2, inter)  # Finds the range for Z
        # hA = find_a(f, hB, hL, hZ, 2, inter)  # Finds the range for A

        # Finds the uI value using the above ranges
        uI = getUi(get_ave(hB), get_ave(hL), get_ave(hZ))

        # Finds the mi_star value using the above ranges
        mi_star = getMiStar(get_ave(hL))

        m_i = getMi(get_ave(hB), uI)

        countL.append(count+1)
        count += 1  # Increases number of simulations done

        # Adds the error percentage to the u_i List
        u_iL.append(getDIP(uI, f[0][0]))
        # Adds the error percentage to the m_i List
        m_iL.append(getDIP(m_i, f[1][0]))
        # Adds the error percentage to the m_i_star List
        m_i_starL.append(getDIP(mi_star, f[1][1]))

        # Adds the user ui value to the init_u_i List
        new_ui.append(round(uI, 5))
        # Adds the error percentage to the m_i List
        new_mi.append(round(m_i, 5))
        # Adds the error percentage to the m_i_star List
        new_mi_star.append(round(mi_star, 5))

        # Adds the user ui value to the init_u_i List
        init_ui.append(f[0][0])
        # Adds the error percentage to the m_i List
        init_mi.append(f[1][0])
        # Adds the error percentage to the m_i_star List
        init_mi_star.append(f[1][1])

        data = {
            'iteration': countL,

            'u_i_diff': u_iL,
            'm_i_diff': m_iL,
            'm_istar_diff': m_i_starL,

            "new u_i":   new_ui,
            'new m_i':    new_mi,
            "new m_i_star":      new_mi_star,

            "user u_i":   init_ui,
            'user m_i':    init_mi,
            "user m_i_star":      init_mi_star

        }
    return data
    # return u_iL, m_iL, m_i_starL  # Returns all the final values
