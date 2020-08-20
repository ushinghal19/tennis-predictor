
from math import comb

def gameProbability(withDeuce, p1, p2):
    if withDeuce:
        # Probability that player 1 wins four points in a row
        p1_w4 = (p1)**4
        # Probability that player 1 wins four points, and loses one
        p1_w4_l1 = comb(4,1) * (p1**4) * (p2)
        # Probability that player 1 wins four points, and loses two
        p1_w4_l2 = comb(5,2) * (p1**4) * (p2**2)
        # If they both win 3 points, then the game goes to Deuce. 
        p1_w3_l3 = comb(6,3) * (p1**3) * (p2**3)
        # Then, to win the game, PLayer 1 must win both points. 
        # But there is also a chance that both players win a point,
        # and the game goes back to deuce.
        p1_w3_l3_w2 = (p1**2) / (1-(2*p1*p2)) * p1_w3_l3
        #Thus, the final probability of Player 1 winning the game is:
        p1_win = p1_w4 + p1_w4_l1 + p1_w4_l2 + p1_w3_l3_w2
        
        return p1_win

    if not withDeuce:
        # Probability that player 1 wins four points in a row
        p1_w4 = (p1)**4
        # Probability that player 1 wins four points, and loses one
        p1_w4_l1 = comb(4,1) * (p1**4) * (p2)
        # Probability that player 1 wins four points, and loses two
        p1_w4_l2 = comb(5,2) * (p1**4) * (p2**2)
        # If they both win 3 points, then the game goes to Deuce. 
        p1_w3_l3 = comb(6,3) * (p1**3) * (p2**3)
        # To win the game, Player 1 must just win the next point
        p1_w3_l3_w1 = p1_w3_l3 * p1
        #Thus, the final probability of Player 1 winning the game is:
        p1_win = p1_w4 + p1_w4_l1 + p1_w4_l2 + p1_w3_l3_w1

        return p1_win

        