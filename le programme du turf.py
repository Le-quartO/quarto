import sys, pygame
from pygame.locals import *

pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((1302, 739))
piecerect1=pygame.Rect(50,50,100,50)

#Chargement et collage du fond

fond = pygame.image.load("fond.png").convert() # insere une image et la convertie au bon format"perso= pygame.image.load("perso.png").convert_alpha()

#Chargement et collage du personnage
lepouce= pygame.image.load("lepouce.png").convert_alpha()
reset = pygame.image.load("piece/restart.png").convert_alpha()
piece1 = pygame.image.load("piece/1.1.png").convert_alpha()
piece2 = pygame.image.load("piece/2.png").convert_alpha()
piece3 = pygame.image.load("piece/3.png").convert_alpha()
piece4 = pygame.image.load("piece/4.png").convert_alpha()
piece5 = pygame.image.load("piece/5.png").convert_alpha()
piece6 = pygame.image.load("piece/6.png").convert_alpha()
piece7 = pygame.image.load("piece/7.png").convert_alpha()
piece8 = pygame.image.load("piece/8.png").convert_alpha()
piece9 = pygame.image.load("piece/9.png").convert_alpha()
piece10 = pygame.image.load("piece/10.png").convert_alpha()
piece11 = pygame.image.load("piece/11.png").convert_alpha()

#création des chaines de caractères des pièces
#R = rond ou C = carré  ; B = beige ou M = marron  ; G = grande ou P = petite  ; T = avec trou ou S = sans trou.

piece1v="RBPT"
piece2v="RMPT"
piece3v="RMPS"
piece4v="RBPS"
piece5v="RBGT"
piece6v="RMGT"
piece7v="RMGS"
piece8v="RBGS"
piece9v="CBPT"
piece10v="CMPT"
piece11v="CBGS"

p1=2
p2=2
p3=2
p4=2
p5=2
p6=2
p7=2
p8=2
p9=2
p10=2
p11=2

fenetre.blit(fond, (0,0))
resetrect=pygame.Rect(1140,617,150,150)
piecerect1=pygame.Rect(900,150,100,50)
piecerect2=pygame.Rect(900,300,100,50)
piecerect3=pygame.Rect(900,450,100,50)
piecerect4=pygame.Rect(1020,150,100,50)
piecerect5=pygame.Rect(1020,300,100,50)
piecerect6=pygame.Rect(1020,450,100,50)
piecerect7=pygame.Rect(1020,10,100,50)
piecerect8=pygame.Rect(870,10,100,50)
piecerect9=pygame.Rect(759,15,95,99)
piecerect10=pygame.Rect(765,150,95,99)
piecerect11=pygame.Rect(765,275,95,99)

lepoucerect=pygame.Rect(950,575,138,157)



fenetre.blit(reset,resetrect)
fenetre.blit(piece1,piecerect1)
fenetre.blit(piece2,piecerect2)
fenetre.blit(piece3,piecerect3)
fenetre.blit(piece4,piecerect4)
fenetre.blit(piece5,piecerect5)
fenetre.blit(piece6,piecerect6)
fenetre.blit(piece7,piecerect7)
fenetre.blit(piece8,piecerect8)
fenetre.blit(piece9,piecerect9)
fenetre.blit(piece10,piecerect10)
fenetre.blit(piece11,piecerect11)

fenetre.blit(lepouce,lepoucerect)



case0=pygame.Rect(110,20,150,150)
case1=pygame.Rect(270,20,150,150)
case2=pygame.Rect(430,20,150,150)
case3=pygame.Rect(590,20,150,150)
case4=pygame.Rect(110,180,150,150)
case5=pygame.Rect(270,180,150,150)
case6=pygame.Rect(430,180,150,150)
case7=pygame.Rect(590,180,150,150)
case8=pygame.Rect(110,340,150,150)
case9=pygame.Rect(270,340,150,150)
case10=pygame.Rect(430,340,150,150)
case11=pygame.Rect(590,340,150,150)
case12=pygame.Rect(110,500,150,150)
case13=pygame.Rect(270,500,150,150)
case14=pygame.Rect(430,500,150,150)
case15=pygame.Rect(590,500,150,150)


#création liste des cases
case=[["OOOO" for i in range(4) ] for i in range(4) ]

# test creation de la fonction test

def test(case):
    for x in range (0,4):
        for i in range (0,4):


            if case[x][0][i]==case[x][1][i]and case [x][1][i]==case[x][2][i]and case[x][2][i]==case[x][3][i] and  case[x][3][i]!="O" :
                print ("bien joué")



    for y in range (0,4):
        for i in range (0,4):


            if case [0][y][i]==case [1][y][i]and case [1][y][i]==case[2][y][i]and case [2][y][i]==case [3][y][i] and case[3][y][i]!="O" :
                print ("bien joué")


    for i in range (0,4):
        if case[0][0][i]==case [1][1][i]and case [1][1][i]==case [2][2][i]and case [2][2][i]==case [3][3][i] and case[3][3][i]!="O" :
            print ("bien joué")

    for i in range (0,4):
        if case[0][3][i]==case [1][2][i]and case [1][2][i]==case [2][1][i] and case [2][1][i]==case [3][0][i] and case[3][0][i]!="O" :
            print ("bien joué")



#Rafraîchissement de l'écran
pygame.display.flip()

#BOUCLE INFINIE
continuer = 1


