#========================================================
#
#       Simulation de percolation electrique
#
#========================================================

#====================================
# Import

#import matplotlib as mp
import matplotlib.animation as animation
import matplotlib.pyplot as plt

import numpy as np
import random as r

#====================================
# Définition des variables

#Taille de matrice
N1, N2 = (200,100)
#Taux de remplissage
rate = 1/3

#Création de la matrice via numpy (matrice pleine de 0)
surface = np.zeros([N2,N1], dtype=bool)

#Création d'une liste contenant les positions des cases vides (toutes au début)  
emptyCells = []
for i in range(N2):
    for j in range(N1):
         emptyCells.append((i,j))

#====================================
# Functions

### Fill

#Fonction de reset de la matrice et de la liste des cases vides
def reset(surface, emptyCells):

    for i in range(N2):
        for j in range(N1):
            surface[i][j] = 0

    emptyCells = []
    for i in range(N2):
        for j in range(N1):
            emptyCells.append((i,j))

#Fonction pour remplir la matrice avec {rate}% de cases
def fillWithRate(surface, emptyCells, N1, N2, rate):
    
    tN = int(N1*N2*rate)
    #newEmptyCells = list(emptyCells)

    for _ in range(tN):
        randomIndex = r.randint(0,len(emptyCells)-1)
        (y,x) = emptyCells[randomIndex]
        emptyCells.pop(randomIndex)
        surface[y][x] = True

### Show

#Afficher la matrice dans une fenêtre
def pltShow(surface):
    plt.figure(figsize=(15,7))
    plt.matshow(surface, fignum=1, vmin=0, vmax=1)
    plt.show()

#Affiche la matrice dans la console
def npShow(surface):
    print(surface)
    print()


#====================================
# Entry Point

#Foncion principale
def main():
    print("Lancement")
    print("Affichage matrice vide")
    reset(surface, emptyCells)
    #pltShow(surface)
    print("Remplissage")
    fillWithRate(surface, emptyCells, N1, N2, rate)
    print("Affichage matrice pleine à "+str(rate*100)+"%")
    pltShow(surface)

#Point d'entrée du programme, il lance la fonction "main"
if __name__ == "__main__":
    main()
