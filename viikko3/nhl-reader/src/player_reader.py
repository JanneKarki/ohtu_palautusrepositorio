import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_players(self):
        response = requests.get(self.url).json()
        players = []
        for player_dict in response:

            name = player_dict['name']
            team = player_dict['team']
            goals = player_dict['goals']
            assists = player_dict['assists']
            nationality = player_dict['nationality']
            points = goals + assists
            player = Player(
                            name,
                            team,
                            goals,
                            assists,
                            nationality,
                            points
                            )
            players.append(player)
            players.sort(key=lambda x: x.points, reverse=True)
        return players

