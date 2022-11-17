from player import Player
import requests
import datetime


def main():
    #print(dir(requests))
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    response = requests.get(url).json()

    #print("JSON-muotoinen vastaus:")
    #print(response)

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
                        points
                        )
        if nationality == "FIN":
            players.append(player)
 
    print("Players from FIN" + " " + str(datetime.datetime.now()))
    players.sort(key=lambda x: x.points, reverse=True)
    for player in players:
        print(player)

if __name__ == "__main__":
    main()

