import math
from math_func_helper import *


def getDIP(newNum, ogNum): 
    """
    Use: To get the difference in percentage error between the original value and the new value we calculated.
    Arguments: 
        newNum - The new value we calculated; 
        ogNum - The original value we had;
    Return: Returns the different percentage. 
    """
    temp = abs(newNum-ogNum) # Calculates the difference
    return float(temp/ogNum)*100 # Calculates the difference percentage and returns it


def runSim(times, inter, lowestDeg, highestDeg, d=2):
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

    count = 0 # Keeps count of the number of simulations ran until now
    u_iL = [] # List to store the values of u_i for the different utility function
    m_iL = [] # List to store the different values of m_i for the different utility function
    m_i_starL = [] # List to store the different valus of m_i_star # for the different utility function 

    while(count < times): # While we haven't exceeded the number of simulations 

        f = randomPoly(lowestDeg, highestDeg) # Creates a random utility function 
        hB = find_h(f, 2, inter) # Finds the range for B
        hL = find_l(hB, f, 2, inter) # Finds the range for L
        hZ = find_z(f, 2, inter) # Finds the range for Z 
        hA = find_a(f, hB, hL, hZ, 2, inter) # Finds the range for A

        uI = getUi(get_ave(hB), get_ave(hL), get_ave(hZ)) # Finds the uI value using the above ranges

        mi_star = getMiStar(get_ave(hL)) # Finds the mi_star value using the above ranges 

        m_i = getMi(get_ave(hB), get_ave(hL), get_ave(hZ), get_ave(hA)) # Finds the m_i value using the above ranges

        count += 1 # Increases number of simulations done 

        u_iL.append(getDIP(uI, f[0][0])) # Adds the error percentage to the u_i List
        m_iL.append(getDIP(m_i, f[1][0])) # Adds the error percentage to the m_i List
        m_i_starL.append(getDIP(mi_star, f[1][1])) # Adds the error percentage to the m_i_star List

    return u_iL, m_iL, m_i_starL # Returns all the final values
