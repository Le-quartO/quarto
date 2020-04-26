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
    print("c'est la premiere phase")
    for r in range (16):
            a=r//4
            b=r%4
            if case2[a][b]== "OOOO":
                #Mode de jeu gagnant
                case2[a][b]=piecev[i]

                if test2(case2,r)==1:
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
        case2[ca//4][ca%4]=piecev[i]
        cord_piece[i]=cord_case[ca]
        p[i]=0
        c[ca]=1
        print (case2)

    #sélection de pièce
    print("selection")
    m=2
    sauvetage=0
    le=[i for i in range(14)]
    print(le)
    p2=deepcopy(p)
    print(p2)
    while m==2:
        print("ici")

        while p2[e]!=2:
            if le==[]:
                e=random.randint(0,15)
            else:
                e=random.choice(le)
                le.remove(e)

        if le==[]:
                m=1
                break

        p2[e]=0
        m=1


        print(e,"et",le)
        for r in range (16):
            a=r//4
            b=r%4
            if case2[a][b]== "OOOO":
                #Mode de jeu gagnant
                case2[a][b]=piecev[e]
                if test2(case2,r)==1:
                    print ("on sait jamais")
                    m=2
                    case2[a][b]="OOOO"
                    break
                case2[a][b]="OOOO"

    print(e,"c'est e")



    cord_piece[e]=cselection