from player import Player

class PlayerStats:

    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self,nationality):
        result = []
        players = self.reader.get_players()
        for i in players:
            if i.nationality == nationality:
                result.append(i)
        return result