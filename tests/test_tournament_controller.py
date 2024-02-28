import unittest
from unittest.mock import patch, MagicMock
from Controllers.TournamentController import TournamentController
from Models.Tournament import Tournament


class TestTournamentController(unittest.TestCase):
    def setUp(self):
        self.tournament_controller = TournamentController()

    @patch("builtins.input", side_effect=["1"])
    def test_create_tournament(self, mock_input):
        # Mock la méthode get_new_id pour renvoyer une ID fictive
        Tournament.get_new_id = MagicMock(return_value=1)

        # Mock la méthode get_valid_date_input pour renvoyer une date fictive
        TournamentController.get_valid_date_input = MagicMock(return_value="01/01/2025")

        # Mock la méthode get_valid_alpha_input pour renvoyer un nom fictif
        TournamentController.get_valid_alpha_input = MagicMock(
            return_value="Tournament A"
        )

        # Exécute la méthode create_tournament
        self.tournament_controller.create_tournament()

        # Assertions
        self.assertTrue(Tournament.get_new_id.called)
        self.assertTrue(TournamentController.get_valid_date_input.called)
        self.assertTrue(TournamentController.get_valid_alpha_input.called)
