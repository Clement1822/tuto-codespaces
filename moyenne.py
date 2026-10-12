"""Ce module fournit une fonction pour calculer une moyenne de valeurs"""

# NB: Ce fichier contient du code à compléter

from rich.console import Console
from rich.markdown import Markdown


def moyenne(valeurs):
    """Code moyenne"""
    if len(valeurs) == 0:
        raise ValueError
    compteur = 0
    for element in valeurs:
        compteur = compteur + element
    return compteur / (len(valeurs))


print("!! TODO : Compléter la fonction moyenne !!", end=" ")


if __name__ == "__main__":
    Console().print(Markdown(moyenne.__doc__))
    print("moyenne([10, 20, 15]) :", end=" ")
    print(moyenne([10, 20, 15]))
