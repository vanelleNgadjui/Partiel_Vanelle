# tests/test_player_view.py
import unittest
from unittest.mock import patch
from io import StringIO
from Views.PlayerView import PlayerView


class TestPlayerView(unittest.TestCase):
    @patch("builtins.input", side_effect=["John", "Doe", "01/01/1990", "AB12345"])
    def test_get_player_info(self, mock_input):
        # Teste si la méthode get_player_info fonctionne correctement
        player_view = PlayerView()

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            result = player_view.get_player_info()
            expected_output = ""
            # Ajoutez des assertions en fonction de votre structure de données attendue


if __name__ == "__main__":
    unittest.main()
