# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 18:01:30 2022

@author: 33660
"""


from Jeu import Jeu
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