from math import comb
from game import gameProbability as gp
from tiebreak import tiebreakProbability as tp

def setProbability(withDeuce, p1, p2):
    if withDeuce:
        # Player 1's game probability:
        gp1 = gp(True, p1, p2)
        # Player 2's game probability:
        gp2 = 1-gp1
        # Player 1 wins 6 games in a row
        p1_w6 = gp1 ** 6
        # Player 1 wins 6 games and loses 1
        p1_w6_l1 = comb(6,1) * (gp1 ** 6) * (gp2)
        # Player 1 wins 6 games and loses 2
        p1_w6_l2 = comb(7,2) * (gp1 ** 6) * (gp2**2)
        # Player 1 wins 6 games and loses 3
        p1_w6_l3 = comb(8,3) * (gp1 ** 6) * (gp2**3)
        # Player 1 wins 6 games and loses 4
        p1_w6_l4 = comb(9,4) * (gp1 ** 6) * (gp2**4)
        # Both players win 5 games, and Player 1 wins two games in a row
        p1_w5_l5_w2 = comb(10,5) * (gp1 ** 5) * (gp2 ** 5) * (gp1 ** 2)
        # Both players win 5 games, then each win 1 more game, taking the set to a tiebreak of 7 points
        p1_win_tp = tp(p1, p2)
        # Therefore, the probability that Player 1 and Player 2 both win a game at 5-5, and Player 1 wins the tiebreak is:
        p1_w6_l6_win_tp = comb(10,5) * (gp1 ** 5) * (gp2 ** 5) * 2 * (gp1) * (gp2) * p1_win_tp 
        # Hence, the probability that Player 1 wins the tiebreak is:
        p1_win = p1_w6 + p1_w6_l1 + p1_w6_l2 + p1_w6_l3 + p1_w6_l4 + p1_w5_l5_w2 + p1_w6_l6_win_tp

        return p1_win

    if not withDeuce:
        # Player 1's game probability:
        gp1 = gp(False, p1, p2)
        # Player 2's game probability:
        gp2 = 1-gp1
        # Player 1 wins 6 games in a row
        p1_w6 = gp1 ** 6
        # Player 1 wins 6 games and loses 1
        p1_w6_l1 = comb(6,1) * (gp1 ** 6) * (gp2)
        # Player 1 wins 6 games and loses 2
        p1_w6_l2 = comb(7,2) * (gp1 ** 6) * (gp2**2)
        # Player 1 wins 6 games and loses 3
        p1_w6_l3 = comb(8,3) * (gp1 ** 6) * (gp2**3)
        # Player 1 wins 6 games and loses 4
        p1_w6_l4 = comb(9,4) * (gp1 ** 6) * (gp2**4)
        # Both players win 5 games, and Player 1 wins two games in a row
        p1_w5_l5_w2 = comb(10,5) * (gp1 ** 5) * (gp2 ** 5) * (gp1 ** 2)
        # Both players win 5 games, then each win 1 more game, taking the set to a tiebreak of 7 points
        p1_win_tp = tp(p1, p2)
        # Therefore, the probability that Player 1 and Player 2 both win a game at 5-5, and Player 1 wins the tiebreak is:
        p1_w6_l6_win_tp = comb(10,5) * (gp1 ** 5) * (gp2 ** 5) * 2 * (gp1) * (gp2) * p1_win_tp 
        # Hence, the probability that Player 1 wins the tiebreak is:
        p1_win = p1_w6 + p1_w6_l1 + p1_w6_l2 + p1_w6_l3 + p1_w6_l4 + p1_w5_l5_w2 + p1_w6_l6_win_tp

        return p1_win

print(setProbability(True, 0.6, 0.4))
print(setProbability(True, 0.4, 0.6))
print(setProbability(False, 0.6, 0.4))
print(setProbability(False, 0.4, 0.6))


