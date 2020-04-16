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
                test2(case2,r)
                print(a,b,"ah")
                if test2(case2,r)==1:
                    print ("on sait jamais")
                    g=r
                    caseg=1
                case2[a][b]="OOOO"



    if caseg==1:
        cord_piece[i]=cord_case[g]
        case[g//4][g%4]=piecev[i]
        p[i]=0
        c[g]=1

        print("et ouais mon coco tu t'es fait battre par un programme fait par une terminale")
        return
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
    print("selection")

    for z in range (16):
        while p[e]!=2:
            e=random.randint(0,15)
        for r in range (16):

            a=r//4
            b=r%4
            if case2[a][b]== "OOOO":
                #Mode de jeu gagnant
                case2[a][b]=piecev[e]
                print(a,b,"ah")
                print ("on sait jamais")
                if test2(case2,r)==0:
                    cord_piece[e]=cselection
                case2[a][b]="OOOO"

            #mettre ici les coordonnées de la case ou poser les piéces sélectionnées











