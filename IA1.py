from copy import deepcopy
from fonctions_test import test2
from math import*
import random

def IA(case,e,piecev,cord_piece,cord_case,g,p,c,cselection):

    g=0
    caseg=0
    i=e

    #etat du jeu
    print (case)
    print (piecev[i])
    case2= deepcopy(case)
    print(case2)
    for r in range (16):
            a=r//4
            b=r%4
            if case2[a][b]== "OOOO":
                #Mode de jeu gagnant
                case2[a][b]=piecev[i]
                test2(case2,r,a,b)
                print("ah")
                case2[a][b]="OOOO"
                print (test2(case2,r,a,b))
                if test2(case2,r,a,b)==1:
                    g=r
                    caseg=1

    if caseg!=0:
        cord_piece[i]=cord_case[g]
        case[g//4][g%4]=piecev[i]
        p[i]=0
        c[g]=1
    #placement aléatoire
    else:
        while caseg!="OOOO":
            print("alea")
            ca=random.randint(0,15)
            caseg=case[ca//4][ca%4]

        case[ca//4][ca%4]=piecev[i]
        cord_piece[i]=cord_case[ca]
        p[i]=0
        c[ca]=1

    #sélection de pièce
    while p[i]==0:
        i=random.randint(0,15)
        #mettre ici les coordonnées de la case ou poser les piéces sélectionnées
    cord_piece[i]=cselection










