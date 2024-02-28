import unittest
from unittest.mock import patch, MagicMock
from Controllers.RoundsController import RoundController
from Models.Rounds import Round


class TestRoundController(unittest.TestCase):
    def setUp(self):
        self.round_controller = RoundController()

    @patch("builtins.input", side_effect=["1"])
    def test_play_round(self, mock_input):
        # Mock la méthode select_tournament_from_list pour renvoyer un tournoi fictif
        RoundController.select_tournament_from_list = MagicMock(
            return_value={
                "id": 1,
                "name": "Tournament A",
                "player_list": [
                    {
                        "first_name": "Alice",
                        "last_name": "Smith",
                        "national_chess_id": "12345",
                    },
                    {
                        "first_name": "Bob",
                        "last_name": "Johnson",
                        "national_chess_id": "67890",
                    },
                ],
            }
        )

        # Mock la méthode select_round_from_list pour renvoyer un round fictif
        RoundController.select_round_from_list = MagicMock(
            return_value={
                "round_number": 1,
                "round_name": "Round 1",
                "matches": [{"player1": "Alice", "player2": "Bob"}],
            }
        )

        # Mock la méthode play_match pour renvoyer un résultat fictif
        RoundController.play_match = MagicMock(
            return_value={
                "player1": "Alice",
                "player2": "Bob",
                "score1": 1,
                "score2": 0,
            }
        )

        # Exécute la méthode play_round
        self.round_controller.play_round()

        # Assertions
        self.assertTrue(RoundController.select_tournament_from_list.called)
        self.assertTrue(RoundController.select_round_from_list.called)
        self.assertTrue(RoundController.play_match.called)


if __name__ == "__main__":
    unittest.main()
