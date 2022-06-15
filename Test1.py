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


def calc_a(atr1, atr2, ndp):
    s1 = {atr1: 2, atr2: 0} # Control Tuple
    s2 = {atr1: 1, atr2: 1} # Given Tuple 
    seta = [2]
    
    print("1.", s1) # Prints the initial choices for the user
    print("2.", s2) 
    
    """The following loop calculates a loose lower bound for a wrt the user"""    
    choice = False # We set the choice as False
    while(choice == False): # While the user does not find his bound, the loop keeps running
        s = input("Choose between the given tuples: ") # Takes input from user regarding their choice
        if(s == '1'):
            choice = True # If the user found their bound, we break the loop
            break
        else:
            s1[atr1] = s1[atr1] * 2 # Otherwise we increase the value for the given attribute
            seta.append(s1[atr1]) # Appending all the possible values we parsed through for the user
            
        print()
        print("1.", s1) # Repeatedly gives the user to make a choice as long as they do not find their upper bound
        print("2.", s2) 
        
    """Once the Loop is over, we get a loose lower bound on the a"""
    float a = s1[atr1]
    
    """The following loop narrows down the value of a by a half everytime as long as the user wants"""
    while(choice == True): # We narrow down the value atleast once before the uesr chooses 
        for chi in range(1,3): # Because we are narrowing it down by 2, we only keep the iteration from 1 to 2
            chi_j = seta[-2] + (chi*(a - seta[-2])/ndp) #Partitions the range into ndp equal parts to narrow down better
            temp = {atr1: chi_j, atr2: 0} # Creates the new tuple using the partitioned values
            print()
            if(chi_j != a): # Removes the reduntant case when the partitioned value is equal to the current value of a
                print("1.", temp)
                print("2.", s2)
                s = input("Choose between the given tuples: ")
                if(s == '1'):
                    a = chi_j # If the user chooses a lower bound for a, we update it and break the FOR loop
                    break
                else:
                    seta[-2] = chi_j # Otherwise we update our lower bound in the seta for the next iteration
                    
        print("Your current value for the attribute", atr1, "is", a) # Prints the latest value of a
        s = input("Would you like to narrow down the value of a? Press 0 for no. Anything else for yes. ")  # Asks the user if they want to narrow down the value of a further or not
        if(s == '0'):
            choice = False # Helps break the loop if the user chooses not to narrow down any further
    
    return a # Returns the value of a
