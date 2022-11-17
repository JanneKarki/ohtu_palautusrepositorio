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

        player = Player(
                        name,
                        team,
                        goals,
                        assists
                        )
        if nationality == "FIN":
            players.append(player)
 
    print("Players from FIN" + " " + str(datetime.datetime.now()))

    for player in players:
        print(player)

if __name__ == "__main__":
    main()

