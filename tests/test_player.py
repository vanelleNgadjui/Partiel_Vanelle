# tests/test_player.py
import unittest
from Models.Player import Player
import json
import os


class TestPlayer(unittest.TestCase):
    def setUp(self):
        # Création d'une instance de Player pour les tests
        self.player = Player("John", "Doe", "01/01/1990", "AB12345")

    def tearDown(self):
        # Suppression du fichier players.json après chaque test
        if os.path.exists("data/players.json"):
            os.remove("data/players.json")

    def test_save_player(self):
        # Teste si la méthode save_player fonctionne correctement
        self.player.save_player()

        # Vérifie si le fichier players.json a été créé
        self.assertTrue(os.path.exists("data/players.json"))

        # Charge le fichier pour vérifier le contenu
        with open("data/players.json", "r") as file:
            players = json.load(file)

        # Ajoutez des assertions en fonction de votre structure de données attendue
        self.assertEqual(len(players), 1)
        self.assertEqual(players[0]["first_name"], "John")
        # Ajoutez d'autres assertions

    def test_get_players_existing_file(self):
        # Teste si la méthode get_players renvoie une liste de joueurs depuis le fichier existant
        self.player.save_player()
        players = self.player.get_players()

        # Ajoutez des assertions en fonction de votre structure de données attendue
        self.assertEqual(len(players), 1)
        self.assertEqual(players[0]["first_name"], "John")
        # Ajoutez d'autres assertions

    def test_get_players_nonexistent_file(self):
        # Teste si la méthode get_players renvoie un message d'erreur pour un fichier inexistant
        players = self.player.get_players()

        # Ajoutez des assertions en fonction du comportement attendu
        self.assertEqual(players, "Fichier players.json introuvable")

    def test_get_new_id_existing_file(self):
        # Teste si la méthode get_new_id renvoie le bon nouvel ID pour un fichier existant
        self.player.save_player()
        new_id = self.player.get_new_id("data/players.json")

        # Ajoutez des assertions en fonction du comportement attendu
        self.assertEqual(
            new_id, 2
        )  # Si un joueur est déjà enregistré, le nouvel ID doit être le dernier ID + 1

    def test_get_new_id_nonexistent_file(self):
        # Teste si la méthode get_new_id renvoie 1 pour un fichier inexistant
        new_id = self.player.get_new_id("data/nonexistent.json")

        # Ajoutez des assertions en fonction du comportement attendu
        self.assertEqual(new_id, 1)


if __name__ == "__main__":
    unittest.main()
