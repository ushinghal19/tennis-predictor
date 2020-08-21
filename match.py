from math import comb
from sets import setProbability as sp

def matchProbability(withDeuce, p1, p2):
    # Player 1's set probability
    sp1 = sp(withDeuce, p1, p2)
    # Player 2's set proboability
    sp2 = sp(withDeuce, p1, p2)
    # Player 1 wins 3 sets and wins the match
    p1_w3 = sp1**3
    # Player 1 wins 3 sets and loses 1
    p1_w3_l1 = comb(3,1) * (sp1 ** 3) * (sp2)
    # Player 1 wins 3 sets and loses 2
    p1_w3_l2 = comb(4,2) * (sp1 ** 3) * (sp2)

    p1_win = p1_w3 + p1_w3_l1 + p1_w3_l2

    return p1_win
