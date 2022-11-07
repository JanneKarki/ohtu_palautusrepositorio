import unittest
from statistics import Statistics
from player import Player
from statistics import SortBy

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_search_player(self):
        player = self.statistics.search("Kurri").name
        self.assertEqual(player, "Kurri")
  
    def test_top_results(self):
        list = self.statistics.top(3)
        self.assertEqual(list[0].team,"EDM")

    def test_team_size(self):
        team = self.statistics.team("EDM")
        self.assertEqual(len(team), 3)

    def test_player_not_found_returns_none(self):
        player = self.statistics.search("Seppo")
        self.assertEqual(player, None)

    def test_most_goal_points(self):
        player = self.statistics.top(2, SortBy.GOALS)[0].name
        self.assertEqual(player, "Lemieux")
    
    def test_most_assist_points(self):
        player = self.statistics.top(2, SortBy.ASSISTS)[0].name
        self.assertEqual(player, "Gretzky")

