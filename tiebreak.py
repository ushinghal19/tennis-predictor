from math import comb

def tiebreakProbability(p1, p2):
    # This is a 7 point tiebreak that occurs when the set score is 6-6
    # Player 1 wins 7 points in a row
    p1_w7 = p1 ** 7
    # Player 1 wins 7 points and loses 1
    p1_w7_l1 = comb(7,1) * (p1**7) * (p2)
    # Player 1 wins 7 points and loses 2
    p1_w7_l2 = comb(8,2) * (p1**7) * (p2**2)
    # Player 1 wins 7 points and loses 3
    p1_w7_l3 = comb(9,3) * (p1**7) * (p2**3)
    # Player 1 wins 7 points and loses 4
    p1_w7_l4 = comb(10,4) * (p1**7) * (p2**4)
    # Player 1 wins 7 points and loses 5
    p1_w7_l5 = comb(11,5) * (p1**7) * (p2**5)
    # Both players win 6 points each
    p1_w6_l6 = comb(12,6) * (p1**6) * (p2**6)
    # To win the tiebreak, player 1 must win two more points
    # But there is also a chance that both players win a point,
    # and the game goes back to deuce.
    p1_w6_l6_w2 = ((p1**2) / (1-2*(p1*p2))) * p1_w6_l6
    # Hence, the probability that Player 1 wins the tiebreak is:
    p1_win = p1_w7 + p1_w7_l1 + p1_w7_l2 + p1_w7_l3 + p1_w7_l4 + p1_w7_l5 + p1_w6_l6_w2 

    return p1_win
