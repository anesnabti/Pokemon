# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 13:05:03 2021

@author: Youcef CHORFI
         Walid SAKR
"""

#from Dresseur import Dresseur
from Attaque import Attaque
from Defense import Defense
#from Pokemon import Pokemon
#from Deck import Deck
import time


class JCJ:

    # =============================================================================
    def __init__(self, d1, d2):
        # d1 et d2 sont des dresseurs
        self.__d1 = d1
        self.__d2 = d2

    def __str__(self):
        return f"Combat entre {self.__d1.nom} et {self.__d2.nom}"

    # =============================================================================

    # =============================================================================
    def combatBegin(self):

        # =============================================================================
        #         Methode principal du déroulement du combat
        # =============================================================================

        print('\n' + "*" * 50, end='\n\n')
        # Affichage du combat entre deck1 et deck2
        print(self, end=('\n\n'))
        print("*" * 50, end='\n\n')
        tour = 1

        # L'etat de chaque joueur (True = loser 'joueur a perdu')
        d1_State = False
        d2_State = False

        # choix du pokemon actif 'fighter' pour les 2 joueurs
        print(f"\nChoisissez votre pokemon {self.__d1.nom}\n ")
        fighter1 = self.__d1.deck.choisirPokemon()
        print("*" * 50, end='\n\n')
        print(f"\nChoisissez votre pokemon {self.__d2.nom}\n ")
        fighter2 = self.__d2.deck.choisirPokemon()
        print()

        time.sleep(1)

        # Reboucler tant que dresseur1 n'a pas perdu et dresseur 2 n'a pas perdu 
        while not d1_State and not d2_State:

            # mise à jour du statut des joueur (s'il y a un perdant)
            d1_State = self.__checkVie(1)
            d2_State = self.__checkVie(2)

            """ TOUR DU JOUEUR 1 """
            
            """
            vérifier si le pokemon actif du 1er dresseur a été mis KO par 
             la dernière attaque du dresseur 2
            """
            if fighter1.vie == 0:
                if d1_State:
                    print("-" * 80, end='\n\n')
                    break
                print(f"C'est à {self.__d1.nom} de jouer\n")
                #demander au dresseur de modifié le pokemon actif
                print(f"\nVeuillez changer votre Pokemon {fighter1.nom} car il a deja été mis KO! \n")
                
                fighter1 = self.__d1.deck.choisirPokemon()

            else:
                #mise en forme de l'affichage
                print("#" * 30, end='\n\n')
                print(f"Tour numéro {tour}\n")
                print("#" * 30, end='\n\n')
                print(f"C'est à {self.__d1.nom} de jouer\n")
                print(f'Voici votre Pokemon : \n\n{fighter1}')
                #choix de l'action à faire par le dresseur1 pour ce tour
                index1 = self.__jcjMenu(fighter1)
                choix1 = self.__choisirOption(index1)
                # choix d'une compétence
                if 0 <= choix1 <= index1:
                    degats1 = self.__choixCompetence(choix1, fighter1)
                    """
                    si elle est de type attaque et qu'elle est réussie 
                    on met à jour la vie du pokemon actif du dresseur2 
                    """
                    fighter2.updateVie(degats1)
                #changer de pokemon
                elif choix1 == index1 + 1:
                    fighter1 = self.__d1.deck.choisirPokemon()
                #passer son tour
                elif choix1 == index1 + 2:
                    pass
                # Fuir le combat
                elif choix1 == index1 + 3:
                    d1_State = True
                    break

            #regeneration d'energie à chaque tour
            fighter1.regenerationEnergie()
            
            #verification de la vie des deux combatants
            d1_State = self.__checkVie(1)
            d2_State = self.__checkVie(2)

            time.sleep(1)

            """ TOUR DU JOUEUR2 2 """
            print("-" * 80, end='\n\n')
            
            """
            vérifier si le pokemon actif du 1er dresseur a été mis KO par 
             la dernière attaque du dresseur 2
            """
            if fighter2.vie == 0:
                if d2_State:
                    break
                #demander à l'utilisateur de changer de pokemon 
                print(f"C'est à {self.__d2.nom} de jouer\n")
                print(f"\nVeuillez changer votre Pokemon {fighter2.nom}, car il a déjà été mis KO! \n")
                fighter2 = self.__d2.deck.choisirPokemon()

            else:
                print(f"C'est à {self.__d2.nom} de jouer\n")
                print(f'Voici votre Pokemon : \n\n{fighter2}')
                #choix de l'action à faire pour ce tour
                index2 = self.__jcjMenu(fighter2)
                choix2 = self.__choisirOption(index2)
                # choix d'une compétence
                if 0 <= choix2 <= index2:
                    degats2 = self.__choixCompetence(choix2, fighter2)
                    """
                    si elle est de type attaque et qu'elle est réussie 
                    on met à jour la vie du pokemon actif du dresseur1 
                    """
                    fighter1.updateVie(degats2)
                #changer de pokemon
                elif choix2 == index2 + 1:
                    fighter2 = self.__d2.deck.choisirPokemon()
                #passer son tour
                elif choix2 == index2 + 2:
                    pass
                #Fuir le combat
                elif choix2 == index2 + 3:
                    d2_State = True
                    break
            #regeneration d'energie à chaque tour
            fighter2.regenerationEnergie()
            
            #passer au tour suivant 
            tour += 1
            time.sleep(1)
        #si c'est le dresseur2 qui a gagné
        if d1_State and not d2_State:
            print(f"Bravo! {self.__d2.nom} a gagné ")
        elif d2_State and not d1_State:
        #si c'est le dresseur1 qui a gagné
            print(f"Bravo! {self.__d1.nom} a gagné ")

        # update de l'experience et du niveau des pokemons du gagnant
        self.__victory(d1_State, d2_State)

    # =============================================================================
    """
    cette méthode gére l'evolution de l'experience et du niveau des pokemons
    du deck du dresseur gagnant
    """
    def __victory(self, d1_state, d2_state):
        # Si le joueur 2 a gagné
        if d1_state and not d2_state:
            Niveau_moyen = 0
            #calcul du niveau moyen des pokemons du deck 1
            for d in self.__d1.deck.deck:
                Niveau_moyen += d.niveau
            Niveau_moyen /= 3
            
            print(f"\nLes pokemons de {self.__d2.nom} ont gagné de l'experiences :\n")
            #update de l'experience et du niveau du deck du dresseur2
            for d in self.__d2.deck.deck:
                d.experienceJCJ(Niveau_moyen)
                d.evolutionNiveau()
                print(f"{d.nom} a gagné : {d.experience}\n")
                #remise à niveau de l'energie et de la vie des deux decks
                self.reset()
        # Si le joueur 2 a gagné
        if d2_state and not d1_state:
            Niveau_moyen = 0
            #calcul du niveau moyen des pokemons du deck 2
            for d in self.__d2.deck.deck:
                Niveau_moyen += d.niveau
            Niveau_moyen /= 3
            print(f"\nLes pokemons de {self.__d1.nom} ont gagné de l'experiences :\n")
            #update de l'experience et du niveau du deck du dresseur1
            for d in self.__d1.deck.deck:
                d.experienceJCJ(Niveau_moyen)
                d.evolutionNiveau()
                print(f"{d.nom} a gagné : {d.experience} \n")
                #remise à niveau de l'energie et de la vie des deux decks
                self.reset()

    # =============================================================================            
    """ 
    checkVie permet de vérifier la vie des pokemons du deck des deux dresseur
    si joueur = 1, on vérifie les pokemons du dresseur1, de meme pour le joueur2
    la méthode return true si l'ensemble des pokemons du deck du joueur sont KO
    """
    
    def __checkVie(self, joueur):
        
        if joueur == 1:
            s = 0
            for d in self.__d1.deck.deck:
                if d.vie == 0:
                    s += 1
            if s == 3:
                return True
            else:
                return False
        if joueur == 2:
            s = 0
            for d in self.__d2.deck.deck:
                if d.vie == 0:
                    s += 1
            if s == 3:
                return True
            else:
                return False

    # =============================================================================    
    """
    méthode qui permet d'utiliser la compétence choisie
    sous conditions que l'energie du pokemon est suffisante
    si c'est une attaque et qu'elle est réussie on retourne les dégats
    sinon on augmente la vie ou l'energie et on retourne 0
    """
    def __choixCompetence(self, a, fighter):

        Competence = fighter.competences[a]
        #verifier que la compétence est utilisable
        if Competence.cout > fighter.energie:
            print(f"Energie n'est pas suffisante! Vous ne pouvez pas utiliser {Competence.nom}\n")
            return 0  # Pas de degats
        #si la compétence choisi est de type attaque 
        elif isinstance(Competence, Attaque):
            #calcul des dégats 
            Degats = Competence.calculDegat(fighter)
            return Degats  
        #si la compétence choisi est de type defense 
        elif isinstance(Competence, Defense):
            Competence.restaurerVieEnergie(fighter)
            return 0  # Pas de degats mais on restaure l'energie ou bien la vie

    # =============================================================================
    #afficher les compétences utilisables par un pokemon 
    def __afficheCompetence(self, fighter):

        # fighter est le pokemon choisi pour le combat 
        for i, c in enumerate(fighter.competences):
            # on affiche que les compétence qui sont utilisables
            if c.cout <= fighter.energie:
                print(f"{i}/ {c}", end="\n\n")
        return i

    # =============================================================================             
    # affichage des choix possibles par les dresseurs
    def __jcjMenu(self, fighter):
        n = self.__afficheCompetence(fighter)
        print(f'{n + 1}/ Changer de pokemon\n')
        print(f'{n + 2}/ Passer son tour\n')
        print(f'{n + 3}/ Fuir le combat\n')
        return n

    # =============================================================================  
    #saisie du choix par le dresseur
    def __choisirOption(self, index):
        #demander à l'utilisateur de saisir son choix
        a = int(input("Que voulez vous choisir ? \n"))
        #vérifier que la saisie n'est pas érronée 
        while a > index + 4:
            print(f"Veuillez entrer une valeur entre 0 et {index + 3} \n")
            a = int(input("Que voulez vous choisir ? \n"))
        return a

    # =============================================================================   
    """
    cette méthode est nécessaire pour la classe jeu car 
    a la fin d'un combat si un joueur veut reprogrammer un JCJ 
    il doit d'abord regenerer la vie et l'energie des pokemons
    """
    def reset(self):
        for p in self.__d1.deck.deck:
            p.vie = p.vieSauv
            p.energie = p.energieSauv
            
        for p in self.__d2.deck.deck:
            p.vie = p.vieSauv
            p.energie = p.energieSauv
      

    # ============================================================================= 

"""
if __name__ == "__main__":
    P1 = [Pokemon('Pikachu'), Pokemon('Raichu'), Pokemon('Roucool'), Pokemon('Ptitard')]
    D2 = Deck([Pokemon('Pikachu'), Pokemon('Raichu'), Pokemon('Roucool')], P1)
    P2 = [Pokemon('Pikachu'), Pokemon('Salameche'), Pokemon('Roucool'), Pokemon('Ptitard')]
    D1 = Deck([Pokemon('Carapuce'), Pokemon('Raichu'), Pokemon('Ptitard')], P2)
    Dresseur1 = Dresseur("Youcef", D1)
    Dresseur2 = Dresseur("Walid", D2)
    Combat = JCJ(Dresseur1, Dresseur2)
    Combat.combatBegin()
"""