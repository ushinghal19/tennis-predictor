from game import gameProbability
from sets import setProbability
from match import matchProbability
from scraper import playerScraper

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
    realPlayers = input("Would you like to check the match probability prediction of real players? (y/n) ")
    if realPlayers == 'y':
        withDeuce = True
        tryAgain = "y"
        player_one = input("Enter player 1's name (Ex: 'Rafael Nadal') here: ")
        player_two = input("Enter player 2's name (Ex: 'Novak Djokovic') here: ")
        players = playerScraper(player_one, player_two)
        players[player_one] = float(players[player_one][0:4])/100
        players[player_two] = float(players[player_two][0:4])/100
        print(players)

        while tryAgain == "y":
            score_type = input("What would you like to find the prediction probability for? (game, set, match) ")
            if score_type == "game":
                player_one_game_probability = gameProbability(withDeuce, players[player_one], players[player_two])
                print(f"{player_one} has a {player_one_game_probability} probability of winning a game against {player_two}")
                tryAgain = input("Want to calculate again? (y/n) ")
            elif score_type == "set":
                player_one_set_probability = setProbability(withDeuce, players[player_one], players[player_two])
                print(f"{player_one} has a {player_one_set_probability} probability of winning a set against {player_two}")
                tryAgain = input("Want to calculate again? (y/n) ")
            elif score_type == "match":
                player_one_match_probability = matchProbability(withDeuce, players[player_one], players[player_two])
                print(f"{player_one} has a {player_one_match_probability} probability of winning a match against {player_two}")
                tryAgain = input("Want to calculate again? (y/n) ")
            
        if tryAgain == "n":
            onceMore = input("Want to predict with new players? (y/n) ")
            if onceMore == "y":
                pass
            else:
                break
        
    if realPlayers == "n":
        goAgain = True
        
        while goAgain:
            withDeuce = input("Do you want to predict with the Deuce Scoring System (y/n) (If you choose 'n', it will be the Sudden-Death Scoring System) ")
            if withDeuce == 'y':
                withDeuce = True
            else:
                withDeuce = False

            player_one = input("What is the point probability of player one? ")
            player_two = input("What is the point probability of player two? ")
    
            # Checking if they entered a valid point-probability
            if type(player_one) != float or type(player_two) != float:
                print ("You must enter values between 0.0 and 1.0")
                goAgainInput = input("Do you want to try again? (y/n)")
                if goAgainInput == "y":
                    pass
                else:
                    print("Exiting")
                    break
        
            # Checking if both point-probabilities add up to 1.0
            if player_one + player_two!= 1.0:
                print ("Your probabilities must add up to 1.0")
                goAgainInput = input("Do you want to try again? (y/n)")
                if goAgainInput == "y":
                    pass
                else:
                    print("Exciting")
                    break
