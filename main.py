from math_func_helper import *
# GLOBAL VARIABLES
s = 2  # NUMBER OF TUPLES TO SHOW
d = 2  # NUMBER OF ATTRIBUTES TO SHOW


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

        shownTuple[0][1] = 0

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

# def find_a(f, hB, lB, zB, d=2, iter=10, show=False):

#     # Showing default tuples

#     s1 = [1, 0]  # Control Tuple
#     s2 = [0, 1]  # Given Tuple
#     i_star = getI_star(f)
#     i = 0
#     zBound = [s1[1], s2[1]]
#     tupleSet = [s1, s2]
#     count = 0

#     while(count < iter):
#         shownTuple = []
#         chi = []
#         for j in range(d):

#             # if j == i_star:
#             #     continue
#             chi_j = zBound[0] + (j*(
#                 zBound[1]-zBound[0]))/s
#             chi.append(chi_j)
#             t = [chi_j, tupleSet[j][i_star]]
#             t = [tupleSet[j][i], chi_j]
#             shownTuple.append(t)

#         shownTuple[0][1] = 0

#         max_score_index = getUtilityScore(f, shownTuple)

#         zBound[max_score_index] = chi_j

#         count += 1
#         if(show):
#             print('=========== Round', count, '===========')
#             print(shownTuple)
#             print('USER PICKED TUPLE', max_score_index+1)
#             print('------- New Bound for Z --------')
#             print(zBound)
#             print('                                      ')
#             print('                                      ')
#     return zBound


def main():
    iteration = 10
    f = randomPoly(1, 5)

    hB = find_h(f, 2, iteration)
    hL = find_l(hB, f, 2, iteration)
    hZ = find_z(f, 2, iteration)
    # hA = find_a(f, hB, hL, hZ, 2, iteration, True)

    print("Bound for H: ", hB)

    print("Bound for L: ", hL)

    print("Bound for Z: ", hZ)

    # print("Bound for Z: ", hA)

    print("Ui is: ", getUi(get_ave(hB), get_ave(hL), get_ave(hZ)))

    print("Mi_star is: ", getMiStar(get_ave(hL)))
    print(f)


if __name__ == "__main__":
    main()
