# Test1
Juste pour faire un test

Programme: calcul de l'indice de masse corporelle (IMC / BMI)

Fichiers ajoutés:
- `bmi.py` : module principal avec fonctions et petit CLI
- `tests/test_bmi.py` : tests unitaires (unittest)

Usage rapide (interactif):
1. Ouvrir un terminal dans le dossier du projet.
2. Lancer :

	python bmi.py

Le programme demandera le poids (kg) et la taille (m ou cm). Si vous fournissez
la taille en centimètres (par ex. 170), le programme convertira automatiquement
en mètres.

Pour lancer les tests unitaires:

1. Dans le terminal, exécuter:

	python -m unittest discover -v

ou exécuter le fichier de test:

	python -m unittest tests.test_bmi

