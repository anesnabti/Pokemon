# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 11:13:22 2022

@author: Walid SAKR & Youcef CHORFI 
"""

#from Dresseur import Dresseur
from Attaque import Attaque
from Defense import Defense
from Pokemon import Pokemon
#from Deck import Deck
from random import random, choice, randint
import numpy as np
import time
from Readfile import Readfile


class JCE:

    # =============================================================================
    def __init__(self, d):
        # d est un dresseur
        self.__d = d
        # choose a random pokemon
        self.__pokemon = self.__getPokemon()


    # ============================================================================= 
    
    # méthode qui retourne un pokemon aléatoire de niveau 1
    def __getPokemon(self):
        pokemon = []
        while len(pokemon) != 1:
            P = Pokemon(choice(Readfile("pokemon")['Nom']))
            #affecter un pokemon de niveau  1
            if P not in pokemon and P.avant == "":
                pokemon.append(P)
        return pokemon[0]


    # ============================================================================= 

    def __str__(self):
        return f"Combat entre {self.__d.nom} et {self.__pokemon.nom}"

    # =============================================================================
    #méthode qui permet de gerer le combat entre le dresseur et le pokemon
    def combatBegin(self):

        # =============================================================================
        #         Methode principal du déroulement du combat
        # =============================================================================

        print('\n' + "*" * 50, end='\n\n')
        # Affichage du combat entre dresseur et pokemon
        print("*" * 50, end='\n\n')
        tour = 1

        # L'etat de chaque joueur (True = loser 'joueur a perdu')
        d_State = False
        p_State = False
        #L'etat de la capture 
        capture = False

        print(f"\nBienvenue {self.__d.nom}   ")
        # choisir la difficulte du combat
        level = self.__difficulty()
        #choix du pokemon actif 'fighter' pour le joueur
        print(f"\nChoisissez votre pokemon {self.__d.nom}\n ")
        fighter1 = self.__d.deck.choisirPokemon()
        
        print("*" * 50, end='\n\n')
        print(f"\nVous allez combattre le pokemon {self.__pokemon.nom}\n ")
    
        fighter2 = self.__pokemon
        print()
        
        # temporiser l'affichage
        time.sleep(1)

        #Reboucler tant que dresseur n'a pas perdu ou le pokemon n'a pas perdu 
        while not d_State and not p_State:

            # mise à jour du statut des joueur (s'il y a un perdant)
            d_State = self.__checkVie(1)
            p_State = self.__checkVie(2)

            """ TOUR DU Dresseur """
            
            """
            verifier si le pokemon actif du dresseur n'a pas ete mis KO par
            la derniere attaque du pokemon
            """
            if fighter1.vie == 0:
                if d_State:
                    print("-" * 80, end='\n\n')
                    break
                print(f"C'est à {self.__d.nom} de jouer\n")
                #demander au dresseur de changer de pokemon
                print(f"\nVeuillez changer votre Pokemon {fighter1.nom} car il a deja été mis KO! \n")
                fighter1 = self.__d.deck.choisirPokemon()

            else:
                #mise en forme de l'affichage
                print("#" * 30, end='\n\n')
                print(f"Tour numéro {tour}\n")
                print("#" * 30, end='\n\n')
                print(f"C'est à {self.__d.nom} de jouer\n")
                print(f'Voici votre Pokemon : \n\n{fighter1}')
                
                #choix de l'action à faire par le dresseur 1 pour ce tour
                index1 = self.__jceMenu(fighter1)
                choix1 = self.__choisirOption(index1)
                # choix d'une compétence
                if 0 <= choix1 <= index1:
                    degats1 = self.__choixCompetence(choix1, fighter1)
                    """
                    si elle est de type attaque et qu'elle est réussie 
                    on met à jour la vie du pokemon adversaire 
                    """
                    fighter2.updateVie(degats1)
                #changer de pokemon
                elif choix1 == index1 + 1:
                    fighter1 = self.__d.deck.choisirPokemon()
                #passer son tour
                elif choix1 == index1 + 2:
                    pass
                # Fuir le combat
                elif choix1 == index1 + 3:
                    d_State = True
                    break
                #essayer de capturer le pokemon
                elif choix1 == index1 + 4:
                    # verifier que le pokemon est capturable
                    if self.__pokemon.vie <= 0.2 * self.__pokemon.vieSauv:
                        capture = self.__capture_Pokemon()
                        
                        #si le pokemon est capturé
                        if capture:
                            p_State = capture
                            break
                    else:
                        print("Le pokemon n'est pas assez faible pour etre capturé")
            #regeneration d'energie à chaque tour
            fighter1.regenerationEnergie()
            
            #verification de la vie des deux combatants
            d_State = self.__checkVie(1)
            p_State = self.__checkVie(2)
            # temporiser entre les instructions
            time.sleep(2)

            """ TOUR DU POKEMON  """
            print("-" * 80, end='\n\n')
            # verifier si le pokemon a ete mis KO par la derniere attaque
            if fighter2.vie == 0:
                p_State = True
                break

            else:
                print(f"C'est à {self.__pokemon.nom} de jouer\n\n")
                print(f"{self.__pokemon}\n")
                # si la difficulté choisie est facile
                if level == 0:
                    #le choix de la compétence se fait aléatoirement
                    choix2 = randint(0, len(fighter2.competences) - 1)
                    degats2 = self.__choixCompetence(choix2, fighter2)
                    """
                    si elle est de type attaque et qu'elle est réussie 
                    on met à jour la vie du pokemon actif du dresseur 
                    """
                    fighter1.updateVie(degats2)
                # si la difficulté choisie est moyenne ou difficile 
                if level == 1 or level == 2:
                    #le choix de la compétence est choisie par une IA
                    degats2 = self.__IA()
                    """
                    si elle est de type attaque et qu'elle est réussie 
                    on met à jour la vie du pokemon actif du dresseur 
                    """
                    fighter1.updateVie(degats2)

            #regeneration d'energie à chaque tour
            fighter2.regenerationEnergie()
            
            #passer au tour suivant
            tour += 1
            time.sleep(2)
            
        #si le pokemon a gagné
        if d_State and not p_State:
            print(f"Dommage! {self.__d.nom} a perdu contre {self.__pokemon.nom}  ")
            
        # si le pokemon est capturé
        elif p_State and not d_State and capture:
            print(f"\nLe combat est fini après la capture de {self.__pokemon.nom}\n")
            
         #si le pokemon est KO
        elif p_State and not d_State and not capture:
            print(f"Bravo! {self.__d.nom} a gagné ")
            
        #si le combat est à égalité
        elif d_State and p_State :
            print("Combat fini! il n'y a pas de Gagnant\nMatch Forfait!!!!!!")
            
        #update de l'experience et du niveau des pokemons du dresseur
        #(sauf si le pokemon est capturé)
        
        if not capture and not d_State:
            self.__victory(d_State,p_State)
            self.reset()
        if capture:
            self.reset()

    # =============================================================================   
    #methode pour choisir la difficulté du combat
    def __difficulty(self):
        level = int(input(
            "veuillez taper: \n0/ pour le niveau facile \n1/ pour le niveau moyen \n2/ pour le niveau difficile \n"))
        while level not in [0, 1, 2]:
            print('\nLevel error! \n')
            level = int(input(
                "veuillez taper: \n0/ pour le niveau facile \n1/ pour le niveau moyen \n2/ pour le niveau difficile "
                "\n \n"))
            
        #incrémentation du niveau des pokemons
        if level == 1:
            for i in range(6):
                self.__pokemon.experienceJCE(300)
                self.__pokemon.evolutionNiveau()
                
        #incrémentation du niveau des pokemons
        if level == 2:
            for i in range(12):
                self.__pokemon.experienceJCE(300)
                self.__pokemon.evolutionNiveau()
        return level

    # =============================================================================
    
    # methode qui gére l'evolution des pokemons si le dresseur à gagné
    def __victory(self, d_state, p_state):

        # Si le joueur a gagné
        if p_state and not d_state:

            print(f"\nLes pokemons de {self.__d.nom} ont gagnés de l'experiences :\n")
            # pour tous les pokemon
            for d in self.__d.deck.deck:
                d.experienceJCE(self.__pokemon.niveau)
                d.evolutionNiveau()
                print(f"{d.nom} a gangé : {d.experience}\n")
        

    # =============================================================================            
    """ 
    checkVie permet de vérifier la vie des pokemons du deck du dresseur ou du 
    pokemon adversaire
    si joueur = 1, on vérifie les pokemons du dresseur1
    si joueur = 2 on vérifie la vie du pokemon adversaire
    si la méthode return true le pokemon ou le deck du jour sont KO
    """
    def __checkVie(self, joueur):
        # vérification pour le dresseur
        if joueur == 1:
            s = 0
            #verifier la vie des pokemons du deck
            for d in self.__d.deck.deck:
                if d.vie == 0:
                    s += 1
            if s == 3:
                return True
            else:
                return False
        #vérification pour le pokemon
        if joueur == 2:

            if self.__pokemon.vie == 0:
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
        # choix de la compétence du pokemon actif
        Competence = fighter.competences[a]
        #si la compétence n'est pas utilisable
        if Competence.cout > fighter.energie:
            print(f"Energie n'est pas suffisante! Vous ne pouvez pas utiliser {Competence.nom}\n")
            return 0  # Pas de degats
        
        #si la compétence est utilisable
        #et si elle est de type attaque
        elif isinstance(Competence, Attaque):
            # Calcul de degats
            Degats = Competence.calculDegat(fighter)
            return Degats  
        
        #si la compétence est utilisable
        #et si elle est de type defense
        elif isinstance(Competence, Defense):
            Competence.restaurerVieEnergie(fighter)
            return 0  # Pas de degats mais on restaure l'energie ou bien la vie

    # =============================================================================
    #afficher les compétences utilisables par un pokemon 
    def __afficheCompetence(self, fighter):

        # le pokemon choisi pour le combat 
        for i, c in enumerate(fighter.competences):
            # on affiche que les compétences qui sont utilisables
            if c.cout <= fighter.energie:
                print(f"{i}/ {c}", end="\n\n")
        return i

    # =============================================================================             
    # affichage des choix possibles par le dresseur
    def __jceMenu(self, fighter):
        n = self.__afficheCompetence(fighter)
        print(f'{n + 1}/ Changer de pokemon\n')
        print(f'{n + 2}/ Passer son tour\n')
        print(f'{n + 3}/ Fuir le combat\n')
        print(f'{n + 4}/ Capturer le pokemon\n')
        return n

    # =============================================================================  
    #saisie du choix par le dresseur
    def __choisirOption(self, index):
        #demander à l'utilisateur de saisir son choix
        a = int(input("Que voulez vous choisir ? \n"))
        #vérifier que la saisie n'est pas érronée 
        while a > index + 4:
            print(f"Veuillez entre une valeur entre 0 {index + 3} \n")
            a = int(input("Que voulez vous choisir ? \n"))
        return a

    # =============================================================================

    #méthode qui nous permet de capturer le pokemon adversaire
    def __capture_Pokemon(self):
        proba = 4 * (0.2 - (self.__pokemon.vie / self.__pokemon.vieSauv))
        #Le pokemon est capturé
        if proba > random():
            print(f"\nFélicitations le pokemon {self.__pokemon.nom} vous appartient désormais\n")
            #ajout du pokemon pour le dresseur
            self.__d.deck.pokemon.append(self.__pokemon)
            return True
        #si le pokemon n'a pu etre capturé 
        else:
            print("\nLa capture a échoué \n")
            return False

    # =============================================================================
    
    """
    Les méthodes : highest_Attack, highest_Energie, restaur_vie. 
    Seront utilisées par notre IA tel que :
    highest_Attack : choisie l'attaque qui peut infliger le plus de dégats
    highest_Energie : choisie la compétence qui regénére le mieux l'energie
    restaur_vie : choisie la compétence apporte les meilleurs soins
    """
    # ============================================================================= 

    def __highest_Attack(self):
        
        competence_attaque = []
        puissance = []
        # parcourir les compétences
        for c in self.__pokemon.competences:
            # si la compétence est de type attaque et elle est réalisable
            if isinstance(c, Attaque) and self.__pokemon.energie >= c.cout:
                competence_attaque.append(c)
                puissance.append(c.puissance)
                
        
        #si le pokemon posséde une compétence d'attaque
        if puissance:
            # la competence avec la plus grande puissance
            choix = competence_attaque[np.argmax(puissance)]
            degats = choix.calculDegat(self.__pokemon)
            return degats
        
        # si le pokemon ne posséde pas de compétences d'attaques
        # ou si notre energie est insuffisante pour les utiliser
        else:
            #augmenter l'énergie du pokemon
            degats = self.__highest_Energie()
            return degats

        # =============================================================================  

        
    def __highest_Energie(self):
        
        competence_defensive = []
        energie = []
        
        # parcourir les compétences
        for c in self.__pokemon.competences:
            
            # si la compétence est de type defense et elle est réalisable
            if isinstance(c, Defense) and self.__pokemon.energie >= c.cout:
                #on récupére que les compétences qui augmentent l'energie
                if c.energie:
                    competence_defensive.append(c)
                    energie.append(c.energie[1])

        # si le pokemon ne posséde pas de compétences de regéneration d'energie
        # ou si notre energie est insuffisante pour les utiliser
        if not energie:
            # On essaye d'attaquer
            degats = self.__highest_Attack()
            return degats
        
        else:
             # la competence qui augmente le plus l'energie du pokemon
            choix = competence_defensive[np.argmax(energie)]
            print(f"\n{self.__pokemon.nom} a choisit d'utiliser {choix.nom}")
            print(f"\nl'energie de {self.__pokemon.nom} vient d'augmenter de {max(energie)}")
            # ajout de l'energie
            self.__pokemon.energie += max(energie)
            if self.__pokemon.energie > self.__pokemon.energieMax[1]:    
                self.__pokemon.energie = self.__pokemon.energieMax[1]
            return 0

    # =============================================================================
    
    def __restaur_vie(self):
        competence_soin = []
        soin = []
         # parcourir les compétences
        for c in self.__pokemon.competences:
            # si la compétence est de type defense et elle est réalisable
            if isinstance(c, Defense) and self.__pokemon.energie >= c.cout:
                #on récupére que les compétences qui augmentent la vie
                if c.soin:
                    competence_soin.append(c)
                    soin.append(c.soin[1]) 
                    
        # si le pokemon ne posséde pas de compétences de soins
        # ou si notre energie est insuffisante pour les utiliser
        if not soin:
            #augmenter l'energie
            degats = self.__highest_Energie()  
            return degats
        
        else:
             # la competence qui augmente le plus la vie du pokemon
            choix = competence_soin[np.argmax(soin)]
            print(f"\n {self.__pokemon.nom} a choisit d'utiliser {choix.nom}")
            print(f"\nla vie de {self.__pokemon.nom} vient d'augmenter de {max(soin)}")
            #ajout du soin 
            self.__pokemon.vie += max(soin)
            #remise a niveau de la vie max 
            if self.__pokemon.vie > self.__pokemon.vieMax[1]:
                self.__pokemon.vie = self.__pokemon.vieMax[1]
            return 0

    # =============================================================================

    """
    IA va permettre au pokemon de jouer d'une maniére intelligente en vérifions 
    son énergie et sa vie. 
    en comparons ces deux derniers avec un seuil définit par rapport à l'energie 
    ou la vie max le pokemon choisit soit d'attaquer, d'augmenter sa vie ou bien 
    son énergie
    """
    def __IA(self):

        if self.__pokemon.vie >= 0.5 * self.__pokemon.vieSauv and self.__pokemon.energie > 0.3 * self.__pokemon.energieSauv:
            degats = self.__highest_Attack()
            return degats
        if self.__pokemon.energie <= 0.3 * self.__pokemon.energieSauv and self.__pokemon.vie >= 0.5 * self.__pokemon.vieSauv:
            degats = self.__highest_Energie()
            return degats  # pas de degats 

        if self.__pokemon.vie < 0.5 * self.__pokemon.vieSauv:
            degats = self.__restaur_vie()
            return degats  # pas de degats
        return 0

    # =============================================================================   
    """
    cette méthode est nécessaire pour la classe jeu car 
    a la fin d'un combat si un joueur veut reprogrammer un JCE
    il doit d'abord regenerer la vie et l'energie des pokemons
    """
    def reset(self):
        for p in self.__d.deck.deck:
            p.vie = p.vieSauv
            p.energie = p.energieSauv
        self.__pokemon.vie = self.__pokemon.vieSauv
        self.__pokemon.energie = self.__pokemon.energieSauv


   # ============================================================================= 

"""
if __name__ == "__main__":
    P1 = [Pokemon('Pikachu'), Pokemon('Raichu'), Pokemon('Roucool'), Pokemon('Ptitard')]
    D2 = Deck([Pokemon('Pikachu'), Pokemon('Raichu'), Pokemon('Roucool')], P1)
    P2 = [Pokemon('Pikachu'), Pokemon('Salameche'), Pokemon('Roucool'), Pokemon('Ptitard')]
    D1 = Deck([Pokemon('Carapuce'), Pokemon('Raichu'), Pokemon('Ptitard')], P2)
    Dresseur1 = Dresseur("Walid", D1)
    Combat = JCE(Dresseur1)
    Combat.combatBegin()
"""