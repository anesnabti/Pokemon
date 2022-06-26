# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 19:30:24 2021

@author: Anes NABTI
         Youcef CHORFI  **Update
"""

from Readfile import Readfile
from Competence import Competence
import numpy as np


class Attaque(Competence):

    # =============================================================================

    def __init__(self, nom):
        self.nom = nom
        # Si la compétence est de type attaque on initialise le reste des attributs
        if self.type():
            self.description = (Readfile("attaque")['Description'][Readfile("attaque")['Nom'].index(nom)])
            self.element = (Readfile("attaque")['Element'][Readfile("attaque")['Nom'].index(nom)])
            self.cout = float((Readfile("attaque")['Cout'][Readfile("attaque")['Nom'].index(nom)]))
            self.puissance = float((Readfile("attaque")['Puissance'][Readfile("attaque")['Nom'].index(nom)]))
            self.precision = float((Readfile("attaque")['Precision'][Readfile("attaque")['Nom'].index(nom)]))

    # =============================================================================

    def __str__(self):
        return f"Competence attaque '{self.nom}' : {self.description} Element : {self.element}, Puissance : {self.puissance}, Precision : {self.precision}, Cout : {self.cout} "

    # =============================================================================

    # methods
    # =============================================================================

    # Type de la competence : True si attaque
    def type(self):
        if self.nom in Readfile('attaque')['Nom']:
            return True
        else:
            return False

    # =============================================================================

    # Vérification si l'attaque est reussie ou pas
    def isAttackOk(self):
        rand = np.random.randint(0, 101)
        if rand > self.precision:
            return False
        else:
            return True

    # =============================================================================

    # Calcule de degats si l'attaque est reussie
    # Si elle a echoué on affiche l'echec
    def calculDegat(self, pokemon):
        #soustraction de l'energie
        pokemon.energie -= self.cout
        matrix = [[1, 1, 0.5, 1.5],
                  [1.5, 1, 1, 0.5],
                  [0.5, 1.5, 1, 1],
                  [1, 0.5, 1.5, 1]]
        tab = ['Air', 'Eau', 'Feu', 'Terre']
        if not (self.isAttackOk()):
            print(f"{pokemon.nom} a échoué dans son attaque ({self.nom})\n")
            return 0  # Pas de degats
        else:
            for i in tab:
                if i == pokemon.element:
                    n = tab.index(i)
            for j in tab:
                if j == self.element:
                    m = tab.index(j)

            # determination du coefficion Multiplicateur b qui intervient dans le calcul des degats

            b = matrix[n][m]
            degat = b * np.random.uniform(0.85, 1) * (
                        (self.puissance) * ((4 * pokemon.niveau + 2) / pokemon.resistance) + 2)
            print(f'attaque reussie ({self.nom}) : {degat} \n')
            return degat

    # =============================================================================

"""
if __name__ == "__main__":
    CC = Attaque("Eclair")
    print(CC)
"""