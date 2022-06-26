# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 11:47:39 2021

@author: walid SAKR
         Youcef CHORFI  ** Update
"""

#from Deck import Deck



class Dresseur:

    # =============================================================================

    def __init__(self, nom, deck):
        self.nom = nom  # nom du joueur
        self.deck = deck  # tableau de pokemons      

    # =============================================================================

    @property
    def nom(self):
        return self.__nom

    # =============================================================================

    @nom.setter
    def nom(self, nom):
        self.__nom = nom

    # =============================================================================

"""
if __name__ == "__main__":
    P = [Pokemon('Pikachu'), Pokemon('Raichu'), Pokemon('Roucool'), Pokemon('Ptitard')]
    D = Deck([Pokemon('Pikachu'), Pokemon('Raichu'), Pokemon('Roucool')], P)
    W = Dresseur("walid", D)
    print(P[0])
    # D.afficheDeck()
    # W.deck.afficheDeck()
"""