# tests/test_report_controller.py

import unittest
from unittest.mock import patch, MagicMock
from Controllers.ReportController import ReportController
from Models.Report import Report


class TestReportController(unittest.TestCase):
    def setUp(self):
        self.report_controller = ReportController()

    @patch("builtins.input", side_effect=["1"])
    def test_players_alphabetical(self, mock_input):
        # Mock la méthode load_players pour renvoyer une liste fictive de joueurs
        Report.load_players = MagicMock(
            return_value=[
                {"first_name": "Alice", "last_name": "Smith"},
                {"first_name": "Bob", "last_name": "Johnson"},
                {"first_name": "Charlie", "last_name": "Brown"},
            ]
        )

        sorted_players = self.report_controller.players_alphabetical()

        # Assertions
        self.assertTrue(Report.load_players.called)
        self.assertEqual(sorted_players[0]["first_name"], "Alice")
        self.assertEqual(sorted_players[1]["last_name"], "Johnson")

    @patch("builtins.input", side_effect=["1"])
    def test_list_tournaments(self, mock_input):
        # Mock la méthode load_tournaments pour renvoyer une liste fictive de tournois
        Report.load_tournaments = MagicMock(
            return_value=[
                {"name": "Tournament A"},
                {"name": "Tournament B"},
                {"name": "Tournament C"},
            ]
        )

        tournaments = self.report_controller.list_tournaments()

        # Assertions
        self.assertTrue(Report.load_tournaments.called)
        self.assertEqual(tournaments[0]["name"], "Tournament A")
        self.assertEqual(len(tournaments), 3)

    @patch("builtins.input", side_effect=["2"])
    def test_select_tournament_from_list(self, mock_input):
        # Mock la méthode load_tournaments pour renvoyer une liste fictive de tournois
        Report.load_tournaments = MagicMock(
            return_value=[
                {"name": "Tournament A"},
                {"name": "Tournament B"},
                {"name": "Tournament C"},
            ]
        )

        # Mock la fonction input pour simuler la sélection de l'utilisateur
        with patch("builtins.input", side_effect=["2"]):
            selected_tournament = self.report_controller.select_tournament_from_list()

        # Assertions
        self.assertTrue(Report.load_tournaments.called)
        self.assertEqual(selected_tournament["name"], "Tournament B")

    @patch("builtins.input", side_effect=["1"])
    def test_tournament_players_alphabetical(self, mock_input):
        # Mock la méthode select_tournament_from_list pour renvoyer un tournoi fictif
        ReportController.select_tournament_from_list = MagicMock(
            return_value={
                "player_list": [
                    {"first_name": "Alice", "last_name": "Smith"},
                    {"first_name": "Bob", "last_name": "Johnson"},
                    {"first_name": "Charlie", "last_name": "Brown"},
                ]
            }
        )

        sorted_players = self.report_controller.tournament_players_alphabetical()

        # Assertions
        self.assertTrue(ReportController.select_tournament_from_list.called)
        self.assertEqual(sorted_players[0]["first_name"], "Alice")
        self.assertEqual(sorted_players[1]["last_name"], "Johnson")


if __name__ == "__main__":
    unittest.main()
