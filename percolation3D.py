#========================================================
#
#       Simulation de percolation electrique (3D)
#
#========================================================

#====================================
# Import

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import numpy as np
import random as r

import skimage.measure

#====================================
# Variables

#Taille du cube
N1, N2, N3 = (5,5,5)

# 2 - Etude statistique sur le nombre d'itération suivant :
nIteration = 10

surface = np.zeros([N2,N1,N3], dtype=bool)

#Création d'une liste contenant les positions des cases vides (toutes au début)  
emptyCells = []
for i in range(N2):
    for j in range(N1):
        for k in range(N3):
            emptyCells.append((i,j,k))

#====================================
# Functions

### Fill

#Fonction de reset de la matrice et de la liste des cases vides (1)(2)
def reset(surface, emptyCells):

    for i in range(N2):
        for j in range(N1):
            for k in range(N3):
                surface[i][j][k] = 0

    emptyCells = []
    for i in range(N2):
        for j in range(N1):
            for k in range(N3):
                emptyCells.append((i,j,k))
    
    return surface, emptyCells

#Fonction pour remplir une case (1)(2)
def fillOneCell(surface, emptyCells):
    randomIndex = r.randint(0,len(emptyCells)-1)
    (y,x,z) = emptyCells[randomIndex]
    emptyCells.pop(randomIndex)
    surface[y][x][z] = True

#Fonction de véirification de la percolation (1)(2)
def percolationVerif(result):
    left = []
    for k in range(N1):
        for z in range(N3):
            if (result[k][0][z] != 0):
                left.append(result[k][0][z])
    for k in range(N1):
        for z in range(N3):
            if (result[k][len(result[0])-1][z] in left):
                return True,result[k][len(result[0])-1][z]
    return False, -1


### Show
def explode(data):
    size = np.array(data.shape)*2
    data_e = np.zeros(size - 1, dtype=data.dtype)
    data_e[::2, ::2, ::2] = data
    return data_e

#Afficher la matrice dans une fenêtre (1)(2)
def pltShow(surface, value):
    #plt.figure(figsize=(15,7))
    #plt.matshow(surface, fignum=1, vmin=0, vmax=np.amax(surface))
    #plt.show()

    #z,y,x = surface.nonzero()

    filled = np.ones(surface.shape)
    filled_2 = explode(filled)
    colors = np.where(surface, '#55555555', '#00000000')
    colo = explode(colors)

    x, y, z = np.indices(np.array(filled_2.shape) + 1).astype(float)
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.voxels(x, y, z, filled_2, facecolors=colo, edgecolors='k', linewidth=0)

    result = np.copy(surface)
    result[result!=value] = 0

    filled = np.ones(result.shape)
    filled_2 = explode(filled)
    colors = np.where(result, '#55000055', '#00000000')
    colo = explode(colors)

    x, y, z = np.indices(np.array(filled_2.shape) + 1).astype(float)
    ax = fig.gca(projection='3d')
    ax.voxels(x, y, z, filled_2, facecolors=colo, edgecolors='k', linewidth=0)

    plt.show()

def pltShowM(surfaces):
    x = 1
    for surface in surfaces:
        plt.figure(x, figsize=(15,7))
        plt.matshow(surface, fignum=x, vmin=np.amin(surface), vmax=np.amax(surface))
        x+=1
    plt.show()

#Affiche la matrice dans la console (1)(2)
def npShow(surface):
    print(surface)
    print()

#====================================
# Main

def seq5(surface, emptyCells):
    print("Lancement de l'étude statistique")
    surface, emptyCells = reset(surface, emptyCells)
    
    meanRate = []
    for k in range(nIteration):
        
        if (k%(nIteration/10)==0):
            print(str(k/nIteration*100)+"% complété")
            
        result = None
        isP, value = None, None
        while (not isP):
            if ((N1*N2*N3-len(emptyCells))%((N1*N2*N3)/10)==0):
                print(str((N1*N2*N3-len(emptyCells))/((N1*N2*N3))*100)+"% du remplissage complété")
            fillOneCell(surface, emptyCells)
            result = skimage.measure.label(surface, neighbors=4)
            isP, value = percolationVerif(result)
        meanRate.append((N1*N2*N3-len(emptyCells))/(N1*N2*N3)*100)
        #print("La percolation ce fait à un taux de "+str((N1*N2-len(emptyCells))/(N1*N2)*100)+"%")
        pltShow(result, value)
        surface, emptyCells = reset(surface, emptyCells)
    print("\nLa percolation se fait en moyenne à un taux de "+str(np.mean(meanRate))+"%")


#====================================
# Entry Point

#Foncion principale
def main():
    seq5(surface, emptyCells)
#Point d'entrée du programme, il lance la fonction "main"
if __name__ == "__main__":
    main()
