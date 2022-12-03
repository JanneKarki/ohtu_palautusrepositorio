
LOVE = "Love"
FIFTEEN = "Fifteen"
THIRTY = "Thirty"
FORTY = "Forty"

LOVE_ALL = "Love-All"
FIFTEEN_ALL = "Fifteen-All"
THIRTY_ALL = "Thirty-All"
FORTY_ALL = "Forty-All"
DEUCE = "Deuce"

ADV1 = "Advantage player1"
ADV2 = "Advantage player2"
WIN1 = "Win for player1"
WIN2 = "Win for player2"

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1


    def get_score(self):
        score = ""

        if self.player1_score == self.player2_score:
            score = self.scores_are_equal(self.player1_score)
           
        elif self.player1_score >= 4 or self.player2_score >= 4:
            score = self.both_scores_are_at_least_four(score)
            
        else:
            score = self.check_scores(score)
            
        return score

    def check_scores(self, score):
        temp_score = 0
        for player in range(1, 3):
                if player == 1:
                    temp_score = self.player1_score
                else:
                    score = score + "-"
                    temp_score = self.player2_score

                if temp_score == 0:
                    score = score + LOVE
                elif temp_score == 1:
                    score = score + FIFTEEN
                elif temp_score == 2:
                    score = score + THIRTY
                elif temp_score == 3:
                    score = score + FORTY
        return score


    def scores_are_equal(self, player_scores):

        if player_scores == 0:
            score = LOVE_ALL
        elif player_scores == 1:
            score = FIFTEEN_ALL
        elif player_scores == 2:
            score = THIRTY_ALL
        elif player_scores == 3:
            score = FORTY_ALL
        else:
            score = DEUCE
        
        return score

    def both_scores_are_at_least_four(self, score):
        score_difference = self.player1_score - self. player2_score

        if score_difference == 1:
            score = ADV1
        elif score_difference == -1:
            score = ADV2
        elif score_difference >= 2:
            score = WIN1
        else:
            score = WIN2
        
        return score