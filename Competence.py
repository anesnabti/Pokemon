# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 20:24:12 2021

@author: Youcef CHORFI
"""

"""
Classe abstraite 
"""

from abc import ABC, abstractmethod

class Competence(ABC) : 

    # =============================================================================

    # Code inchange pour ces methodes
    def __str__(self): 
        return ""

        # =============================================================================

    # Declaration d’une methode abstraite
    # elle nous permet de savoir si la compétence est de type Attaque ou Defense
    @abstractmethod
    def type(self): pass
    
