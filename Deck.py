# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 12:44:41 2021

@author: walid
"""

from Pokemon import Pokemon


class Deck:

    # =============================================================================

    def __init__(self, deck, pokemon):
        self.deck = deck
        self.pokemon = pokemon

    # =============================================================================

    def afficheDeck(self):
        print("\nVoici votre deck:")
        for i, p in enumerate(self.deck):
            print(f"\n{i}/ {p}\n")
  
    # =============================================================================            
    #méthode qui permet l'affichage de l'ensemble des pokemons détenus par le joueur
    def affichePokemon(self):
        n = 0
        print("\nVoici vos pokemons:")
        #Les pokemon hors deck
        for i, p in enumerate(self.pokemon) :
            n = n+1
            print(f"\n{i}/ {p}\n")
        #Les pokemons du deck
        for i , p in enumerate(self.deck,n) :
            print(f"\n{i}/ {p}\n")

    # =============================================================================
    #méthode pour modifier le deck d'un joueur
    def changerDeck(self):

        # affichage du deck
        self.afficheDeck()
        # le pokémon a remplacer
        a = int(input("\nQuel pokémon voulez-vous changer ? \n"))
        #tant que la saisie est fausse on reboucle la demande
        while a >= len(self.deck):
            print("\nveuillez rentrer un chiffre correct\n")
            print()
            a = int(input("\nQuel pokémon voulez-vous changer ?\n"))
        # affichage des pokémons qui ne sont pas dans le deck     
        print("\nVoici vos pokémons :\n")
        for i, p in enumerate(self.pokemon):
            print(f"{i}/ {p}\n")
            # le pokemon a ajouter
        b = int(input("\nQuel pokémon voulez-vous ajouter ? \n"))
        while b >= len(self.pokemon):
            print("\nveuillez rentrer un chiffre correct\n")
            b = int(input("\nQuel pokémon voulez-vous ajouter ? \n"))
        # ajout du pokémon
        self.deck[a] = self.pokemon[b]
        #afficher le nouveau deck 
        self.afficheDeck()

    # =============================================================================
    #méthode qui permet de choisir le pokemon actif pour le combat
    def choisirPokemon(self):
        #afficher le deck 
        self.afficheDeck()
        #demander à l'utilisateur de choisir un pokemon 
        a = int(input("\nQuel pokémon voulez-vous utiliser ? \n"))
        while a >= len(self.deck):
            print("\nVeuillez rentrer un chiffre correct\n")
            a = int(input("\nQuel pokémon voulez-vous utiliser ? \n"))
        #s'assurer que le pokemon choisi n'est pas KO
        while self.deck[a].vie <= 0:
            print(f"\n{self.deck[a].nom} a été mis KO! Veuiller en choisir un autre\n")
            a = int(input("\nQuel pokémon voulez-vous utiliser ? \n"))
            #si le joueur a saisie un chiffre incorrecte  
            while a >= len(self.deck):
                print("\nVeuillez rentrer un chiffre correct\n")
                a = int(input("\nQuel pokémon voulez-vous utiliser ? \n"))
        return self.deck[a]

    # =============================================================================

    @property
    def deck(self):
        return self.__deck

    # =============================================================================

    @deck.setter
    def deck(self, deck):
        Setter = True
        for i in deck:
            if not isinstance(i, Pokemon):
                Setter = False
        if Setter:
            self.__deck = deck
        else:
            raise TypeError("Type of object is not Deck")

    # =============================================================================

    @property
    def pokemon(self):
        return self.__pokemon

    # =============================================================================

    @pokemon.setter
    def pokemon(self, pokemon):
        Setter = True
        for i in list(pokemon):
            if not isinstance(i, Pokemon):
                Setter = False
            #laisser que les pokemons hors deck
            if i in self.deck:
                ind = pokemon.index(i)
                del pokemon[ind]
        if Setter:
            self.__pokemon = pokemon
        else:
            raise TypeError("Type of object is not Pokemon")

    # =============================================================================
"""
if __name__ == "__main__":
    P = [Pokemon('Pikachu'), Pokemon('Raichu'), Pokemon('Roucool'), Pokemon('Ptitard')]
    D = Deck([Pokemon('Pikachu'), Pokemon('Raichu'), Pokemon('Roucool')], P)
    # D.afficheDeck()
    #D.changerDeck()
    print(P[0])
    # D.afficheDeck()
    P = D.choisirPokemon()
    # C = D.ChoixCompetence()
    # D.ChoisirPokemon().D.ChoixCompetence().CalculDegat(D.ChoisirPokemon())
"""