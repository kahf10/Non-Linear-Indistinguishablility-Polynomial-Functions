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
