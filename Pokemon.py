# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 20:22:18 2021

@author: Youcef CHORFI
         Walid SAKR ** Update
"""

import re  # pour manipuler des chaines de caractères
from Readfile import Readfile  # pour lire le fichier text pokemon
from Attaque import Attaque
from Defense import Defense
from numpy.random import uniform


class Pokemon:
    
    
    
    """    
    les attributs : vie et energie sont la vie et l'energie actuelle du pokemon,
    elles evoluent pendant le combat .
    
    les attributs : vieSauv et energieSauv servent a sauvgardés la vie et l'energie
    maximale du pokemon selon le niveau actuel.
    
    les attributs : niveauMax, vieMax et energieMax nous indiquent le niveau, la vie
    l'energie maximale et minimale du pokemon, l'energie et la vie evoluent selon
    le niveau, et le niveau evolue selon l'expérience acquise.
    
    
                                       (niveau - niveauMin)*(energieMax-energieMin)
    exemple : energie = energieMin +  ----------------------------------------------
                                                  (niveauMax - niveauMin)
                                                                                                         

    """

    # =============================================================================
    def __init__(self, nom, experience=0):
        # Initialisation des attributs à partir du fichier texte après avoir entré le nom du pokemon
        self.nom = nom

        self.avant = (Readfile('pokemon')['Avant'][Readfile('pokemon')['Nom'].index(self.nom)])

        self.apres = (Readfile('pokemon')['Apres'][Readfile('pokemon')['Nom'].index(self.nom)])

        self.element = (Readfile('pokemon')['Element'][Readfile('pokemon')['Nom'].index(self.nom)])

        self.niveauMax = [int(i) for i in re.findall(r'\b\d+\b', (
            Readfile('pokemon')['Niveau'][Readfile('pokemon')['Nom'].index(self.nom)]))]

        self.niveau = [int(i) for i in re.findall(r'\b\d+\b', (
            Readfile('pokemon')['Niveau'][Readfile('pokemon')['Nom'].index(self.nom)]))][0]

        self.vieMax = [int(i) for i in re.findall(r'\b\d+\b', (
            Readfile('pokemon')['Vie'][Readfile('pokemon')['Nom'].index(self.nom)]))]

        self.vie = self.vieMax[0] + (self.niveau - self.niveauMax[0])*(self.vieMax[1]-self.vieMax[0])/(self.niveauMax[1]-self.niveauMax[0])
        
        self.vieSauv = self.vieMax[0] + (self.niveau - self.niveauMax[0])*(self.vieMax[1]-self.vieMax[0])/(self.niveauMax[1]-self.niveauMax[0])
        
        self.energieMax = [int(i) for i in re.findall(r'\b\d+\b', (
            Readfile('pokemon')['Energie'][Readfile('pokemon')['Nom'].index(self.nom)]))]
        
        self.energie = self.energieMax[0] + (self.niveau - self.niveauMax[0])*(self.energieMax[1] - self.energieMax[0])/(self.niveauMax[1] - self.niveauMax[0])
        
        self.energieSauv = self.energieMax[0] + ((self.niveau) - self.niveauMax[0])*(self.energieMax[1] - self.energieMax[0])/(self.niveauMax[1] - self.niveauMax[0])

        self.regeneration = [int(i) for i in re.findall(r'\b\d+\b', (
            Readfile('pokemon')['Regeneration'][Readfile('pokemon')['Nom'].index(self.nom)]))]

        self.resistance = [int(i) for i in re.findall(r'\b\d+\b', (
            Readfile('pokemon')['Resistance'][Readfile('pokemon')['Nom'].index(self.nom)]))][0]

        self.resistanceMax = [int(i) for i in re.findall(r'\b\d+\b', (
            Readfile('pokemon')['Resistance'][Readfile('pokemon')['Nom'].index(self.nom)]))]

        self.competences = self.getCompetence()
        self.experience = experience

    # =============================================================================
    
    def getCompetence(self):
        competences = []
        # le numero de la competence
        indx = Readfile('pokemon')['Nom'].index(self.nom)
        for i in (Readfile('pokemon')['Competences'][indx]).replace('[', '').replace(']', '').split(', '):

            if Attaque(i).type():
                competences.append(Attaque(i))
            elif Defense(i).type():
                competences.append(Defense(i))
        return competences

    # =============================================================================
    
    # re-definition du print pour la class Pokemon
    def __str__(self):
        res = f"{self.nom}(Lvl {self.niveau}, {self.experience}/100, {self.element}): Vie {self.vie}/{self.vieMax[1]},"
        res += f" Energie {self.energie}/{self.energieMax[1]}, Resistance {self.resistance},"
        res += f" {(Readfile('pokemon')['Competences'][Readfile('pokemon')['Nom'].index(self.nom)]).replace('[', '').replace(']', '').split(', ')}\n "
        return res

    # =============================================================================

    #méthode qui permet de faire évaluer le pokemon au niveau supérieur
    def evolutionPokemon(self):
        #verifier que le pokemon peut évoluer 
        if self.apres != "" and self.niveau == self.niveauMax[1] + 1:
            self.nom = self.apres
            self.avant = (Readfile('pokemon')['Avant'][Readfile('pokemon')['Nom'].index(self.nom)])
            self.apres = (Readfile('pokemon')['Apres'][Readfile('pokemon')['Nom'].index(self.nom)])
            self.element = (Readfile('pokemon')['Element'][Readfile('pokemon')['Nom'].index(self.nom)])
            self.niveauMax = [int(i) for i in re.findall(r'\b\d+\b', (
                Readfile('pokemon')['Niveau'][Readfile('pokemon')['Nom'].index(self.nom)]))]
            self.niveau = [int(i) for i in re.findall(r'\b\d+\b', (
                Readfile('pokemon')['Niveau'][Readfile('pokemon')['Nom'].index(self.nom)]))][0]
            self.vieMax = [int(i) for i in re.findall(r'\b\d+\b', (
                Readfile('pokemon')['Vie'][Readfile('pokemon')['Nom'].index(self.nom)]))]
            self.vie = self.vieMax[0] + (self.niveau - self.niveauMax[0])*(self.vieMax[1]-self.vieMax[0])/(self.niveauMax[1]-self.niveauMax[0])
            self.energie = [int(i) for i in re.findall(r'\b\d+\b', (
                Readfile('pokemon')['Energie'][Readfile('pokemon')['Nom'].index(self.nom)]))][0]
            self.energieMax = [int(i) for i in re.findall(r'\b\d+\b', (
                Readfile('pokemon')['Energie'][Readfile('pokemon')['Nom'].index(self.nom)]))]
            self.regeneration = [int(i) for i in re.findall(r'\b\d+\b', (
                Readfile('pokemon')['Regeneration'][Readfile('pokemon')['Nom'].index(self.nom)]))]
            self.resistance = [int(i) for i in re.findall(r'\b\d+\b', (
                Readfile('pokemon')['Resistance'][Readfile('pokemon')['Nom'].index(self.nom)]))][0]
            self.resistanceMax = [int(i) for i in re.findall(r'\b\d+\b', (
                Readfile('pokemon')['Resistance'][Readfile('pokemon')['Nom'].index(self.nom)]))]
            self.competences = self.getCompetence()

    # =============================================================================
    
    #méthode qui permet de gérer l'evolution du niveau des pokemons
    def evolutionNiveau(self):
        #evolution du niveau si experience = 100 et niveau actuel < niveau max
        if self.apres == "" and self.niveau < self.niveauMax[1] and self.experience == 100:
            self.niveau += 1
            self.experience = 0
            self.vie = self.vieMax[0] + (self.niveau - self.niveauMax[0])*(self.vieMax[1]-self.vieMax[0])/(self.niveauMax[1]-self.niveauMax[0])
            self.energie = self.energieMax[0] + (self.niveau - self.niveauMax[0] )*(self.energieMax[1] - self.energieMax[0])/(self.niveauMax[1] - self.niveauMax[0])
            self.resistance += (self.resistanceMax[1] - self.resistanceMax[0]) / (
                    self.niveauMax[1] - self.niveauMax[0])

        #evolution du niveau si experience = 100 et niveau actuel = niveau max
        elif self.apres != "" and self.niveau <= self.niveauMax[1] and self.experience == 100:
            self.niveau += 1
            self.experience = 0
            self.vie = self.vieMax[0] + (self.niveau - self.niveauMax[0])*(self.vieMax[1]-self.vieMax[0])/(self.niveauMax[1]-self.niveauMax[0])
            self.energie = self.energieMax[0] + (self.niveau - self.niveauMax[0] )*(self.energieMax[1] - self.energieMax[0])/(self.niveauMax[1] - self.niveauMax[0])
            self.resistance += (self.resistanceMax[1] - self.resistanceMax[0]) / (
                    self.niveauMax[1] - self.niveauMax[0])
            
        #remise à niveau de l'energie max
        if self.energie > self.energieMax[1]:
            self.energie = self.energieMax[1]
        #evolution du pokemon si niveau max atteint
        self.evolutionPokemon()

    # =============================================================================

    #gain d'experience à la fin d'un combat JCE
    def experienceJCE(self, nivPokemonVaincu):
        self.experience += (10 + nivPokemonVaincu - self.niveau) / 3
        #remise à niveau de l'expeience max
        if self.experience > 100:
            self.experience = 100

    # =============================================================================

    #gain d'experience à la fin d'un combat JCJ
    def experienceJCJ(self, nivPokemonVaincu):
        self.experience += 10 + nivPokemonVaincu - self.niveau
        #remise à niveau de l'expeience max
        if self.experience > 100:
            self.experience = 100

    # =============================================================================
    # mise à jour de la vie pendant un combat 
    def updateVie(self, degats):
        self.vie -= degats
        #remise à niveau de la vie min 
        if self.vie < 0:
            self.vie = 0

    # =============================================================================

    def __eq__(self, other):
        if not isinstance(other, Pokemon):
            return False
        if self is other:
            return True
        if self.nom != other.nom:
            return False
        return True

    # =============================================================================
    #méthode pour régénérer l'energie du pokemon actif à chaque tour
    def regenerationEnergie(self):
        self.energie += uniform(self.regeneration[0], self.regeneration[1])
        #remise à niveau de l'energie max
        if self.energie > self.energieMax[1]:
            self.energie = self.energieMax[1]

    # =============================================================================



if __name__ == "__main__":
    nom = "Pikachu"
    P1 = Pokemon(nom)
    print(P1.energie)
    print(P1.regeneration)
    print(P1.experience)
    P1.regenerationEnergie()
    print(P1.energie)
    P1.experienceJCE(300)
    P1.evolutionNiveau()
    print(P1)
    P1.experienceJCE(300)
    P1.evolutionNiveau()
    print(P1)
    P1.experienceJCE(300)
    P1.evolutionNiveau()
    print(P1)
    P1.experienceJCE(300)
    P1.evolutionNiveau()
    print(P1)
    P1.experienceJCE(300)
    P1.evolutionNiveau()
    print(P1)
    P1.experienceJCE(300)
    P1.evolutionNiveau()
    print(P1)
    print(P1.experience)
    P1.experienceJCE(300)
    P1.evolutionNiveau()
    print(P1)
    P1.experienceJCE(300)
    P1.evolutionNiveau()
    print(P1)
    P1.experienceJCE(300)
    P1.evolutionNiveau()
    print(P1)
    P1.experienceJCE(300)
    P1.evolutionNiveau()
    
    print(P1)

