
LOVE = "Love"
FIFTEEN = "Fifteen"
THIRTY = "Thirty"
FORTY = "Forty"

LOVEALL = "Love-All"
FIFTEENALL = "Fifteen-All"
THIRTYALL = "Thirty-All"
FORTYALL = "Forty-All"
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
        temp_score = 0

        if self.player1_score == self.player2_score:
            score = self.scores_are_equal(score)
           
        elif self.player1_score >= 4 or self.player2_score >= 4:
            score = self.both_scores_are_at_least_four(score)
            
        else:
            for i in range(1, 3):
                if i == 1:
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

    def scores_are_equal(self, score):

        if self.player1_score == 0:
            score = LOVEALL
        elif self.player1_score == 1:
            score = FIFTEENALL
        elif self.player1_score == 2:
            score = THIRTYALL
        elif self.player1_score == 3:
            score = FORTYALL
        else:
            score = DEUCE
        
        return score

    def both_scores_are_at_least_four(self, score):
        minus_result = self.player1_score - self. player2_score

        if minus_result == 1:
            score = ADV1
        elif minus_result == -1:
            score = ADV2
        elif minus_result >= 2:
            score = WIN1
        else:
            score = WIN2
        
        return score