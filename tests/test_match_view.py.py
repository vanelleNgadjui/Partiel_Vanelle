# tests/test_match_view.py
# Commande exec: python -m unittest discover -s tests -p "test_match_view.py"


import unittest
from unittest.mock import patch
from io import StringIO
from Views.MatchView import MatchView
from Models.Match import Match


class TestMatchView(unittest.TestCase):
    def setUp(self):
        # Créez une instance de MatchView pour les tests
        self.match_view = MatchView()

        # Créez des joueurs fictifs pour les tests
        self.player1 = {"first_name": "John", "last_name": "Doe"}
        self.player2 = {"first_name": "Jane", "last_name": "Doe"}

        # Créez un match fictif pour les tests
        self.match = Match(self.player1, self.player2)

    def test_display_match_results(self):
        # Teste si l'affichage des résultats d'un match fonctionne correctement
        with patch("builtins.input", return_value="1"), patch(
            "sys.stdout", new_callable=StringIO
        ) as mock_stdout:
            choice = self.match_view.display_match_results(self.match, 1, 2)
            expected_output = (
                "Match 1 Round 2 - Résultats\n1 - John Doe\n2 - Jane Doe\n3 - égalité\n"
            )
            self.assertEqual(mock_stdout.getvalue(), expected_output)
            self.assertEqual(choice, 1)

    def test_get_user_choice(self):
        # Teste si la récupération du choix de l'utilisateur fonctionne correctement
        with patch("builtins.input", return_value="2"), patch(
            "sys.stdout", new_callable=StringIO
        ):
            choice = self.match_view.get_user_choice()
            self.assertEqual(choice, 2)

        with patch("builtins.input", side_effect=["invalid", "3"]), patch(
            "sys.stdout", new_callable=StringIO
        ) as mock_stdout:
            choice = self.match_view.get_user_choice()
            expected_output = "Entrée invalide. Veuillez entrer un numéro.\n"
            self.assertEqual(mock_stdout.getvalue(), expected_output)
            self.assertEqual(choice, 3)


if __name__ == "__main__":
    unittest.main()
