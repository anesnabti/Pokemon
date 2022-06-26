# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 20:30:30 2021

@author: Anes NABTI
         Youcef CHORFI  ** Update
"""
import re
# from Pokemon import Pokemon
from Readfile import Readfile
from Competence import Competence
import numpy as np


class Defense(Competence):
    def __init__(self, nom):

        # =============================================================================

        self.nom = nom
        # Si la compétence est défensive on initialise le reste des attributs
        if self.type():
            self.description = (Readfile("defense")['Description'][Readfile("defense")['Nom'].index(nom)])
            self.element = (Readfile("defense")['Element'][Readfile("defense")['Nom'].index(nom)])
            self.cout = float((Readfile("defense")['Cout'][Readfile("defense")['Nom'].index(nom)]))
            self.soin = [int(i) for i in
                         re.findall(r'\b\d+\b', (Readfile("defense")['Soin'][Readfile("defense")['Nom'].index(nom)]))]
            self.energie = [int(i) for i in re.findall(r'\b\d+\b', (
                Readfile("defense")['Energie'][Readfile("defense")['Nom'].index(nom)]))]

            # =============================================================================
    #méthode qui vérifie si la compétence est de type defense
    def type(self):
        if self.nom in Readfile('defense')['Nom']:
            return True
        else:
            return False
    # =============================================================================
    
    def __str__(self):
        return f"Competence defensive '{self.nom}' : {self.description} Element : {self.element}, Soin : {self.soin}, " \
               f"Energie : {self.energie}, Cout : {self.cout} "

    # =============================================================================
    
    def restaurerVieEnergie(self, pokemon):
        pokemon.energie -= self.cout
        # si le pokemon posséde des compétence de soin et d'energie
        if self.energie != [] and self.soin != []:
            pokemon.energie += np.random.uniform(self.energie[0], self.energie[1])
            pokemon.vie += np.random.uniform(self.soin[0], self.soin[1])
        # si le pokemon posséde que des compétences de regéneration de l'energie
        elif self.energie:
            pokemon.energie += np.random.uniform(self.energie[0], self.energie[1])
        # si le pokemon posséde que des compétences de soin
        elif self.soin:
            pokemon.vie += np.random.uniform(self.soin[0], self.soin[1])
        # remise à niveau de l'energie et de la vie max 
        if pokemon.energie > pokemon.energieMax[1]:
            pokemon.energie = pokemon.energieMax[1]
        elif pokemon.vie > pokemon.vieMax[1]:
            pokemon.vie = pokemon.vieMax[1]

    # =============================================================================

"""
if __name__ == "__main__":
    CC = Defense("Atterrissage")
    print(CC)
    # print(CC.restaurer_vie_energie())
"""