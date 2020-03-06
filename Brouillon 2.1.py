import sys, pygame
from pygame.locals import *

pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((1302, 739))
piecerect1=pygame.Rect(50,50,100,50)

#Chargement et collage du fond

fond = pygame.image.load("fond.png").convert() # insere une image et la convertie au bon format"perso= pygame.image.load("perso.png").convert_alpha()

#Chargement et collage du personnage

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

p1=0
p2=0
p3=0
p4=0
p5=0
p6=0
p7=0
p8=0
p9=0

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
piecerect9=pygame.Rect(765,15,95,99)


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
case=[[0 for i in range(4) ] for i in range(4) ]



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
                    if pygame.mouse.get_pos()[0] >= 800 and pygame.mouse.get_pos()[1] >= 100 and pygame.mouse.get_pos()[0] <= 1020 and pygame.mouse.get_pos()[1]<=320:
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



                    if pygame.mouse.get_pos()[0] >= 900 and pygame.mouse.get_pos()[1] >= 300 and pygame.mouse.get_pos()[0] <= 1020 and pygame.mouse.get_pos()[1]<=420:
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



                    if pygame.mouse.get_pos()[0] >= 900 and pygame.mouse.get_pos()[1] >= 450 and pygame.mouse.get_pos()[0] <= 1020 and pygame.mouse.get_pos()[1]<=570:
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




                    if pygame.mouse.get_pos()[0] >= 1020 and pygame.mouse.get_pos()[1] >= 150 and pygame.mouse.get_pos()[0] <= 1140 and pygame.mouse.get_pos()[1]<=270:
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


                    if pygame.mouse.get_pos()[0] >= 1020 and pygame.mouse.get_pos()[1] >= 300 and pygame.mouse.get_pos()[0] <= 1140 and pygame.mouse.get_pos()[1]<=420:
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
                        case[0][3]=piece4v

                    if pygame.mouse.get_pos()[0] >= 110 and pygame.mouse.get_pos()[1] >= 180 and pygame.mouse.get_pos()[0] <= 260 and pygame.mouse.get_pos()[1]<= 330 and p5==1 :
                        piecerect5=case4
                        p5=0
                        case[1][0]=piece4v

                    if pygame.mouse.get_pos()[0] >= 270 and pygame.mouse.get_pos()[1] >= 180 and pygame.mouse.get_pos()[0] <= 420 and pygame.mouse.get_pos()[1]<= 330 and p5==1 :
                        piecerect5=case5
                        p5=0
                        case[1][1]=piece4v

                    if pygame.mouse.get_pos()[0] >= 430 and pygame.mouse.get_pos()[1] >= 180 and pygame.mouse.get_pos()[0] <= 580 and pygame.mouse.get_pos()[1]<= 330 and p5==1 :
                        piecerect5=case6
                        p5=0
                        case[1][2]=piece4v

                    if pygame.mouse.get_pos()[0] >= 590 and pygame.mouse.get_pos()[1] >= 180 and pygame.mouse.get_pos()[0] <= 740 and pygame.mouse.get_pos()[1]<= 330 and p5==1 :
                        piecerect5=case7
                        p5=0
                        case[1][3]=piece4v

                    if pygame.mouse.get_pos()[0] >= 110 and pygame.mouse.get_pos()[1] >= 340 and pygame.mouse.get_pos()[0] <= 260 and pygame.mouse.get_pos()[1]<= 490 and p5==1 :
                        piecerect5=case8
                        p5=0
                        case[2][0]=piece4v

                    if pygame.mouse.get_pos()[0] >= 270 and pygame.mouse.get_pos()[1] >= 340 and pygame.mouse.get_pos()[0] <= 420 and pygame.mouse.get_pos()[1]<= 490 and p5==1 :
                        piecerect5=case9
                        p5=0
                        case[2][1]=piece4v

                    if pygame.mouse.get_pos()[0] >= 430 and pygame.mouse.get_pos()[1] >= 340 and pygame.mouse.get_pos()[0] <= 580 and pygame.mouse.get_pos()[1]<= 490 and p5==1 :
                        piecerect5=case10
                        p5=0
                        case[2][2]=piece4v

                    if pygame.mouse.get_pos()[0] >= 590 and pygame.mouse.get_pos()[1] >= 340 and pygame.mouse.get_pos()[0] <= 740 and pygame.mouse.get_pos()[1]<= 490 and p5==1 :
                        piecerect5=case11
                        p5=0
                        case[2][3]=piece4v

                    if pygame.mouse.get_pos()[0] >= 110 and pygame.mouse.get_pos()[1] >= 500 and pygame.mouse.get_pos()[0] <= 260 and pygame.mouse.get_pos()[1]<= 650 and p5==1 :
                        piecerect5=case12
                        p5=0
                        case[3][0]=piece4v

                    if pygame.mouse.get_pos()[0] >= 270 and pygame.mouse.get_pos()[1] >= 500 and pygame.mouse.get_pos()[0] <= 420 and pygame.mouse.get_pos()[1]<= 650 and p5==1 :
                        piecerect5=case13
                        p5=0
                        case[3][1]=piece4v

                    if pygame.mouse.get_pos()[0] >= 430 and pygame.mouse.get_pos()[1] >= 500 and pygame.mouse.get_pos()[0] <= 580 and pygame.mouse.get_pos()[1]<= 650 and p5==1 :
                        piecerect5=case14
                        p5=0
                        case[3][2]=piece4v

                    if pygame.mouse.get_pos()[0] >= 590 and pygame.mouse.get_pos()[1] >= 500 and pygame.mouse.get_pos()[0] <= 740 and pygame.mouse.get_pos()[1]<= 650 and p5==1 :
                        piecerect5=case15
                        p5=0
                        case[3][1]=piece4v


                    #mouvement pièce 6


                    if pygame.mouse.get_pos()[0] >= 1020 and pygame.mouse.get_pos()[1] >= 450 and pygame.mouse.get_pos()[0] <= 1140 and pygame.mouse.get_pos()[1]<=570:
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


                    if pygame.mouse.get_pos()[0] >= 1020 and pygame.mouse.get_pos()[1] >= 10 and pygame.mouse.get_pos()[0] <= 1140 and pygame.mouse.get_pos()[1]<=130:
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


                    if pygame.mouse.get_pos()[0] >= 900 and pygame.mouse.get_pos()[1] >= 10 and pygame.mouse.get_pos()[0] <= 1020 and pygame.mouse.get_pos()[1]<=130:
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


                    if pygame.mouse.get_pos()[0] >= 765 and pygame.mouse.get_pos()[1] >= 15 and pygame.mouse.get_pos()[0] <= 860 and pygame.mouse.get_pos()[1]<=105:
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
                    if pygame.mouse.get_pos()[0] >= 110 and pygame.mouse.get_pos()[1] >= 180 and pygame.mouse.get_pos()[0] <= 260 and pygame.mouse.get_pos()[1]<= 330 and p9==1 :
                        piecerect9=case4
                        p9=0
                    if pygame.mouse.get_pos()[0] >= 270 and pygame.mouse.get_pos()[1] >= 180 and pygame.mouse.get_pos()[0] <= 420 and pygame.mouse.get_pos()[1]<= 330 and p9==1 :
                        piecerect9=case5
                        p9=0
                    if pygame.mouse.get_pos()[0] >= 430 and pygame.mouse.get_pos()[1] >= 180 and pygame.mouse.get_pos()[0] <= 580 and pygame.mouse.get_pos()[1]<= 330 and p9==1 :
                        piecerect9=case6
                        p9=0
                    if pygame.mouse.get_pos()[0] >= 590 and pygame.mouse.get_pos()[1] >= 180 and pygame.mouse.get_pos()[0] <= 740 and pygame.mouse.get_pos()[1]<= 330 and p9==1 :
                        piecerect9=case7
                        p9=0
                    if pygame.mouse.get_pos()[0] >= 110 and pygame.mouse.get_pos()[1] >= 340 and pygame.mouse.get_pos()[0] <= 260 and pygame.mouse.get_pos()[1]<= 490 and p9==1 :
                        piecerect9=case8
                        p9=0
                    if pygame.mouse.get_pos()[0] >= 270 and pygame.mouse.get_pos()[1] >= 340 and pygame.mouse.get_pos()[0] <= 420 and pygame.mouse.get_pos()[1]<= 490 and p9==1 :
                        piecerect9=case9
                        p9=0
                    if pygame.mouse.get_pos()[0] >= 430 and pygame.mouse.get_pos()[1] >= 340 and pygame.mouse.get_pos()[0] <= 580 and pygame.mouse.get_pos()[1]<= 490 and p9==1 :
                        piecerect9=case10
                        p9=0
                    if pygame.mouse.get_pos()[0] >= 590 and pygame.mouse.get_pos()[1] >= 340 and pygame.mouse.get_pos()[0] <= 740 and pygame.mouse.get_pos()[1]<= 490 and p9==1 :
                        piecerect9=case11
                        p9=0
                    if pygame.mouse.get_pos()[0] >= 110 and pygame.mouse.get_pos()[1] >= 500 and pygame.mouse.get_pos()[0] <= 260 and pygame.mouse.get_pos()[1]<= 650 and p9==1 :
                        piecerect9=case12
                        p9=0
                    if pygame.mouse.get_pos()[0] >= 270 and pygame.mouse.get_pos()[1] >= 500 and pygame.mouse.get_pos()[0] <= 420 and pygame.mouse.get_pos()[1]<= 650 and p9==1 :
                        piecerect9=case13
                        p9=0
                    if pygame.mouse.get_pos()[0] >= 430 and pygame.mouse.get_pos()[1] >= 500 and pygame.mouse.get_pos()[0] <= 580 and pygame.mouse.get_pos()[1]<= 650 and p9==1 :
                        piecerect9=case14
                        p9=0
                    if pygame.mouse.get_pos()[0] >= 590 and pygame.mouse.get_pos()[1] >= 500 and pygame.mouse.get_pos()[0] <= 740 and pygame.mouse.get_pos()[1]<= 650 and p9==1 :
                        piecerect9=case15
                        p9=0

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
                        piecerect9=pygame.Rect(765,10,95,99)










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
        pygame.display.flip()


finally:
    pygame.quit()
    exit()