import math
from math_func_helper import *


def getDIP(newNum, ogNum):
    # getDifferenceInPercentage
    temp = abs(newNum-ogNum)
    return float(temp/ogNum)*100


def runSim(times, inter, lowestDeg, highestDeg, d=2):
    count = 0
    u_iL = []
    m_iL = []
    m_i_starL = []
    while(count < times):

        f = randomPoly(lowestDeg, highestDeg)
        hB = find_h(f, 2, inter)
        hL = find_l(hB, f, 2, inter)
        hZ = find_z(f, 2, inter)
        hA = find_a(f, hB, hL, hZ, 2, inter)

        uI = getUi(get_ave(hB), get_ave(hL), get_ave(hZ))

        mi_star = getMiStar(get_ave(hL))

        m_i = getMi(get_ave(hB), get_ave(hL), get_ave(hZ), get_ave(hA))

        count += 1

        u_iL.append(getDIP(uI, f[0][0]))
        m_iL.append(getDIP(m_i, f[1][0]))
        m_i_starL.append(getDIP(mi_star, f[1][1]))

    return u_iL, m_iL, m_i_starL
