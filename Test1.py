import random
# GLOBAL VARIABLES
s = 2 #NUMBER OF TUPLES TO SHOW
d = 2 #NUMBER OF ATTRIBUTES TO SHOW


def PolyFunction(lowestDeg, highestDeg, n=2):
    function = [[random.random(),random.randint(lowestDeg,highestDeg)] for i in range(n)]
    

    return function


def main():
    print(PolyFunction(1,10))

if __name__ == "__main__":
    main()


def calc_a(Atr1, Atr2):
    s1 = {Atr1: 1, Atr2: 0}
    s2 = {Atr1: 1, Atr2: 1}

    choice = False
    while(choice == False):
        print(s1)
        print(s2)
        s = input("Choose between the above tuples: ")
        if(s == 1):
            choice = True
        else:
            s1[Atr1] = s1[Atr1] * 2
