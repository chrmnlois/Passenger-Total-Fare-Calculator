# San Antonio, Charmaine Lois A. BSIT 2-5 (SET A)
# With Exception Handling

# == FUNCTIONS ==
def student():
    try:    #exception handling for km input
        distance = int(input("Enter distance in km: "))
        print("\nPassenger is a STUDENT")
        if distance > 4:    #formula for total fare when distance traveled > 4km
            SK = float(distance - 4)
            Total_Fare = SK + 7
            print("Total Fare: Php ", Total_Fare)
        else:
            print("Total Fare: Php 7.00")   #displayed when distance traveled is < 4km
    except ValueError as e:
        print("\nERROR FOUND!\nPlease enter a numeric value.", type(e))
    except Exception as e:
        print("\nERROR FOUND!\nPlease enter a numeric value.", type(e))

def elderly():
    try:    #exception handling for km input
        distance = int(input("Enter distance in km: "))
        print("\nPassenger is an ELDERLY")
        if distance > 4:    #formula for total fare when distance traveled > 4km
            SK = float(distance - 4)
            Total_Fare = SK + 7
            print("Total Fare: Php ", Total_Fare)
        else:
            print("Total Fare: Php 7.00")   #displayed when distance traveled is < 4km
    except ValueError as e:
        print("\nERROR FOUND!\nPlease enter a numeric value.", type(e))
    except Exception as e:
        print("\nERROR FOUND!\nPlease enter a numeric value.", type(e))

def pwd():
    try:    #exception handling for km input
        distance = int(input("Enter distance in km: "))
        print("\nPassenger is a PERSON WITH DISABILITY")
        if distance > 4:    #formula for total fare when distance traveled > 4km
            SK = float(distance - 4)
            Total_Fare = SK + 7
            print("Total Fare: Php ", Total_Fare)   #displayed when distance traveled is < 4km
        else:
            print("Total Fare: Php 7.00")
    except ValueError as e:
        print("\nERROR FOUND!\nPlease enter a numeric value.", type(e))
    except Exception as e:
        print("\nERROR FOUND!\nPlease enter a numeric value.", type(e))

def reg():
    try:    #exception handling for km input
        distance = int(input("Enter distance in km: "))
        print("\nRegular Passenger")
        if distance > 4:    #formula for total fare when distance traveled > 4km
            SK = float(distance - 4)
            Total_Fare = SK + 9
            print("Total Fare: Php ", Total_Fare)
        else:
            print("Total Fare: Php 9.00")   #displayed when distance traveled is < 4km
    except ValueError as e:
        print("\nERROR FOUND!\nPlease enter a numeric value.", type(e))
    except Exception as e:
        print("\nERROR FOUND!\nPlease enter a numeric value.", type(e))

# == MAIN PROGRAM ==
choice = ''     #define variable 'choice'
while choice.upper() != 'N':       #if choice.upper = 'N', the program will end

    try:    #exception handling for passenger type
        passenger_type = input("\nEnter passenger type: ")
        if passenger_type.isdigit():
            raise ValueError    #if passenger type is a digit, it will raise an error
    except ValueError as e:
        print("\nERROR FOUND!\nPlease enter a string input.", type(e))

    if passenger_type.isalpha():    #if passenger type is an alphabet, it will execute these if-else statements
        if passenger_type == 'S' or passenger_type == 's':
            student()   #call 'student' function
        elif passenger_type == 'E' or passenger_type == 'e':
            elderly()   #call 'elderly' function
        elif passenger_type == 'D' or passenger_type == 'd':
            pwd()   #call 'pwd' function
        elif passenger_type == 'R' or passenger_type == 'r':
            reg()   #call 'reg' function
        else:   #displayed if passenger type is not 's', 'e', 'd', 'r'
            print("\nINVALID PASSENGER TYPE!\nTotal Fare: = Php 0.00")

    ans = '' #define variable 'ans'
    while ans != 'n':   #if ans = 'n', this loop will stop and will go back to the first while loop
        try:    #exception handling for choice option
            choice = input("\nContinue? : ")[0]   #index[0]: just the first index of the input will be processed
            if choice.isdigit():
                 raise ValueError   #if choice is a digit, it will raise an error
        except ValueError as e:
            print("\nERROR FOUND!\nPlease enter 'Yes' or 'No'.", type(e))
            ans = 'y'   #if this exception is executed, ans variable will still be 'y' so the loop will not end

        if choice.isalpha():    #if passenger type is an alphabet, it will execute these if-else statements
            if choice == 'n' or choice == 'N':
                choice.upper()
                ans = 'n'   #from ans = 'y', it will now be equal to 'n'. this while loop will stop.
            elif choice == 'y' or choice == 'Y':
                choice.upper()
                ans = 'n'   #from ans = 'y', it will now be equal to 'n'. this while loop will stop.
                print('\n' * 5)     #clear screen purposes
            else: #displayed if choice is not between yes or no
                print("INVALID INPUT! Please enter 'Yes' or 'No'")

print("\n == END OF PROGRAM ==")