try:
#Boucle infinie
    while continuer:
        for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
            if event.type == QUIT:     #Si un de ces événements est de type QUIT
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                #mouvement pièce 1

                if pygame.mouse.get_pressed()[0]:
                    if pygame.mouse.get_pos()[0] >= 860 and pygame.mouse.get_pos()[1] >= 150 and pygame.mouse.get_pos()[0] <= 960 and pygame.mouse.get_pos()[1]<=320 and p1==2:
                        p1=1
                    if pygame.mouse.get_pos()[0] >= 110 and pygame.mouse.get_pos()[1] >= 20 and pygame.mouse.get_pos()[0] <= 260 and pygame.mouse.get_pos()[1]<= 170 and p1==1 :
                        piecerect1=case0
                        p1=0
                        case[0][0]=piece1v

                    if pygame.mouse.get_pos()[0] >= 270 and pygame.mouse.get_pos()[1] >= 20 and pygame.mouse.get_pos()[0] <= 420 and pygame.mouse.get_pos()[1]<= 170 and p1==1 :
                        piecerect1=case1
                        p1=0
                        case[0][1]=piece1v

                    if pygame.mouse.get_pos()[0] >= 430 and pygame.mouse.get_pos()[1] >= 20 and pygame.mouse.get_pos()[0] <= 580 and pygame.mouse.get_pos()[1]<= 170 and p1==1 :
                        piecerect1=case2
                        p1=0
                        case[0][2]=piece1v

                    if pygame.mouse.get_pos()[0] >= 590 and pygame.mouse.get_pos()[1] >= 20 and pygame.mouse.get_pos()[0] <= 740 and pygame.mouse.get_pos()[1]<= 170 and p1==1 :
                        piecerect1=case3
                        p1=0
                        case[0][3]=piece1v

                    if pygame.mouse.get_pos()[0] >= 110 and pygame.mouse.get_pos()[1] >= 180 and pygame.mouse.get_pos()[0] <= 260 and pygame.mouse.get_pos()[1]<= 330 and p1==1 :
                        piecerect1=case4
                        p1=0
                        case[1][0]=piece1v

                    if pygame.mouse.get_pos()[0] >= 270 and pygame.mouse.get_pos()[1] >= 180 and pygame.mouse.get_pos()[0] <= 420 and pygame.mouse.get_pos()[1]<= 330 and p1==1 :
                        piecerect1=case5
                        p1=0
                        case[1][1]=piece1v

                    if pygame.mouse.get_pos()[0] >= 430 and pygame.mouse.get_pos()[1] >= 180 and pygame.mouse.get_pos()[0] <= 580 and pygame.mouse.get_pos()[1]<= 330 and p1==1 :
                        piecerect1=case6
                        p1=0
                        case[1][2]=piece1v

                    if pygame.mouse.get_pos()[0] >= 590 and pygame.mouse.get_pos()[1] >= 180 and pygame.mouse.get_pos()[0] <= 740 and pygame.mouse.get_pos()[1]<= 330 and p1==1 :
                        piecerect1=case7
                        p1=0
                        case[1][3]=piece1v

                    if pygame.mouse.get_pos()[0] >= 110 and pygame.mouse.get_pos()[1] >= 340 and pygame.mouse.get_pos()[0] <= 260 and pygame.mouse.get_pos()[1]<= 490 and p1==1 :
                        piecerect1=case8
                        p1=0
                        case[2][0]=piece1v

                    if pygame.mouse.get_pos()[0] >= 270 and pygame.mouse.get_pos()[1] >= 340 and pygame.mouse.get_pos()[0] <= 420 and pygame.mouse.get_pos()[1]<= 490 and p1==1 :
                        piecerect1=case9
                        p1=0
                        case[2][1]=piece1v

                    if pygame.mouse.get_pos()[0] >= 430 and pygame.mouse.get_pos()[1] >= 340 and pygame.mouse.get_pos()[0] <= 580 and pygame.mouse.get_pos()[1]<= 490 and p1==1 :
                        piecerect1=case10
                        p1=0
                        case[2][2]=piece1v

                    if pygame.mouse.get_pos()[0] >= 590 and pygame.mouse.get_pos()[1] >= 340 and pygame.mouse.get_pos()[0] <= 740 and pygame.mouse.get_pos()[1]<= 490 and p1==1 :
                        piecerect1=case11
                        p1=0
                        case[2][3]=piece1v

                    if pygame.mouse.get_pos()[0] >= 110 and pygame.mouse.get_pos()[1] >= 500 and pygame.mouse.get_pos()[0] <= 260 and pygame.mouse.get_pos()[1]<= 650 and p1==1 :
                        piecerect1=case12
                        p1=0
                        case[3][0]=piece1v

                    if pygame.mouse.get_pos()[0] >= 270 and pygame.mouse.get_pos()[1] >= 500 and pygame.mouse.get_pos()[0] <= 420 and pygame.mouse.get_pos()[1]<= 650 and p1==1 :
                        piecerect1=case13
                        p1=0
                        case[3][1]=piece1v

                    if pygame.mouse.get_pos()[0] >= 430 and pygame.mouse.get_pos()[1] >= 500 and pygame.mouse.get_pos()[0] <= 580 and pygame.mouse.get_pos()[1]<= 650 and p1==1 :
                        piecerect1=case14
                        p1=0
                        case[3][2]=piece1v
                    if pygame.mouse.get_pos()[0] >= 590 and pygame.mouse.get_pos()[1] >= 500 and pygame.mouse.get_pos()[0] <= 740 and pygame.mouse.get_pos()[1]<= 650 and p1==1 :
                        piecerect1=case15
                        p1=0
                        case[3][3]=piece1v




                     #mouvement pièce 2



                    if pygame.mouse.get_pos()[0] >= 900 and pygame.mouse.get_pos()[1] >= 300 and pygame.mouse.get_pos()[0] <= 1020 and pygame.mouse.get_pos()[1]<=420 and p2==2:
                        p2=1
                    if pygame.mouse.get_pos()[0] >= 110 and pygame.mouse.get_pos()[1] >= 20 and pygame.mouse.get_pos()[0] <= 260 and pygame.mouse.get_pos()[1]<= 170 and p2==1 :
                        piecerect2=case0
                        p2=0
                        case[0][0]=piece2v

                    if pygame.mouse.get_pos()[0] >= 270 and pygame.mouse.get_pos()[1] >= 20 and pygame.mouse.get_pos()[0] <= 420 and pygame.mouse.get_pos()[1]<= 170 and p2==1 :
                        piecerect2=case1
                        p2=0
                        case[0][1]=piece2v

                    if pygame.mouse.get_pos()[0] >= 430 and pygame.mouse.get_pos()[1] >= 20 and pygame.mouse.get_pos()[0] <= 580 and pygame.mouse.get_pos()[1]<= 170 and p2==1 :
                        piecerect2=case2
                        p2=0
                        case[0][2]=piece2v

                    if pygame.mouse.get_pos()[0] >= 590 and pygame.mouse.get_pos()[1] >= 20 and pygame.mouse.get_pos()[0] <= 740 and pygame.mouse.get_pos()[1]<= 170 and p2==1 :
                        piecerect2=case3
                        p2=0
                        case[0][3]=piece2v

                    if pygame.mouse.get_pos()[0] >= 110 and pygame.mouse.get_pos()[1] >= 180 and pygame.mouse.get_pos()[0] <= 260 and pygame.mouse.get_pos()[1]<= 330 and p2==1 :
                        piecerect2=case4
                        p2=0
                        case[1][0]=piece2v

                    if pygame.mouse.get_pos()[0] >= 270 and pygame.mouse.get_pos()[1] >= 180 and pygame.mouse.get_pos()[0] <= 420 and pygame.mouse.get_pos()[1]<= 330 and p2==1 :
                        piecerect2=case5
                        p2=0
                        case[1][1]=piece2v

                    if pygame.mouse.get_pos()[0] >= 430 and pygame.mouse.get_pos()[1] >= 180 and pygame.mouse.get_pos()[0] <= 580 and pygame.mouse.get_pos()[1]<= 330 and p2==1 :
                        piecerect2=case6
                        p2=0
                        case[1][2]=piece2v

                    if pygame.mouse.get_pos()[0] >= 590 and pygame.mouse.get_pos()[1] >= 180 and pygame.mouse.get_pos()[0] <= 740 and pygame.mouse.get_pos()[1]<= 330 and p2==1 :
                        piecerect2=case7
                        p2=0
                        case[1][3]=piece2v

                    if pygame.mouse.get_pos()[0] >= 110 and pygame.mouse.get_pos()[1] >= 340 and pygame.mouse.get_pos()[0] <= 260 and pygame.mouse.get_pos()[1]<= 490 and p2==1 :
                        piecerect2=case8
                        p2=0
                        case[2][0]=piece2v

                    if pygame.mouse.get_pos()[0] >= 270 and pygame.mouse.get_pos()[1] >= 340 and pygame.mouse.get_pos()[0] <= 420 and pygame.mouse.get_pos()[1]<= 490 and p2==1 :
                        piecerect2=case9
                        p2=0
                        case[2][1]=piece2v

                    if pygame.mouse.get_pos()[0] >= 430 and pygame.mouse.get_pos()[1] >= 340 and pygame.mouse.get_pos()[0] <= 580 and pygame.mouse.get_pos()[1]<= 490 and p2==1 :
                        piecerect2=case10
                        p2=0
                        case[2][2]=piece2v

                    if pygame.mouse.get_pos()[0] >= 590 and pygame.mouse.get_pos()[1] >= 340 and pygame.mouse.get_pos()[0] <= 740 and pygame.mouse.get_pos()[1]<= 490 and p2==1 :
                        piecerect2=case11
                        p2=0
                        case[2][3]=piece2v

                    if pygame.mouse.get_pos()[0] >= 110 and pygame.mouse.get_pos()[1] >= 500 and pygame.mouse.get_pos()[0] <= 260 and pygame.mouse.get_pos()[1]<= 650 and p2==1 :
                        piecerect2=case12
                        p2=0
                        case[3][0]=piece2v

                    if pygame.mouse.get_pos()[0] >= 270 and pygame.mouse.get_pos()[1] >= 500 and pygame.mouse.get_pos()[0] <= 420 and pygame.mouse.get_pos()[1]<= 650 and p2==1 :
                        piecerect2=case13
                        p2=0
                        case[3][1]=piece2v

                    if pygame.mouse.get_pos()[0] >= 430 and pygame.mouse.get_pos()[1] >= 500 and pygame.mouse.get_pos()[0] <= 580 and pygame.mouse.get_pos()[1]<= 650 and p2==1 :
                        piecerect2=case14
                        p2=0
                        case[3][2]=piece2v

                    if pygame.mouse.get_pos()[0] >= 590 and pygame.mouse.get_pos()[1] >= 500 and pygame.mouse.get_pos()[0] <= 740 and pygame.mouse.get_pos()[1]<= 650 and p2==1 :
                        piecerect2=case15
                        p2=0
                        case[3][3]=piece2v




                     #mouvement pièce 3



                    if pygame.mouse.get_pos()[0] >= 900 and pygame.mouse.get_pos()[1] >= 450 and pygame.mouse.get_pos()[0] <= 1020 and pygame.mouse.get_pos()[1]<=570 and p3==2:
                        p3=1
                    if pygame.mouse.get_pos()[0] >= 110 and pygame.mouse.get_pos()[1] >= 20 and pygame.mouse.get_pos()[0] <= 260 and pygame.mouse.get_pos()[1]<= 170 and p3==1 :
                        piecerect3=case0
                        p3=0
                        case[0][0]=piece3v

                    if pygame.mouse.get_pos()[0] >= 270 and pygame.mouse.get_pos()[1] >= 20 and pygame.mouse.get_pos()[0] <= 420 and pygame.mouse.get_pos()[1]<= 170 and p3==1 :
                        piecerect3=case1
                        p3=0
                        case[0][1]=piece3v

                    if pygame.mouse.get_pos()[0] >= 430 and pygame.mouse.get_pos()[1] >= 20 and pygame.mouse.get_pos()[0] <= 580 and pygame.mouse.get_pos()[1]<= 170 and p3==1 :
                        piecerect3=case2
                        p3=0
                        case[0][2]=piece3v

                    if pygame.mouse.get_pos()[0] >= 590 and pygame.mouse.get_pos()[1] >= 20 and pygame.mouse.get_pos()[0] <= 740 and pygame.mouse.get_pos()[1]<= 170 and p3==1 :
                        piecerect3=case3
                        p3=0
                        case[0][3]=piece3v

                    if pygame.mouse.get_pos()[0] >= 110 and pygame.mouse.get_pos()[1] >= 180 and pygame.mouse.get_pos()[0] <= 260 and pygame.mouse.get_pos()[1]<= 330 and p3==1 :
                        piecerect3=case4
                        p3=0
                        case[1][0]=piece3v

                    if pygame.mouse.get_pos()[0] >= 270 and pygame.mouse.get_pos()[1] >= 180 and pygame.mouse.get_pos()[0] <= 420 and pygame.mouse.get_pos()[1]<= 330 and p3==1 :
                        piecerect3=case5
                        p3=0
                        case[1][1]=piece3v

                    if pygame.mouse.get_pos()[0] >= 430 and pygame.mouse.get_pos()[1] >= 180 and pygame.mouse.get_pos()[0] <= 580 and pygame.mouse.get_pos()[1]<= 330 and p3==1 :
                        piecerect3=case6
                        p3=0
                        case[1][2]=piece3v

                    if pygame.mouse.get_pos()[0] >= 590 and pygame.mouse.get_pos()[1] >= 180 and pygame.mouse.get_pos()[0] <= 740 and pygame.mouse.get_pos()[1]<= 330 and p3==1 :
                        piecerect3=case7
                        p3=0
                        case[1][3]=piece3v

                    if pygame.mouse.get_pos()[0] >= 110 and pygame.mouse.get_pos()[1] >= 340 and pygame.mouse.get_pos()[0] <= 260 and pygame.mouse.get_pos()[1]<= 490 and p3==1 :
                        piecerect3=case8
                        p3=0
                        case[2][0]=piece3v

                    if pygame.mouse.get_pos()[0] >= 270 and pygame.mouse.get_pos()[1] >= 340 and pygame.mouse.get_pos()[0] <= 420 and pygame.mouse.get_pos()[1]<= 490 and p3==1 :
                        piecerect3=case9
                        p3=0
                        case[2][1]=piece3v

                    if pygame.mouse.get_pos()[0] >= 430 and pygame.mouse.get_pos()[1] >= 340 and pygame.mouse.get_pos()[0] <= 580 and pygame.mouse.get_pos()[1]<= 490 and p3==1 :
                        piecerect3=case10
                        p3=0
                        case[2][2]=piece3v

                    if pygame.mouse.get_pos()[0] >= 590 and pygame.mouse.get_pos()[1] >= 340 and pygame.mouse.get_pos()[0] <= 740 and pygame.mouse.get_pos()[1]<= 490 and p3==1 :
                        piecerect3=case11
                        p3=0
                        case[2][3]=piece3v

                    if pygame.mouse.get_pos()[0] >= 110 and pygame.mouse.get_pos()[1] >= 500 and pygame.mouse.get_pos()[0] <= 260 and pygame.mouse.get_pos()[1]<= 650 and p3==1 :
                        piecerect3=case12
                        p3=0
                        case[3][0]=piece3v

                    if pygame.mouse.get_pos()[0] >= 270 and pygame.mouse.get_pos()[1] >= 500 and pygame.mouse.get_pos()[0] <= 420 and pygame.mouse.get_pos()[1]<= 650 and p3==1 :
                        piecerect3=case13
                        p3=0
                        case[3][1]=piece3v

                    if pygame.mouse.get_pos()[0] >= 430 and pygame.mouse.get_pos()[1] >= 500 and pygame.mouse.get_pos()[0] <= 580 and pygame.mouse.get_pos()[1]<= 650 and p3==1 :
                        piecerect3=case14
                        p3=0
                        case[3][2]=piece3v

                    if pygame.mouse.get_pos()[0] >= 590 and pygame.mouse.get_pos()[1] >= 500 and pygame.mouse.get_pos()[0] <= 740 and pygame.mouse.get_pos()[1]<= 650 and p3==1 :
                        piecerect3=case15
                        p3=0
                        case[3][3]=piece3v



                     #mouvement pièce 4




                    if pygame.mouse.get_pos()[0] >= 1020 and pygame.mouse.get_pos()[1] >= 150 and pygame.mouse.get_pos()[0] <= 1140 and pygame.mouse.get_pos()[1]<=270 and p4==2:
                        p4=1
                    if pygame.mouse.get_pos()[0] >= 110 and pygame.mouse.get_pos()[1] >= 20 and pygame.mouse.get_pos()[0] <= 260 and pygame.mouse.get_pos()[1]<= 170 and p4==1 :
                        piecerect4=case0
                        p4=0
                        case[0][0]=piece4v

                    if pygame.mouse.get_pos()[0] >= 270 and pygame.mouse.get_pos()[1] >= 20 and pygame.mouse.get_pos()[0] <= 420 and pygame.mouse.get_pos()[1]<= 170 and p4==1 :
                        piecerect4=case1
                        p4=0
                        case[0][1]=piece4v

                    if pygame.mouse.get_pos()[0] >= 430 and pygame.mouse.get_pos()[1] >= 20 and pygame.mouse.get_pos()[0] <= 580 and pygame.mouse.get_pos()[1]<= 170 and p4==1 :
                        piecerect4=case2
                        p4=0
                        case[0][2]=piece4v

                    if pygame.mouse.get_pos()[0] >= 590 and pygame.mouse.get_pos()[1] >= 20 and pygame.mouse.get_pos()[0] <= 740 and pygame.mouse.get_pos()[1]<= 170 and p4==1 :
                        piecerect4=case3
                        p4=0
                        case[0][3]=piece4v

                    if pygame.mouse.get_pos()[0] >= 110 and pygame.mouse.get_pos()[1] >= 180 and pygame.mouse.get_pos()[0] <= 260 and pygame.mouse.get_pos()[1]<= 330 and p4==1 :
                        piecerect4=case4
                        p4=0
                        case[1][0]=piece4v

                    if pygame.mouse.get_pos()[0] >= 270 and pygame.mouse.get_pos()[1] >= 180 and pygame.mouse.get_pos()[0] <= 420 and pygame.mouse.get_pos()[1]<= 330 and p4==1 :
                        piecerect4=case5
                        p4=0
                        case[1][1]=piece4v

                    if pygame.mouse.get_pos()[0] >= 430 and pygame.mouse.get_pos()[1] >= 180 and pygame.mouse.get_pos()[0] <= 580 and pygame.mouse.get_pos()[1]<= 330 and p4==1 :
                        piecerect4=case6
                        p4=0
                        case[1][2]=piece4v

                    if pygame.mouse.get_pos()[0] >= 590 and pygame.mouse.get_pos()[1] >= 180 and pygame.mouse.get_pos()[0] <= 740 and pygame.mouse.get_pos()[1]<= 330 and p4==1 :
                        piecerect4=case7
                        p4=0
                        case[1][3]=piece4v

                    if pygame.mouse.get_pos()[0] >= 110 and pygame.mouse.get_pos()[1] >= 340 and pygame.mouse.get_pos()[0] <= 260 and pygame.mouse.get_pos()[1]<= 490 and p4==1 :
                        piecerect4=case8
                        p4=0
                        case[2][0]=piece4v

                    if pygame.mouse.get_pos()[0] >= 270 and pygame.mouse.get_pos()[1] >= 340 and pygame.mouse.get_pos()[0] <= 420 and pygame.mouse.get_pos()[1]<= 490 and p4==1 :
                        piecerect4=case9
                        p4=0
                        case[2][1]=piece4v

                    if pygame.mouse.get_pos()[0] >= 430 and pygame.mouse.get_pos()[1] >= 340 and pygame.mouse.get_pos()[0] <= 580 and pygame.mouse.get_pos()[1]<= 490 and p4==1 :
                        piecerect4=case10
                        p4=0
                        case[2][2]=piece4v

                    if pygame.mouse.get_pos()[0] >= 590 and pygame.mouse.get_pos()[1] >= 340 and pygame.mouse.get_pos()[0] <= 740 and pygame.mouse.get_pos()[1]<= 490 and p4==1 :
                        piecerect4=case11
                        p4=0
                        case[2][3]=piece4v

                    if pygame.mouse.get_pos()[0] >= 110 and pygame.mouse.get_pos()[1] >= 500 and pygame.mouse.get_pos()[0] <= 260 and pygame.mouse.get_pos()[1]<= 650 and p4==1 :
                        piecerect4=case12
                        p4=0
                        case[3][0]=piece4v

                    if pygame.mouse.get_pos()[0] >= 270 and pygame.mouse.get_pos()[1] >= 500 and pygame.mouse.get_pos()[0] <= 420 and pygame.mouse.get_pos()[1]<= 650 and p4==1 :
                        piecerect4=case13
                        p4=0
                        case[3][1]=piece4v

                    if pygame.mouse.get_pos()[0] >= 430 and pygame.mouse.get_pos()[1] >= 500 and pygame.mouse.get_pos()[0] <= 580 and pygame.mouse.get_pos()[1]<= 650 and p4==1 :
                        piecerect4=case14
                        p4=0
                        case[3][2]=piece4v

                    if pygame.mouse.get_pos()[0] >= 590 and pygame.mouse.get_pos()[1] >= 500 and pygame.mouse.get_pos()[0] <= 740 and pygame.mouse.get_pos()[1]<= 650 and p4==1 :
                        piecerect4=case15
                        p4=0
                        case[3][3]=piece4v


                    #mouvement pièce 5


                    if pygame.mouse.get_pos()[0] >= 1020 and pygame.mouse.get_pos()[1] >= 300 and pygame.mouse.get_pos()[0] <= 1140 and pygame.mouse.get_pos()[1]<=420 and p5==2:
                        p5=1
                    if pygame.mouse.get_pos()[0] >= 110 and pygame.mouse.get_pos()[1] >= 20 and pygame.mouse.get_pos()[0] <= 260 and pygame.mouse.get_pos()[1]<= 170 and p5==1 :
                        piecerect5=case0
                        p5=0
                        case[0][0]=piece5v

                    if pygame.mouse.get_pos()[0] >= 270 and pygame.mouse.get_pos()[1] >= 20 and pygame.mouse.get_pos()[0] <= 420 and pygame.mouse.get_pos()[1]<= 170 and p5==1 :
                        piecerect5=case1
                        p5=0
                        case[0][1]=piece5v

                    if pygame.mouse.get_pos()[0] >= 430 and pygame.mouse.get_pos()[1] >= 20 and pygame.mouse.get_pos()[0] <= 580 and pygame.mouse.get_pos()[1]<= 170 and p5==1 :
                        piecerect5=case2
                        p5=0
                        case[0][2]=piece5v

                    if pygame.mouse.get_pos()[0] >= 590 and pygame.mouse.get_pos()[1] >= 20 and pygame.mouse.get_pos()[0] <= 740 and pygame.mouse.get_pos()[1]<= 170 and p5==1 :
                        piecerect5=case3
                        p5=0
                        case[0][3]=piece5v

                    if pygame.mouse.get_pos()[0] >= 110 and pygame.mouse.get_pos()[1] >= 180 and pygame.mouse.get_pos()[0] <= 260 and pygame.mouse.get_pos()[1]<= 330 and p5==1 :
                        piecerect5=case4
                        p5=0
                        case[1][0]=piece5v

                    if pygame.mouse.get_pos()[0] >= 270 and pygame.mouse.get_pos()[1] >= 180 and pygame.mouse.get_pos()[0] <= 420 and pygame.mouse.get_pos()[1]<= 330 and p5==1 :
                        piecerect5=case5
                        p5=0
                        case[1][1]=piece5v

                    if pygame.mouse.get_pos()[0] >= 430 and pygame.mouse.get_pos()[1] >= 180 and pygame.mouse.get_pos()[0] <= 580 and pygame.mouse.get_pos()[1]<= 330 and p5==1 :
                        piecerect5=case6
                        p5=0
                        case[1][2]=piece5v

                    if pygame.mouse.get_pos()[0] >= 590 and pygame.mouse.get_pos()[1] >= 180 and pygame.mouse.get_pos()[0] <= 740 and pygame.mouse.get_pos()[1]<= 330 and p5==1 :
                        piecerect5=case7
                        p5=0
                        case[1][3]=piece5v

                    if pygame.mouse.get_pos()[0] >= 110 and pygame.mouse.get_pos()[1] >= 340 and pygame.mouse.get_pos()[0] <= 260 and pygame.mouse.get_pos()[1]<= 490 and p5==1 :
                        piecerect5=case8
                        p5=0
                        case[2][0]=piece5v

                    if pygame.mouse.get_pos()[0] >= 270 and pygame.mouse.get_pos()[1] >= 340 and pygame.mouse.get_pos()[0] <= 420 and pygame.mouse.get_pos()[1]<= 490 and p5==1 :
                        piecerect5=case9
                        p5=0
                        case[2][1]=piece5v

                    if pygame.mouse.get_pos()[0] >= 430 and pygame.mouse.get_pos()[1] >= 340 and pygame.mouse.get_pos()[0] <= 580 and pygame.mouse.get_pos()[1]<= 490 and p5==1 :
                        piecerect5=case10
                        p5=0
                        case[2][2]=piece5v

                    if pygame.mouse.get_pos()[0] >= 590 and pygame.mouse.get_pos()[1] >= 340 and pygame.mouse.get_pos()[0] <= 740 and pygame.mouse.get_pos()[1]<= 490 and p5==1 :
                        piecerect5=case11
                        p5=0
                        case[2][3]=piece5v

                    if pygame.mouse.get_pos()[0] >= 110 and pygame.mouse.get_pos()[1] >= 500 and pygame.mouse.get_pos()[0] <= 260 and pygame.mouse.get_pos()[1]<= 650 and p5==1 :
                        piecerect5=case12
                        p5=0
                        case[3][0]=piece5v

                    if pygame.mouse.get_pos()[0] >= 270 and pygame.mouse.get_pos()[1] >= 500 and pygame.mouse.get_pos()[0] <= 420 and pygame.mouse.get_pos()[1]<= 650 and p5==1 :
                        piecerect5=case13
                        p5=0
                        case[3][1]=piece5v

                    if pygame.mouse.get_pos()[0] >= 430 and pygame.mouse.get_pos()[1] >= 500 and pygame.mouse.get_pos()[0] <= 580 and pygame.mouse.get_pos()[1]<= 650 and p5==1 :
                        piecerect5=case14
                        p5=0
                        case[3][2]=piece5v

                    if pygame.mouse.get_pos()[0] >= 590 and pygame.mouse.get_pos()[1] >= 500 and pygame.mouse.get_pos()[0] <= 740 and pygame.mouse.get_pos()[1]<= 650 and p5==1 :
                        piecerect5=case15
                        p5=0
                        case[3][1]=piece5v


                    #mouvement pièce 6


                    if pygame.mouse.get_pos()[0] >= 1020 and pygame.mouse.get_pos()[1] >= 450 and pygame.mouse.get_pos()[0] <= 1140 and pygame.mouse.get_pos()[1]<=570 and p6==2:
                        p6=1
                    if pygame.mouse.get_pos()[0] >= 110 and pygame.mouse.get_pos()[1] >= 20 and pygame.mouse.get_pos()[0] <= 260 and pygame.mouse.get_pos()[1]<= 170 and p6==1 :
                        piecerect6=case0
                        p6=0
                        case[0][0]=piece6v

                    if pygame.mouse.get_pos()[0] >= 270 and pygame.mouse.get_pos()[1] >= 20 and pygame.mouse.get_pos()[0] <= 420 and pygame.mouse.get_pos()[1]<= 170 and p6==1 :
                        piecerect6=case1
                        p6=0
                        case[0][1]=piece6v

                    if pygame.mouse.get_pos()[0] >= 430 and pygame.mouse.get_pos()[1] >= 20 and pygame.mouse.get_pos()[0] <= 580 and pygame.mouse.get_pos()[1]<= 170 and p6==1 :
                        piecerect6=case2
                        p6=0
                        case[0][2]=piece6v

                    if pygame.mouse.get_pos()[0] >= 590 and pygame.mouse.get_pos()[1] >= 20 and pygame.mouse.get_pos()[0] <= 740 and pygame.mouse.get_pos()[1]<= 170 and p6==1 :
                        piecerect6=case3
                        p6=0
                        case[0][3]=piece6v

                    if pygame.mouse.get_pos()[0] >= 110 and pygame.mouse.get_pos()[1] >= 180 and pygame.mouse.get_pos()[0] <= 260 and pygame.mouse.get_pos()[1]<= 330 and p6==1 :
                        piecerect6=case4
                        p6=0
                        case[1][0]=piece6v

                    if pygame.mouse.get_pos()[0] >= 270 and pygame.mouse.get_pos()[1] >= 180 and pygame.mouse.get_pos()[0] <= 420 and pygame.mouse.get_pos()[1]<= 330 and p6==1 :
                        piecerect6=case5
                        p6=0
                        case[1][1]=piece6v

                    if pygame.mouse.get_pos()[0] >= 430 and pygame.mouse.get_pos()[1] >= 180 and pygame.mouse.get_pos()[0] <= 580 and pygame.mouse.get_pos()[1]<= 330 and p6==1 :
                        piecerect6=case6
                        p6=0
                        case[1][2]=piece6v

                    if pygame.mouse.get_pos()[0] >= 590 and pygame.mouse.get_pos()[1] >= 180 and pygame.mouse.get_pos()[0] <= 740 and pygame.mouse.get_pos()[1]<= 330 and p6==1 :
                        piecerect6=case7
                        p6=0
                        case[1][3]=piece6v

                    if pygame.mouse.get_pos()[0] >= 110 and pygame.mouse.get_pos()[1] >= 340 and pygame.mouse.get_pos()[0] <= 260 and pygame.mouse.get_pos()[1]<= 490 and p6==1 :
                        piecerect6=case8
                        p6=0
                        case[2][0]=piece6v

                    if pygame.mouse.get_pos()[0] >= 270 and pygame.mouse.get_pos()[1] >= 340 and pygame.mouse.get_pos()[0] <= 420 and pygame.mouse.get_pos()[1]<= 490 and p6==1 :
                        piecerect6=case9
                        p6=0
                        case[2][1]=piece6v

                    if pygame.mouse.get_pos()[0] >= 430 and pygame.mouse.get_pos()[1] >= 340 and pygame.mouse.get_pos()[0] <= 580 and pygame.mouse.get_pos()[1]<= 490 and p6==1 :
                        piecerect6=case10
                        p6=0
                        case[2][2]=piece6v

                    if pygame.mouse.get_pos()[0] >= 590 and pygame.mouse.get_pos()[1] >= 340 and pygame.mouse.get_pos()[0] <= 740 and pygame.mouse.get_pos()[1]<= 490 and p6==1 :
                        piecerect6=case11
                        p6=0
                        case[2][3]=piece6v

                    if pygame.mouse.get_pos()[0] >= 110 and pygame.mouse.get_pos()[1] >= 500 and pygame.mouse.get_pos()[0] <= 260 and pygame.mouse.get_pos()[1]<= 650 and p6==1 :
                        piecerect6=case12
                        p6=0
                        case[3][0]=piece6v

                    if pygame.mouse.get_pos()[0] >= 270 and pygame.mouse.get_pos()[1] >= 500 and pygame.mouse.get_pos()[0] <= 420 and pygame.mouse.get_pos()[1]<= 650 and p6==1 :
                        piecerect6=case13
                        p6=0
                        case[3][1]=piece6v

                    if pygame.mouse.get_pos()[0] >= 430 and pygame.mouse.get_pos()[1] >= 500 and pygame.mouse.get_pos()[0] <= 580 and pygame.mouse.get_pos()[1]<= 650 and p6==1 :
                        piecerect6=case14
                        p6=0
                        case[3][3]=piece6v

                    if pygame.mouse.get_pos()[0] >= 590 and pygame.mouse.get_pos()[1] >= 500 and pygame.mouse.get_pos()[0] <= 740 and pygame.mouse.get_pos()[1]<= 650 and p6==1 :
                        piecerect6=case15
                        p6=0
                        case[3][3]=piece6v


                     #mouvement pièce 7


                    if pygame.mouse.get_pos()[0] >= 1020 and pygame.mouse.get_pos()[1] >= 10 and pygame.mouse.get_pos()[0] <= 1140 and pygame.mouse.get_pos()[1]<=130 and p7==2:
                        p7=1
                    if pygame.mouse.get_pos()[0] >= 110 and pygame.mouse.get_pos()[1] >= 20 and pygame.mouse.get_pos()[0] <= 260 and pygame.mouse.get_pos()[1]<= 170 and p7==1 :
                        piecerect7=case0
                        p7=0
                        case[0][0]=piece7v

                    if pygame.mouse.get_pos()[0] >= 270 and pygame.mouse.get_pos()[1] >= 20 and pygame.mouse.get_pos()[0] <= 420 and pygame.mouse.get_pos()[1]<= 170 and p7==1 :
                        piecerect7=case1
                        p7=0
                        case[0][1]=piece7v

                    if pygame.mouse.get_pos()[0] >= 430 and pygame.mouse.get_pos()[1] >= 20 and pygame.mouse.get_pos()[0] <= 580 and pygame.mouse.get_pos()[1]<= 170 and p7==1 :
                        piecerect7=case2
                        p7=0
                        case[0][2]=piece7v

                    if pygame.mouse.get_pos()[0] >= 590 and pygame.mouse.get_pos()[1] >= 20 and pygame.mouse.get_pos()[0] <= 740 and pygame.mouse.get_pos()[1]<= 170 and p7==1 :
                        piecerect7=case3
                        p7=0
                        case[0][3]=piece7v

                    if pygame.mouse.get_pos()[0] >= 110 and pygame.mouse.get_pos()[1] >= 180 and pygame.mouse.get_pos()[0] <= 260 and pygame.mouse.get_pos()[1]<= 330 and p7==1 :
                        piecerect7=case4
                        p7=0
                        case[1][0]=piece7v

                    if pygame.mouse.get_pos()[0] >= 270 and pygame.mouse.get_pos()[1] >= 180 and pygame.mouse.get_pos()[0] <= 420 and pygame.mouse.get_pos()[1]<= 330 and p7==1 :
                        piecerect7=case5
                        p7=0
                        case[1][1]=piece7v

                    if pygame.mouse.get_pos()[0] >= 430 and pygame.mouse.get_pos()[1] >= 180 and pygame.mouse.get_pos()[0] <= 580 and pygame.mouse.get_pos()[1]<= 330 and p7==1 :
                        piecerect7=case6
                        p7=0
                        case[1][2]=piece7v

                    if pygame.mouse.get_pos()[0] >= 590 and pygame.mouse.get_pos()[1] >= 180 and pygame.mouse.get_pos()[0] <= 740 and pygame.mouse.get_pos()[1]<= 330 and p7==1 :
                        piecerect7=case7
                        p7=0
                        case[1][3]=piece7v

                    if pygame.mouse.get_pos()[0] >= 110 and pygame.mouse.get_pos()[1] >= 340 and pygame.mouse.get_pos()[0] <= 260 and pygame.mouse.get_pos()[1]<= 490 and p7==1 :
                        piecerect7=case8
                        p7=0
                        case[2][0]=piece7v

                    if pygame.mouse.get_pos()[0] >= 270 and pygame.mouse.get_pos()[1] >= 340 and pygame.mouse.get_pos()[0] <= 420 and pygame.mouse.get_pos()[1]<= 490 and p7==1 :
                        piecerect7=case9
                        p7=0
                        case[2][1]=piece7v

                    if pygame.mouse.get_pos()[0] >= 430 and pygame.mouse.get_pos()[1] >= 340 and pygame.mouse.get_pos()[0] <= 580 and pygame.mouse.get_pos()[1]<= 490 and p7==1 :
                        piecerect7=case10
                        p7=0
                        case[2][2]=piece7v

                    if pygame.mouse.get_pos()[0] >= 590 and pygame.mouse.get_pos()[1] >= 340 and pygame.mouse.get_pos()[0] <= 740 and pygame.mouse.get_pos()[1]<= 490 and p7==1 :
                        piecerect7=case11
                        p7=0
                        case[2][3]=piece7v

                    if pygame.mouse.get_pos()[0] >= 110 and pygame.mouse.get_pos()[1] >= 500 and pygame.mouse.get_pos()[0] <= 260 and pygame.mouse.get_pos()[1]<= 650 and p7==1 :
                        piecerect7=case12
                        p7=0
                        case[3][0]=piece7v

                    if pygame.mouse.get_pos()[0] >= 270 and pygame.mouse.get_pos()[1] >= 500 and pygame.mouse.get_pos()[0] <= 420 and pygame.mouse.get_pos()[1]<= 650 and p7==1 :
                        piecerect7=case13
                        p7=0
                        case[3][1]=piece7v

                    if pygame.mouse.get_pos()[0] >= 430 and pygame.mouse.get_pos()[1] >= 500 and pygame.mouse.get_pos()[0] <= 580 and pygame.mouse.get_pos()[1]<= 650 and p7==1 :
                        piecerect7=case14
                        p7=0
                        case[3][2]=piece7v

                    if pygame.mouse.get_pos()[0] >= 590 and pygame.mouse.get_pos()[1] >= 500 and pygame.mouse.get_pos()[0] <= 740 and pygame.mouse.get_pos()[1]<= 650 and p7==1 :
                        piecerect7=case15
                        p7=0
                        case[3][3]=piece7v


                     #mouvement pièce 8


                    if pygame.mouse.get_pos()[0] >= 900 and pygame.mouse.get_pos()[1] >= 10 and pygame.mouse.get_pos()[0] <= 1020 and pygame.mouse.get_pos()[1]<=130 and p8==2:
                        p8=1
                    if pygame.mouse.get_pos()[0] >= 110 and pygame.mouse.get_pos()[1] >= 20 and pygame.mouse.get_pos()[0] <= 260 and pygame.mouse.get_pos()[1]<= 170 and p8==1 :
                        piecerect8=case0
                        p8=0
                        case[0][0]=piece8v

                    if pygame.mouse.get_pos()[0] >= 270 and pygame.mouse.get_pos()[1] >= 20 and pygame.mouse.get_pos()[0] <= 420 and pygame.mouse.get_pos()[1]<= 170 and p8==1 :
                        piecerect8=case1
                        p8=0
                        case[0][1]=piece8v

                    if pygame.mouse.get_pos()[0] >= 430 and pygame.mouse.get_pos()[1] >= 20 and pygame.mouse.get_pos()[0] <= 580 and pygame.mouse.get_pos()[1]<= 170 and p8==1 :
                        piecerect8=case2
                        p8=0
                        case[0][2]=piece8v

                    if pygame.mouse.get_pos()[0] >= 590 and pygame.mouse.get_pos()[1] >= 20 and pygame.mouse.get_pos()[0] <= 740 and pygame.mouse.get_pos()[1]<= 170 and p8==1 :
                        piecerect8=case3
                        p8=0
                        case[0][3]=piece8v

                    if pygame.mouse.get_pos()[0] >= 110 and pygame.mouse.get_pos()[1] >= 180 and pygame.mouse.get_pos()[0] <= 260 and pygame.mouse.get_pos()[1]<= 330 and p8==1 :
                        piecerect8=case4
                        p8=0
                        case[1][0]=piece8v

                    if pygame.mouse.get_pos()[0] >= 270 and pygame.mouse.get_pos()[1] >= 180 and pygame.mouse.get_pos()[0] <= 420 and pygame.mouse.get_pos()[1]<= 330 and p8==1 :
                        piecerect8=case5
                        p8=0
                        case[1][1]=piece8v

                    if pygame.mouse.get_pos()[0] >= 430 and pygame.mouse.get_pos()[1] >= 180 and pygame.mouse.get_pos()[0] <= 580 and pygame.mouse.get_pos()[1]<= 330 and p8==1 :
                        piecerect8=case6
                        p8=0
                        case[1][2]=piece8v

                    if pygame.mouse.get_pos()[0] >= 590 and pygame.mouse.get_pos()[1] >= 180 and pygame.mouse.get_pos()[0] <= 740 and pygame.mouse.get_pos()[1]<= 330 and p8==1 :
                        piecerect8=case7
                        p8=0
                        case[1][3]=piece8v

                    if pygame.mouse.get_pos()[0] >= 110 and pygame.mouse.get_pos()[1] >= 340 and pygame.mouse.get_pos()[0] <= 260 and pygame.mouse.get_pos()[1]<= 490 and p8==1 :
                        piecerect8=case8
                        p8=0
                        case[2][0]=piece8v

                    if pygame.mouse.get_pos()[0] >= 270 and pygame.mouse.get_pos()[1] >= 340 and pygame.mouse.get_pos()[0] <= 420 and pygame.mouse.get_pos()[1]<= 490 and p8==1 :
                        piecerect8=case9
                        p8=0
                        case[2][1]=piece8v

                    if pygame.mouse.get_pos()[0] >= 430 and pygame.mouse.get_pos()[1] >= 340 and pygame.mouse.get_pos()[0] <= 580 and pygame.mouse.get_pos()[1]<= 490 and p8==1 :
                        piecerect8=case10
                        p8=0
                        case[2][2]=piece8v

                    if pygame.mouse.get_pos()[0] >= 590 and pygame.mouse.get_pos()[1] >= 340 and pygame.mouse.get_pos()[0] <= 740 and pygame.mouse.get_pos()[1]<= 490 and p8==1 :
                        piecerect8=case11
                        p8=0
                        case[2][3]=piece8v

                    if pygame.mouse.get_pos()[0] >= 110 and pygame.mouse.get_pos()[1] >= 500 and pygame.mouse.get_pos()[0] <= 260 and pygame.mouse.get_pos()[1]<= 650 and p8==1 :
                        piecerect8=case12
                        p8=0
                        case[3][0]=piece8v

                    if pygame.mouse.get_pos()[0] >= 270 and pygame.mouse.get_pos()[1] >= 500 and pygame.mouse.get_pos()[0] <= 420 and pygame.mouse.get_pos()[1]<= 650 and p8==1 :
                        piecerect8=case13
                        p8=0
                        case[3][1]=piece8v

                    if pygame.mouse.get_pos()[0] >= 430 and pygame.mouse.get_pos()[1] >= 500 and pygame.mouse.get_pos()[0] <= 580 and pygame.mouse.get_pos()[1]<= 650 and p8==1 :
                        piecerect8=case14
                        p8=0
                        case[3][2]=piece8v

                    if pygame.mouse.get_pos()[0] >= 590 and pygame.mouse.get_pos()[1] >= 500 and pygame.mouse.get_pos()[0] <= 740 and pygame.mouse.get_pos()[1]<= 650 and p8==1 :
                        piecerect8=case15
                        p8=0
                        case[3][3]=piece8v



                    #mouvement pièce 9


                    if pygame.mouse.get_pos()[0] >= 765 and pygame.mouse.get_pos()[1] >= 15 and pygame.mouse.get_pos()[0] <= 860 and pygame.mouse.get_pos()[1]<=105 and p9==2:
                        p9=1
                    if pygame.mouse.get_pos()[0] >= 110 and pygame.mouse.get_pos()[1] >= 20 and pygame.mouse.get_pos()[0] <= 260 and pygame.mouse.get_pos()[1]<= 170 and p9==1 :
                        piecerect9=case0
                        p9=0
                        case[0][0]=piece9v

                    if pygame.mouse.get_pos()[0] >= 270 and pygame.mouse.get_pos()[1] >= 20 and pygame.mouse.get_pos()[0] <= 420 and pygame.mouse.get_pos()[1]<= 170 and p9==1 :
                        piecerect9=case1
                        p9=0
                        case[0][1]=piece9v

                    if pygame.mouse.get_pos()[0] >= 430 and pygame.mouse.get_pos()[1] >= 20 and pygame.mouse.get_pos()[0] <= 580 and pygame.mouse.get_pos()[1]<= 170 and p9==1 :
                        piecerect9=case2
                        p9=0
                        case[0][2]=piece9v

                    if pygame.mouse.get_pos()[0] >= 590 and pygame.mouse.get_pos()[1] >= 20 and pygame.mouse.get_pos()[0] <= 740 and pygame.mouse.get_pos()[1]<= 170 and p9==1 :
                        piecerect9=case3
                        p9=0
                        case[0][3]=piece9v

                    if pygame.mouse.get_pos()[0] >= 110 and pygame.mouse.get_pos()[1] >= 180 and pygame.mouse.get_pos()[0] <= 260 and pygame.mouse.get_pos()[1]<= 330 and p9==1 :
                        piecerect9=case4
                        p9=0
                        case[1][0]=piece9v

                    if pygame.mouse.get_pos()[0] >= 270 and pygame.mouse.get_pos()[1] >= 180 and pygame.mouse.get_pos()[0] <= 420 and pygame.mouse.get_pos()[1]<= 330 and p9==1 :
                        piecerect9=case5
                        p9=0
                        case[1][1]=piece9v

                    if pygame.mouse.get_pos()[0] >= 430 and pygame.mouse.get_pos()[1] >= 180 and pygame.mouse.get_pos()[0] <= 580 and pygame.mouse.get_pos()[1]<= 330 and p9==1 :
                        piecerect9=case6
                        p9=0
                        case[1][2]=piece9v

                    if pygame.mouse.get_pos()[0] >= 590 and pygame.mouse.get_pos()[1] >= 180 and pygame.mouse.get_pos()[0] <= 740 and pygame.mouse.get_pos()[1]<= 330 and p9==1 :
                        piecerect9=case7
                        p9=0
                        case[1][3]=piece9v

                    if pygame.mouse.get_pos()[0] >= 110 and pygame.mouse.get_pos()[1] >= 340 and pygame.mouse.get_pos()[0] <= 260 and pygame.mouse.get_pos()[1]<= 490 and p9==1 :
                        piecerect9=case8
                        p9=0
                        case[2][0]=piece9v

                    if pygame.mouse.get_pos()[0] >= 270 and pygame.mouse.get_pos()[1] >= 340 and pygame.mouse.get_pos()[0] <= 420 and pygame.mouse.get_pos()[1]<= 490 and p9==1 :
                        piecerect9=case9
                        p9=0
                        case[2][1]=piece9v

                    if pygame.mouse.get_pos()[0] >= 430 and pygame.mouse.get_pos()[1] >= 340 and pygame.mouse.get_pos()[0] <= 580 and pygame.mouse.get_pos()[1]<= 490 and p9==1 :
                        piecerect9=case10
                        p9=0
                        case[2][2]=piece9v

                    if pygame.mouse.get_pos()[0] >= 590 and pygame.mouse.get_pos()[1] >= 340 and pygame.mouse.get_pos()[0] <= 740 and pygame.mouse.get_pos()[1]<= 490 and p9==1 :
                        piecerect9=case11
                        p9=0
                        case[2][3]=piece9v

                    if pygame.mouse.get_pos()[0] >= 110 and pygame.mouse.get_pos()[1] >= 500 and pygame.mouse.get_pos()[0] <= 260 and pygame.mouse.get_pos()[1]<= 650 and p9==1 :
                        piecerect9=case12
                        p9=0
                        case[3][0]=piece9v

                    if pygame.mouse.get_pos()[0] >= 270 and pygame.mouse.get_pos()[1] >= 500 and pygame.mouse.get_pos()[0] <= 420 and pygame.mouse.get_pos()[1]<= 650 and p9==1 :
                        piecerect9=case13
                        p9=0
                        case[3][1]=piece9v

                    if pygame.mouse.get_pos()[0] >= 430 and pygame.mouse.get_pos()[1] >= 500 and pygame.mouse.get_pos()[0] <= 580 and pygame.mouse.get_pos()[1]<= 650 and p9==1 :
                        piecerect9=case14
                        p9=0
                        case[3][2]=piece9v

                    if pygame.mouse.get_pos()[0] >= 590 and pygame.mouse.get_pos()[1] >= 500 and pygame.mouse.get_pos()[0] <= 740 and pygame.mouse.get_pos()[1]<= 650 and p9==1 :
                        piecerect9=case15
                        p9=0
                        case[3][3]=piece9v


                     #mouvement pièce 10



                    if pygame.mouse.get_pos()[0] >= 765 and pygame.mouse.get_pos()[1] >= 150 and pygame.mouse.get_pos()[0] <= 850 and pygame.mouse.get_pos()[1]<=250 and p10==2:
                        p10=1
                    if pygame.mouse.get_pos()[0] >= 110 and pygame.mouse.get_pos()[1] >= 20 and pygame.mouse.get_pos()[0] <= 260 and pygame.mouse.get_pos()[1]<= 170 and p10==1 :
                        piecerect10=case0
                        p10=0
                        case[0][0]=piece10v

                    if pygame.mouse.get_pos()[0] >= 270 and pygame.mouse.get_pos()[1] >= 20 and pygame.mouse.get_pos()[0] <= 420 and pygame.mouse.get_pos()[1]<= 170 and p10==1 :
                        piecerect10=case1
                        p10=0
                        case[0][1]=piece10v

                    if pygame.mouse.get_pos()[0] >= 430 and pygame.mouse.get_pos()[1] >= 20 and pygame.mouse.get_pos()[0] <= 580 and pygame.mouse.get_pos()[1]<= 170 and p10==1 :
                        piecerect10=case2
                        p10=0
                        case[0][2]=piece10v

                    if pygame.mouse.get_pos()[0] >= 590 and pygame.mouse.get_pos()[1] >= 20 and pygame.mouse.get_pos()[0] <= 740 and pygame.mouse.get_pos()[1]<= 170 and p10==1 :
                        piecerect10=case3
                        p10=0
                        case[0][3]=piece10v

                    if pygame.mouse.get_pos()[0] >= 110 and pygame.mouse.get_pos()[1] >= 180 and pygame.mouse.get_pos()[0] <= 260 and pygame.mouse.get_pos()[1]<= 330 and p10==1 :
                        piecerect10=case4
                        p10=0
                        case[1][0]=piece10v

                    if pygame.mouse.get_pos()[0] >= 270 and pygame.mouse.get_pos()[1] >= 180 and pygame.mouse.get_pos()[0] <= 420 and pygame.mouse.get_pos()[1]<= 330 and p10==1 :
                        piecerect10=case5
                        p10=0
                        case[1][1]=piece10v

                    if pygame.mouse.get_pos()[0] >= 430 and pygame.mouse.get_pos()[1] >= 180 and pygame.mouse.get_pos()[0] <= 580 and pygame.mouse.get_pos()[1]<= 330 and p10==1 :
                        piecerect10=case6
                        p10=0
                        case[1][2]=piece10v

                    if pygame.mouse.get_pos()[0] >= 590 and pygame.mouse.get_pos()[1] >= 180 and pygame.mouse.get_pos()[0] <= 740 and pygame.mouse.get_pos()[1]<= 330 and p10==1 :
                        piecerect10=case7
                        p10=0
                        case[1][3]=piece10v

                    if pygame.mouse.get_pos()[0] >= 110 and pygame.mouse.get_pos()[1] >= 340 and pygame.mouse.get_pos()[0] <= 260 and pygame.mouse.get_pos()[1]<= 490 and p10==1 :
                        piecerect10=case8
                        p10=0
                        case[2][0]=piece10v

                    if pygame.mouse.get_pos()[0] >= 270 and pygame.mouse.get_pos()[1] >= 340 and pygame.mouse.get_pos()[0] <= 420 and pygame.mouse.get_pos()[1]<= 490 and p10==1 :
                        piecerect10=case9
                        p10=0
                        case[2][1]=piece10v

                    if pygame.mouse.get_pos()[0] >= 430 and pygame.mouse.get_pos()[1] >= 340 and pygame.mouse.get_pos()[0] <= 580 and pygame.mouse.get_pos()[1]<= 490 and p10==1 :
                        piecerect10=case10
                        p10=0
                        case[2][2]=piece10v

                    if pygame.mouse.get_pos()[0] >= 590 and pygame.mouse.get_pos()[1] >= 340 and pygame.mouse.get_pos()[0] <= 740 and pygame.mouse.get_pos()[1]<= 490 and p10==1 :
                        piecerect10=case11
                        p10=0
                        case[2][3]=piece10v

                    if pygame.mouse.get_pos()[0] >= 110 and pygame.mouse.get_pos()[1] >= 500 and pygame.mouse.get_pos()[0] <= 260 and pygame.mouse.get_pos()[1]<= 650 and p10==1 :
                        piecerect10=case12
                        p10=0
                        case[3][0]=piece10v

                    if pygame.mouse.get_pos()[0] >= 270 and pygame.mouse.get_pos()[1] >= 500 and pygame.mouse.get_pos()[0] <= 420 and pygame.mouse.get_pos()[1]<= 650 and p10==1 :
                        piecerect10=case13
                        p10=0
                        case[3][1]=piece10v

                    if pygame.mouse.get_pos()[0] >= 430 and pygame.mouse.get_pos()[1] >= 500 and pygame.mouse.get_pos()[0] <= 580 and pygame.mouse.get_pos()[1]<= 650 and p10==1 :
                        piecerect10=case14
                        p10=0
                        case[3][2]=piece10v

                    if pygame.mouse.get_pos()[0] >= 590 and pygame.mouse.get_pos()[1] >= 500 and pygame.mouse.get_pos()[0] <= 740 and pygame.mouse.get_pos()[1]<= 650 and p10==1 :
                        piecerect10=case15
                        p10=0
                        case[3][3]=piece10v


                    #mouvement pièce 11



                    if pygame.mouse.get_pos()[0] >= 770 and pygame.mouse.get_pos()[1] >= 275 and pygame.mouse.get_pos()[0] <= 865 and pygame.mouse.get_pos()[1]<=370 and p11==2:
                        p11=1
                    if pygame.mouse.get_pos()[0] >= 110 and pygame.mouse.get_pos()[1] >= 20 and pygame.mouse.get_pos()[0] <= 260 and pygame.mouse.get_pos()[1]<= 170 and p11==1 :
                        piecerect11=case0
                        p11=0
                        case[0][0]=piece11v

                    if pygame.mouse.get_pos()[0] >= 270 and pygame.mouse.get_pos()[1] >= 20 and pygame.mouse.get_pos()[0] <= 420 and pygame.mouse.get_pos()[1]<= 170 and p11==1 :
                        piecerect11=case1
                        p11=0
                        case[0][1]=piece11v

                    if pygame.mouse.get_pos()[0] >= 430 and pygame.mouse.get_pos()[1] >= 20 and pygame.mouse.get_pos()[0] <= 580 and pygame.mouse.get_pos()[1]<= 170 and p11==1 :
                        piecerect11=case2
                        p11=0
                        case[0][2]=piece11v

                    if pygame.mouse.get_pos()[0] >= 590 and pygame.mouse.get_pos()[1] >= 20 and pygame.mouse.get_pos()[0] <= 740 and pygame.mouse.get_pos()[1]<= 170 and p11==1 :
                        piecerect11=case3
                        p11=0
                        case[0][3]=piece11v

                    if pygame.mouse.get_pos()[0] >= 110 and pygame.mouse.get_pos()[1] >= 180 and pygame.mouse.get_pos()[0] <= 260 and pygame.mouse.get_pos()[1]<= 330 and p11==1 :
                        piecerect11=case4
                        p11=0
                        case[1][0]=piece11v

                    if pygame.mouse.get_pos()[0] >= 270 and pygame.mouse.get_pos()[1] >= 180 and pygame.mouse.get_pos()[0] <= 420 and pygame.mouse.get_pos()[1]<= 330 and p11==1 :
                        piecerect11=case5
                        p11=0
                        case[1][1]=piece11v

                    if pygame.mouse.get_pos()[0] >= 430 and pygame.mouse.get_pos()[1] >= 180 and pygame.mouse.get_pos()[0] <= 580 and pygame.mouse.get_pos()[1]<= 330 and p11==1 :
                        piecerect11=case6
                        p11=0
                        case[1][2]=piece11v

                    if pygame.mouse.get_pos()[0] >= 590 and pygame.mouse.get_pos()[1] >= 180 and pygame.mouse.get_pos()[0] <= 740 and pygame.mouse.get_pos()[1]<= 330 and p11==1 :
                        piecerect11=case7
                        p11=0
                        case[1][3]=piece11v

                    if pygame.mouse.get_pos()[0] >= 110 and pygame.mouse.get_pos()[1] >= 340 and pygame.mouse.get_pos()[0] <= 260 and pygame.mouse.get_pos()[1]<= 490 and p11==1 :
                        piecerect11=case8
                        p11=0
                        case[2][0]=piece11v

                    if pygame.mouse.get_pos()[0] >= 270 and pygame.mouse.get_pos()[1] >= 340 and pygame.mouse.get_pos()[0] <= 420 and pygame.mouse.get_pos()[1]<= 490 and p11==1 :
                        piecerect11=case9
                        p11=0
                        case[2][1]=piece11v

                    if pygame.mouse.get_pos()[0] >= 430 and pygame.mouse.get_pos()[1] >= 340 and pygame.mouse.get_pos()[0] <= 580 and pygame.mouse.get_pos()[1]<= 490 and p11==1 :
                        piecerect11=case10
                        p11=0
                        case[2][2]=piece11v

                    if pygame.mouse.get_pos()[0] >= 590 and pygame.mouse.get_pos()[1] >= 340 and pygame.mouse.get_pos()[0] <= 740 and pygame.mouse.get_pos()[1]<= 490 and p11==1 :
                        piecerect11=case11
                        p11=0
                        case[2][3]=piece11v

                    if pygame.mouse.get_pos()[0] >= 110 and pygame.mouse.get_pos()[1] >= 500 and pygame.mouse.get_pos()[0] <= 260 and pygame.mouse.get_pos()[1]<= 650 and p11==1 :
                        piecerect11=case12
                        p11=0
                        case[3][0]=piece11v

                    if pygame.mouse.get_pos()[0] >= 270 and pygame.mouse.get_pos()[1] >= 500 and pygame.mouse.get_pos()[0] <= 420 and pygame.mouse.get_pos()[1]<= 650 and p11==1 :
                        piecerect11=case13
                        p11=0
                        case[3][1]=piece11v

                    if pygame.mouse.get_pos()[0] >= 430 and pygame.mouse.get_pos()[1] >= 500 and pygame.mouse.get_pos()[0] <= 580 and pygame.mouse.get_pos()[1]<= 650 and p11==1 :
                        piecerect11=case14
                        p11=0
                        case[3][2]=piece11v

                    if pygame.mouse.get_pos()[0] >= 590 and pygame.mouse.get_pos()[1] >= 500 and pygame.mouse.get_pos()[0] <= 740 and pygame.mouse.get_pos()[1]<= 650 and p11==1 :
                        piecerect11=case15
                        p11=0
                        case[3][3]=piece11v

                    #tests
                    if pygame.mouse.get_pos()[0]>=950 and pygame.mouse.get_pos()[0]<=1088 and pygame.mouse.get_pos()[1]<=732 and pygame.mouse.get_pos()[0]>=575  :

                       test(case)




                    #bouton reset
                    if pygame.mouse.get_pos()[0] >= 1140 and pygame.mouse.get_pos()[1] >= 617 and pygame.mouse.get_pos()[0] <= 1302 and pygame.mouse.get_pos()[1]<=767:
                        piecerect1=pygame.Rect(900,150,100,50)
                        piecerect2=pygame.Rect(900,300,100,50)
                        piecerect3=pygame.Rect(900,450,100,50)
                        piecerect4=pygame.Rect(1020,150,100,50)
                        piecerect5=pygame.Rect(1020,300,100,50)
                        piecerect6=pygame.Rect(1020,450,100,50)
                        piecerect7=pygame.Rect(1020,10,100,50)
                        piecerect8=pygame.Rect(870,10,100,50)
                        piecerect9=pygame.Rect(759,10,95,99)
                        piecerect10=pygame.Rect(765,150,95,99)
                        piecerect11=pygame.Rect(770,275,95,99)

                        p1=2
                        p2=2
                        p3=2
                        p4=2
                        p5=2
                        p6=2
                        p7=2
                        p8=2
                        p9=2
                        p10=2
                        p11=2


        fenetre.blit(fond, (0,0))
        fenetre.blit(reset,resetrect)
        fenetre.blit(piece1, piecerect1)
        fenetre.blit(piece2, piecerect2)
        fenetre.blit(piece3,piecerect3)
        fenetre.blit(piece4,piecerect4)
        fenetre.blit(piece5,piecerect5)
        fenetre.blit(piece6,piecerect6)
        fenetre.blit(piece7,piecerect7)
        fenetre.blit(piece8,piecerect8)
        fenetre.blit(piece9,piecerect9)
        fenetre.blit(piece10,piecerect10)
        fenetre.blit(piece11,piecerect11)

        fenetre.blit(lepouce,lepoucerect)

        pygame.display.flip()


finally:
    pygame.quit()
    exit()