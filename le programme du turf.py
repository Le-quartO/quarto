import sys, pygame

from pygame.locals import *

pygame.init()


# importation de la fonction test

from fonctions_test import test


#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((1302, 739))
piecerect1=pygame.Rect(50,50,100,50)

#Chargement et collage du fond


fond = pygame.image.load("image/fond.png").convert() # insere une image et la convertie au bon format"perso= pygame.image.load("perso.png").convert_alpha()

#Chargement et collage du pouce et du bouton restart
lepouce= pygame.image.load("image/lepouce.png").convert_alpha()
reset = pygame.image.load("image/restart.png").convert_alpha()

#chargement et collage des pieces
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
piece12 = pygame.image.load("piece/12.png").convert_alpha()

#création de la liste piece
piece=[piece1,piece2,piece3,piece4,piece5,piece6,piece7,piece8,piece9,piece10,piece11,piece12]

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
piece11v="CBPS"
piece12v="CMPS"
#creation de la liste de chaines de caractere des pieces
piecev=[piece1v,piece2v,piece3v,piece4v,piece5v,piece6v,piece7v,piece8v,piece9v,piece10v,piece11v,piece12v]


#creation de la liste p
p=[2 for i in range(16)]


# définition des rectangles dans lesquelles aparaissent les pieces
fenetre.blit(fond, (0,0))
resetrect=pygame.Rect(1140,617,150,150)
piecerect1=pygame.Rect(900,150,100,100)
piecerect2=pygame.Rect(900,300,100,100)
piecerect3=pygame.Rect(900,450,100,100)
piecerect4=pygame.Rect(1020,150,100,100)
piecerect5=pygame.Rect(1020,300,100,100)
piecerect6=pygame.Rect(1020,450,100,100)
piecerect7=pygame.Rect(1020,10,100,100)
piecerect8=pygame.Rect(870,10,100,100)
piecerect9=pygame.Rect(759,15,95,99)
piecerect10=pygame.Rect(765,150,95,99)
piecerect11=pygame.Rect(765,275,95,99)
piecerect12=pygame.Rect(765,300,95,99)

cord_piece=[piecerect1,piecerect2,piecerect3,piecerect4,piecerect5,piecerect6,piecerect7,piecerect8,piecerect9,piecerect10,piecerect11,piecerect12]

lepoucerect=pygame.Rect(950,575,138,157)


# affichage des boutons
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
fenetre.blit(piece12,piecerect12)

fenetre.blit(lepouce,lepoucerect)


# definition des rectangles des pieces
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

cord_case = [case0, case1, case2,case3,case4,case5,case6,case7,case8,case9,case10,case11,case12,case13,case14,case15]

c=[0 for i in range (16)]


#création liste des cases
case=[["OOOO" for i in range(4) ] for i in range(4) ]




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
                    pos=pygame.mouse.get_pos()
                    #positions pieces


                    for i in range(12):
                        if cord_piece[i].collidepoint(pos) and p[i]==2:
                            p[i]=1
                            print ("piece cliquée" ,i)

                        for r in range (16):

                            if cord_case[r].collidepoint(pos) and p[i]==1 and c[r]==0 :
                                cord_piece[i]=cord_case[r]
                                p[i]=0
                                c[r]=1
                                case[r//4][r%4]=piecev[i]

                                print ("case",r)




                    #tests
                    if  lepoucerect.collidepoint(pos):

                       test(case)
                       print("test")




                    #bouton reset
                    if resetrect.collidepoint(pos):
                        print("restart")
                        cord_piece[0]=pygame.Rect(900,150,120,150)
                        cord_piece[1]=pygame.Rect(900,300,120,150)
                        cord_piece[2]=pygame.Rect(900,450,120,150)
                        cord_piece[3]=pygame.Rect(1020,150,100,150)
                        cord_piece[4]=pygame.Rect(1020,300,100,150)
                        cord_piece[5]=pygame.Rect(1020,450,100,150)
                        cord_piece[6]=pygame.Rect(1020,10,100,100)
                        cord_piece[7]=pygame.Rect(870,10,100,100)
                        cord_piece[8]=pygame.Rect(759,15,95,120)
                        cord_piece[9]=pygame.Rect(765,150,95,120)
                        cord_piece[10]=pygame.Rect(765,275,95,99)
                        cord_piece[11]=pygame.Rect(765,300,95,99)


                        for i in range (16):
                            p[i]=2
                            c[i]=0

                        for x in range (4):
                            for y in range (4):
                                case [x][y]="OOOO"


        fenetre.blit(fond, (0,0))
        fenetre.blit(reset,resetrect)
        for x in range (12):
            fenetre.blit(piece[x],cord_piece[x])
        fenetre.blit(lepouce,lepoucerect)

        pygame.display.flip()


finally:
    pygame.quit()
    exit()