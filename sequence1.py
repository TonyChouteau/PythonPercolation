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

N1, N2 = (200,100)
rate = 1/3

surface = np.zeros([N2,N1], dtype=bool)

emptyCells = []
for i in range(N2):
    for j in range(N1):
         emptyCells.append((i,j))

#====================================
# Functions


# Fill

def reset(surface, emptyCells):

    for i in range(N2):
        for j in range(N1):
            surface[i][j] = 0

    emptyCells = []
    for i in range(N2):
        for j in range(N1):
            emptyCells.append((i,j))

#

def fillWithRate(surface, emptyCells, N1, N2, rate):
    
    tN = int(N1*N2*rate)
    print(tN)
    #newEmptyCells = list(emptyCells)

    for _ in range(tN):
        randomIndex = r.randint(0,len(emptyCells)-1)
        (y,x) = emptyCells[randomIndex]
        emptyCells.pop(randomIndex)
        surface[y][x] = True
        #pltShow(surface)
        #print(surface)
        #print(emptyCells)

# Show

def pltShow(surface):
    plt.figure(figsize=(15,7))
    plt.matshow(surface, fignum=1, vmin=0, vmax=1)
    plt.show()

#

def npShow(surface):
    print(surface)
    print()


#====================================
# Entry Point

def main():
    print("Lancement")
    print("Affichage matrice vide")
    reset(surface, emptyCells)
    #pltShow(surface)
    print("Remplissage")
    fillWithRate(surface, emptyCells, N1, N2, rate)
    print("Affichage matrice pleine à "+str(rate*100)+"%")
    pltShow(surface)

#

if __name__ == "__main__":
    main()
