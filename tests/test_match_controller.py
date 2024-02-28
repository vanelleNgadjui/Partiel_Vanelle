# tests/test_match_controller.py
# Commande exec: python -m unittest discover -s tests -p "test_match_controller.py"


import unittest
from Controllers.MatchController import MatchController
from Models.Match import Match


class TestMatchController(unittest.TestCase):
    def setUp(self):
        # Créez une instance de MatchController pour les tests
        self.match_controller = MatchController()

        # Créez des joueurs fictifs pour les tests
        self.player1 = {"first_name": "John", "last_name": "Doe"}
        self.player2 = {"first_name": "Jane", "last_name": "Doe"}
        self.player3 = {"first_name": "Alice", "last_name": "Smith"}
        self.player4 = {"first_name": "Bob", "last_name": "Johnson"}

    def test_create_match_pairs(self):
        # Teste si la création de paires de joueurs fonctionne correctement
        players = [self.player1, self.player2, self.player3, self.player4]
        expected_pairs = [((self.player1, self.player2), (self.player3, self.player4))]
        self.assertEqual(
            self.match_controller.create_match_pairs(players), expected_pairs
        )

    def test_create_matches(self):
        # Teste si la création de matches à partir de paires de joueurs fonctionne correctement
        pairs = [((self.player1, self.player2), (self.player3, self.player4))]
        expected_matches = [
            Match(self.player1, self.player2),
            Match(self.player3, self.player4),
        ]
        matches = self.match_controller.create_matches(pairs)
        for match, expected_match in zip(matches, expected_matches):
            self.assertEqual(match.serialize(), expected_match.serialize())

    def test_pair_players(self):
        # Teste si l'appariement de joueurs fonctionne correctement
        sorted_players = [self.player1, self.player2, self.player3, self.player4]
        played_matches = []  # Aucun match joué jusqu'à présent
        paired_players = self.match_controller.pair_players(
            sorted_players, played_matches
        )

        # Assurez-vous que chaque joueur est apparié avec un adversaire différent
        for pair in paired_players:
            self.assertNotEqual(pair[0], pair[1])

    def test_has_played_together(self):
        # Teste si la vérification des matches déjà joués ensemble fonctionne correctement
        match1 = Match(self.player1, self.player2)
        match2 = Match(self.player3, self.player4)
        played_matches = [[match1], [match2]]

        # Les joueurs de match1 ont déjà joué ensemble, mais pas ceux de match2
        self.assertTrue(
            self.match_controller.has_played_together(
                self.player1, self.player2, played_matches
            )
        )
        self.assertFalse(
            self.match_controller.has_played_together(
                self.player3, self.player4, played_matches
            )
        )


if __name__ == "__main__":
    unittest.main()
