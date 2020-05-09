### Recreated Scikit-image label function

import numpy as np

#Fonction pour explorer les cases pleines en partant de la droite
def explore(surface):
    x = 20
    surfaceExplored = np.zeros([len(surface),len(surface[0])], dtype=int)

    for k in range(len(surface)):
        toExplore = []
        if (surface[k][0] == 1 and surfaceExplored[k][0]==0):
            toExplore.append((k,0))   
            surfaceExplored[k][0] = x

        explored = []
        while len(toExplore) != 0:
            explored = getNext(surface, surfaceExplored, toExplore)
            saveExplo(surfaceExplored, explored, x)
            toExplore = list(explored)
            explored = []

        x+=1
    return surfaceExplored

#Fonction d'ajout des cases à visiter à la prochaine itération
def getNext(surface, surfaceExplored, toExplore):
    explored = []
    for v in toExplore:
        y = v[0]
        x = v[1]
        if x+1<len(surface[0]) and surface[y][x+1]==True and surfaceExplored[y][x+1]==0 and not ((y,x+1) in explored):
            explored.append((y,x+1))
        if x-1>=0 and surface[y][x-1]==True and surfaceExplored[y][x-1]==0 and not ((y,x-1) in explored):
            explored.append((y,x-1))
        if y+1<len(surface) and surface[y+1][x]==True and surfaceExplored[y+1][x]==0 and not ((y+1,x) in explored):
            explored.append((y+1,x))
        if y-1>=0 and surface[y-1][x]==True and surfaceExplored[y-1][x]==0 and not ((y-1,x) in explored):
            explored.append((y-1,x))
    return explored

#Fonction de remplissage de la seconde matrice (avec les différents passages)
def saveExplo(surfaceExplored, explored, x):
    #print(len(explored))
    #pltShow(surfaceExplored)
    for v in explored:
        surfaceExplored[v[0]][v[1]] = x
