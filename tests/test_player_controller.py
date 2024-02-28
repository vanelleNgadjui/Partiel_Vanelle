# tests/test_player_controller.py
import unittest
from unittest.mock import patch
from io import StringIO
from Controllers.PlayerController import PlayerController


class TestPlayerController(unittest.TestCase):
    @patch("builtins.input", side_effect=["John", "Doe", "01/01/1990", "AB12345", "0"])
    def test_add_player(self, mock_input):
        # Teste si l'ajout d'un joueur fonctionne correctement
        player_controller = PlayerController()

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            player_controller.add_player()
            expected_output = "\nJoueur ajouté à la base de donnée avec succès !\n"
            self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == "__main__":
    unittest.main()

