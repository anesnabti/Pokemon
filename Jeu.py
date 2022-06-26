# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 14:02:47 2022

@author: Walid SAKR
         Youcef CHORFI  **Update
"""

from JCE import JCE
from JCJ import JCJ
from Dresseur import Dresseur
from Pokemon import Pokemon
from Deck import Deck
from Readfile import Readfile
from random import choice



class Jeu:

    def __init__(self):
        pass
    
    # =============================================================================
    
    #Affichage de début du jeu 
    def welcome(self):
        print("\t" * 5 + "#" + "=" * 55 + "#", end='\n')
        print("\t" * 5 + "#" + "\t" * 4 + "Bienvenue dans POOkemon!" + "\t" * 4 + "#")
        print("\t" * 5 + "#" + "\t" * 4 + "Votre Nouveau Jeu Préféré" + "\t" * 4 + "#")
        print("\t" * 5 + "#" + "=" * 55 + "#", end='\n')
        

        
    # =============================================================================
    
    #Affichage de la fin du jeu 
    def goodbye(self):
        print("\t" * 5 + "#" + "=" * 55 + "#", end='\n')
        print("\t" * 5 + "#" + "\t" * 6 + "Au revoir!" + "\t" * 6 + "#")
        print("\t" * 5 + "#  " + "\t" * 5 + "A très bientot !" + "\t" * 5 + "#")
        print("\t" * 5 + "#" + "=" * 55 + "#", end='\n')

    # =============================================================================
    

    #Affichage du menu pour le joueur
    def afficheMenu(self):
        print('\n0/ Voir vos pokemon\n')
        print('1/ Changer le deck\n')
        print('2/ Combattre / Capturer un pokemon\n')
        print('3/ Combattre un autre dresseur\n')
        print('4/ Creer un nouveau dresseur\n')
        print('5/ Quitter\n')
    
    # =============================================================================
    """
    méthode pour céér un dresseur en lui affectant 4 pokemons aléatoirement
    initialement le dresseur posséde des pokemons différents et de niveau 1
    
    """
    def createDresseur(self):
        pokemon = []
        nom = input("Quel est votre nom ? ")

        print(f"\nLe dresseur : {nom} vient d'etre créé \n")
        
        # s'assurer que le dresseur posséde 4 pokemons
        while len(pokemon) != 4:
            P = Pokemon(choice(Readfile("pokemon")['Nom']))
            #affecter des pokemons différents avec niveau = 1
            if P not in pokemon and P.avant == "":
                pokemon.append(P)
                
        #création du deck pour dresseur
        deck = Deck(pokemon[:3], pokemon)
        return Dresseur(nom, deck)
    
    # =============================================================================
    
    # demander au joueur ce qu'il veut faire
    def choix(self):
        a = int(input("Que voulez vous choisir ? \n"))
        #reboucler la demande temps que la saisie est fausse
        while a > 5:
            print("Veuillez entrer une valeur entre 0 et 5 \n")
            a = int(input("Que voulez vous choisir ? \n"))
        return a
    
    # =============================================================================
    
    #executer le choix du joueur 
    def do(self, c, d):
        
        fin = False
        #afficher les pokemons
        if c == 0:
            d.deck.affichePokemon()
        #changer le deck
        if c == 1:
            d.deck.changerDeck()
        # combat contre environnement 
        if c == 2:
            Combat = JCE(d)
            Combat.combatBegin()
        # multijoueur
        if c == 3:
            d2 = self.createDresseur()
            Combat = JCJ(d, d2)
            Combat.combatBegin()
        # créer un nouveau dresseur
        if c == 4:
            d2 = self.createDresseur()
        # Quitter le jeux
        if c == 5:
            fin = True
            self.goodbye()

        return fin
            

    # =============================================================================
    
                      #---------- Programme Principal -----------#


if __name__ == "__main__":
    fin = False
    play = Jeu()
    play.welcome()
    d1 = play.createDresseur()
    d1.deck.afficheDeck()
    #le partie ne s'arrete que si le joueur décide de quitter le jeu
    while not fin:
        print( "#" + "=" * 35 + "#", end='\n')
        print("#" + "\t"*4 + "Menu" + "\t"*4 + "#")
        print( "#" + "=" * 35 + "#", end='\n')
        play.afficheMenu()
        c = play.choix()
        fin = play.do(c, d1)
