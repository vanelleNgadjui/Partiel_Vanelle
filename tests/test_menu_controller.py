# tests/test_menu_controller.py
# Commande exec: python -m unittest discover -s tests -p "test_menu_controller.py"


import unittest
from unittest.mock import patch
from io import StringIO
from Controllers.MenuController import MenuController

class TestMenuController(unittest.TestCase):
    def setUp(self):
        # Créez une instance de MenuController pour les tests
        self.menu_controller = MenuController()

    @patch('builtins.input', side_effect=['1', '0'])
    def test_user_choice_add_player(self, mock_input):
        # Teste si le choix d'ajouter un joueur fonctionne correctement
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.menu_controller.user_choice()
            expected_output = "1. Ajouter un joueur\n2. Créer un tournoi\n3. Ajouter des joueurs à un tournoi\n4. Lancer un Round\n5. Rapports\n0. Quitter\n"
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    # Ajoutez des tests similaires pour les autres choix du menu principal et les cas invalides

    @patch('builtins.input', side_effect=['5', '0'])
    def test_user_choice_report_menu(self, mock_input):
        # Teste si le choix du menu de rapport fonctionne correctement
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.menu_controller.user_choice()
            expected_output = "1. Liste des joueurs par ordre alphabétique\n2. Liste des tous les Tournois\n3. Informations d'un Tournoi\n4. Liste des joueurs d'un Tournoi\n5. Détails d'un Tournoi\n0. Retourner au menu principal\n"
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    # Ajoutez des tests similaires pour les autres choix du menu de rapport et les cas invalides

if __name__ == '__main__':
    unittest.main()
