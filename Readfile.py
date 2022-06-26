# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 20:25:15 2021

@author: Youcef CHORFI
"""

"""
Une fonction qui lit un fichier text en la donnant son nom 
et elle retourne le fichier sous forme d'un dictionnaire
"""


def Readfile(fileName):
    File = open(fr"data\{fileName}.txt", "r")
    file = [i.split('\t') for i in [j.replace('\n', '') for j in File.readlines()]]
    keys = file[0]  # extraire la 1ere ligne, les keys de notre dictionnaire
    del file[0]  # suppression de la 1ere ligne après l'avoir sauvgardé dans keys
    values = list(map(list, zip(*file)))  # Values de notre dictionnaire
    dict_from_list = dict(zip(keys, values))  # conversion vers un dictionnaire
    File.close()
    return dict_from_list


if __name__ == "__main__":
    CC = Readfile("pokemon")
    print(CC)
