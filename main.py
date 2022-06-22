from math_func_helper import *
from stat_func_helper import *

import pandas as pd
# GLOBAL VARIABLES
s = 2  # NUMBER OF TUPLES TO SHOW
d = 2  # NUMBER OF ATTRIBUTES TO SHOW


def main():
    iteration = 10
    lowestDeg = 1
    highestDeg = 5

    f = randomPoly(1, 5)

    # f = [[0.3, 1], [4, 5]]
    hB = find_h(f, 2, iteration)
    hZ = find_z(f, 2, iteration)
    hL = find_l(hB, f, 2, iteration)
    # hA = find_a(f, hB, hL, hZ, 2, iteration, True)
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

    u_i, m_i, m_istar = runSim(100, iteration, lowestDeg, highestDeg)

    u_i_df = pd.Series(u_i)
    m_i_df = pd.Series(m_i)
    m_istar_df = pd.Series(m_istar)

    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    print("Ui data: ", u_i_df.describe())

    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    print("M_i data: ", m_i_df.describe())

    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    print("M_i_star data: ", m_istar_df.describe())
    print("---------------------------------------------------------")
    print("---------------------------------------------------------")


if __name__ == "__main__":
    main()
