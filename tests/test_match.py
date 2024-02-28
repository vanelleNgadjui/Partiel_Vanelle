# tests/test_match.py
# Commande exec: python -m unittest discover -s tests -p "test_match.py"


import unittest
from Models.Match import Match


class TestMatch(unittest.TestCase):
    def setUp(self):
        # Créez des joueurs fictifs pour les tests
        self.player1 = {"first_name": "John", "last_name": "Doe"}
        self.player2 = {"first_name": "Jane", "last_name": "Doe"}

    def test_serialize(self):
        # Teste si la méthode serialize retourne le dictionnaire attendu
        match = Match(self.player1, self.player2)
        expected_dict = {
            "player1": self.player1,
            "player2": self.player2,
            "winner": None,
        }
        self.assertEqual(match.serialize(), expected_dict)

    def test_str_representation(self):
        # Teste si la représentation en chaîne du match est correcte
        match = Match(self.player1, self.player2)
        expected_str = "John Doe VS Jane Doe"
        self.assertEqual(str(match), expected_str)


if __name__ == "__main__":
    unittest.main()
