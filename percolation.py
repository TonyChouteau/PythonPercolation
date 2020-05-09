#========================================================
#
#       Simulation de percolation electrique
#
#========================================================

#====================================
# Import

#import matplotlib as mp
#import matplotlib.animation as animation
import matplotlib.pyplot as plt
#from matplotlib import animation
#from matplotlib.colors import ListedColormap

import numpy as np
import random as r

#Self created lib like Label
#import label as l
# - instead of -
import skimage.measure

#====================================
# Variables

#Taille de matrice
N1, N2 = (100,100)

#Function use :
USE = 3
# 1 - Rempli simplement la matrice et fait un étude de percolation avec le taux suivant :
rate = 2/5
# 2 - Etude statistique sur le nombre d'itération suivant :
nIteration = 20

#Création de la matrice via numpy (matrice pleine de 0)
surface = np.zeros([N2,N1], dtype=bool)

#Création d'une liste contenant les positions des cases vides (toutes au début)  
emptyCells = []
for i in range(len(surface)):
    for j in range(len(surface[0])):
         emptyCells.append((i,j))

#====================================
# Functions

### Fill

#Fonction de reset de la matrice et de la liste des cases vides (1)(2)
def reset(surface, emptyCells):

    for i in range(len(surface)):
        for j in range(len(surface[0])):
            surface[i][j] = 0

    emptyCells = []
    for i in range(len(surface)):
        for j in range(len(surface[0])):
            emptyCells.append((i,j))
    
    return surface, emptyCells

#Fonction pour remplir une case (1)(2)
def fillOneCell(surface, emptyCells):
    randomIndex = r.randint(0,len(emptyCells)-1)
    (y,x) = emptyCells[randomIndex]
    emptyCells.pop(randomIndex)
    surface[y][x] = True

#Fonction de véirification de la percolation (1)(2)
def percolationVerif(result):
    left = []
    for k in range(len(result)):
        if (result[k][0] != 0):
            left.append(result[k][0])
    for k in range(len(result)):
        if (result[k][len(result[0])-1] in left):
            return True,result[k][len(result[0])-1]
    return False, -1

#Fonction pour remplir la matrice avec {rate}% de cases (1)
def fillWithRate(surface, emptyCells, N1, N2, rate):
    
    tN = int(len(surface[0])*len(surface)*rate)
    #newEmptyCells = list(emptyCells)

    for k in range(tN):
        if (k%(tN/10)==0):
            print(str(k/tN*100)+"% complété")
        fillOneCell(surface, emptyCells)

### Show

#Afficher la matrice dans une fenêtre (1)(2)
def pltShow(surface):
    plt.figure(figsize=(15,7))
    plt.matshow(surface, fignum=1, vmin=0, vmax=np.amax(surface))
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
# Parts

def seq1(surface, emptyCells):
    print("Lancement de l'étude d'une percolation à "+str(rate*100)+"%")
    #print("Affichage matrice vide")
    surface, emptyCells = reset(surface, emptyCells)
    #npShow(surface, emptyCells)
    print("Remplissage")
    fillWithRate(surface, emptyCells, len(surface[0]), len(surface), rate)
    print("Affichage matrice pleine à "+str(rate*100)+"%")
    result = skimage.measure.label(surface, connectivity=1)
    pltShowM([surface,result])
    isP, value = percolationVerif(result)
    
    if isP:
        print("La percolation ce fait via ce chemin :")
        result[result!=value] = 0
        pltShow(result)
    else:
        print("Il n'y a pas percolation")
    #pltShowM([surface,l.explore(surface)])

##

# reset(surface, emptyCells)

# fig = plt.figure()
# im = plt.imshow(surface, vmin=0, vmax=1)

# def init():
#     reseqdt(surface, emptyCells)

# def animate(i):
#     im.setData(surface)

def seq2(surface, emptyCells):
    #print("Lancement de l'étude statistique")
    surface, emptyCells = reset(surface, emptyCells)
    
    meanRate = []
    for k in range(nIteration):
        
        #if (k%(nIteration/10)==0):
        #    print(str(k/nIteration*100)+"% complété")
            
        result = None
        isP, value = None, None
        while (not isP):
            #if ((len(surface[0])*len(surface)-len(emptyCells))%((len(surface[0])*len(surface))/10)==0):
            #    print(str((len(surface[0])*len(surface)-len(emptyCells))/((len(surface[0])*len(surface)))*100)+"% du remplissage complété")
            fillOneCell(surface, emptyCells)
            result = skimage.measure.label(surface, connectivity=1)
            isP, value = percolationVerif(result)
        meanRate.append((len(surface[0])*len(surface)-len(emptyCells))/(len(surface[0])*len(surface))*100)
        #print("La percolation ce fait à un taux de "+str((len(surface[0])*len(surface)-len(emptyCells))/(len(surface[0])*len(surface))*100)+"%")
        #pltShow(result)
        result[result!=value] = 0
        #pltShow(result)
        surface, emptyCells = reset(surface, emptyCells)
    #print("\nLa percolation se fait en moyenne à un taux de "+str(np.mean(meanRate))+"%")
    return np.mean(meanRate)
    

def seq3():
    plt.figure()
    total = 5
    for j in range(total):
        print(j,"/",total)
        n = [1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100,150,200]
        r = []
        for i in n:
            print(i)
            N1, N2 = i, 20
            #Création de la matrice via numpy (matrice pleine de 0)
            surface = np.zeros([N2,N1], dtype=bool)

            #Création d'une liste contenant les positions des cases vides (toutes au début)  
            emptyCells = []
            for i in range(len(surface)):
                for j in range(len(surface[0])):
                    emptyCells.append((i,j))

            #print(len(surface), len(surface[0]), len(emptyCells))

            r.append(seq2(surface, emptyCells))

        #print(len(n), len(r), r)
        plt.plot(n, r)

    plt.show()

    print(r)


#====================================
# Entry Point

#Foncion principale
def main():
    if USE == 1:
        seq1(surface, emptyCells)
    if USE == 2:
        seq2(surface, emptyCells)
    if USE == 3:
        seq3()

#Point d'entrée du programme, il lance la fonction "main"
if __name__ == "__main__":
    main()
