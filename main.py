
''' This is a program, that will take two inputs
            - The probability that player A wins any given point in Tennis
            - The probability that player B wins any given point in Tennis
    and will return the probabilty that they (Player A) will win a 
            - Game in tennis
            - Set in tennis
            - Match in tennis
    There are additional options available, like choosing the type of match they are playing
    (ie: With Deuce, Without Deuce, Tiebreak, Etc)
'''
while True:
    playerOneProb = input("Enter Player One's Probability of Winning a Point here: ")
    playerTwoProb= input("Enter Player Two's Probability of Winning a Point here: ")

    # Checking if they entered a valid point-probability
    if type(player_one_pointProb) != float or type(player_one_pointProb) != float:
        print ("You must enter values between 0.0 and 1.0")
        goAgain = input("Do you want to try again? (y/n)")
        if goAgain == "y":
            pass
        else:
            print("Exciting")
            break
    
    # Checking if both point-probabilities add up to 1.0
    if player_one_pointProb + player_two_pointProb != 1.0:
        print ("Your probabilities must add up to 1.0")
        tryAgain = input("Do you want to try again? (y/n)")
        if tryAgain == "y":
            pass
        else:
            print("Exciting")
            break
