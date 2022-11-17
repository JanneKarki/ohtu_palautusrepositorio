from player_reader import PlayerReader
from player_stats import PlayerStats
import requests


def main():
    #print(dir(requests))
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"

    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")
    
    for player in players:
        print(player)


if __name__ == "__main__":
    main()