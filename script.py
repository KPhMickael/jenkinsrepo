# test_pylint.py

"""
Ce module contient des exemples de bonnes pratiques et des erreurs de style que pylint peut détecter.
Il inclut des exemples de fonctions simples, ainsi que des problèmes liés aux conventions de nommage et de style.
"""

def greet(name):
    """
    Cette fonction salue la personne passée en paramètre.

    Parameters:
    name (str): Le nom de la personne à saluer.
    """
    print('Hello, ' + name)

def calculate_sum(a, b):
    """Calculer la somme de deux nombres."""
    return a + b

# Exemple de fonction respectant les conventions de style
def sum_two_numbers():
    """
    Additionne deux nombres.

    Retourne la somme de 1 et 2.
    """
    a = 1
    b = 2
    return a + b

# Constante : utilise une variable en majuscules pour signaler qu'elle ne doit pas être modifiée.
UNUSED = 10

greet("World")
print(calculate_sum(5, 3))

# Cette fonction est définie mais jamais appelée, tu peux la supprimer ou l'utiliser.
def unused_function():
    """
    Fonction inutilisée, définie pour illustration.
    """
    pass

# La variable avec un nom trop long est divisée en deux lignes.
LONG_VARIABLE_NAME = (
    "Long string that exceeds the 80-character limit "
    "set by most style guidelines"
)
