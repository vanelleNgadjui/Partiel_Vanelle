# tests/test_menu.py
# Commande exec: python -m unittest discover -s tests -p "test_menu.py"


import unittest
from unittest.mock import patch
from io import StringIO
from Views.Menu import Menu


class TestMenu(unittest.TestCase):
    def setUp(self):
        # Créez une instance de Menu pour les tests
        self.menu = Menu()

    @patch("builtins.input", return_value="1")
    def test_main_menu_add_player(self, mock_input):
        # Teste si le menu principal affiche correctement le choix d'ajouter un joueur
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.menu.main_menu()
            expected_output = "\n========CHESS TOURNAMENT MANAGER========\n\n--- MENU ---\n1. Ajouter un joueur\n2. Créer un tournoi\n3. Ajouter des joueurs à un tournoi\n4. Lancer un Round\n5. Rapports\n0. Quitter\n\nEntrez le numéro correspondant à votre choix : "
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    # Ajoutez des tests similaires pour les autres choix du menu principal

    @patch("builtins.input", return_value="3")
    def test_report_menu_add_tournament_players(self, mock_input):
        # Teste si le menu des rapports affiche correctement le choix d'ajouter des joueurs à un tournoi
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.menu.report_menu()
            expected_output = "\nMenu des rapports:\n1. Liste des joueurs par ordre alphabétique\n2. Liste des tous les Tournois\n3. Informations d'un Tournoi\n4. Liste des joueurs d'un Tournoi\n5. Détails d'un Tournoi\n0. Retourner au menu principal\n\nEntrez le numéro correspondant à votre choix : "
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    # Ajoutez des tests similaires pour les autres choix du menu de rapport


if __name__ == "__main__":
    unittest.main()
