import sys, pygame
from pygame.locals import *
pygame.init()
#-*- coding:Utf-8 -*-


# importation de la fonction test

from fonctions_test import test
from fonctions_test import test2
from Ia2 import IA


#Ouverture de la fenÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âªtre Pygame
fenetre = pygame.display.set_mode((1600, 900))

#importation de la musique
file = 'musique/funkyraven.mp3'
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play(-1)


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
piece13 = pygame.image.load("piece/13.png").convert_alpha()
piece14 = pygame.image.load("piece/14.png").convert_alpha()
piece15 = pygame.image.load("piece/15.png").convert_alpha()
piece16 = pygame.image.load("piece/16.png").convert_alpha()

#importation des images de fin
victoire = pygame.image.load("image/victoire.jpg").convert_alpha()
perdu = pygame.image.load("image/perdu.jpg").convert_alpha()
#importation des images de menu
volume = pygame.image.load("image/volume.png").convert_alpha()
pasvolume = pygame.image.load("image/volumebarre.png").convert_alpha()
IAimage = pygame.image.load("image/IA.png").convert_alpha()
plusIA = pygame.image.load("image/IAbarre.png").convert_alpha()


#crÃ©ation de la liste piece
piece=[piece1,piece2,piece3,piece4,piece5,piece6,piece7,piece8,piece9,piece10,piece11,piece12,piece13,piece14,piece15,piece16]

#crÃ©ation des chaines de caractÃ¨res des piÃ¨ces
#R = rond ou C = carrÃ©  ; B = beige ou M = marron  ; G = grande ou P = petite  ; T = avec trou ou S = sans trou.
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
piece13v="CBGS"
piece14v="CBGT"
piece15v="CMGT"
piece16v="CMGS"
#creation de la liste de chaines de caractere des pieces
piecev=[piece1v,piece2v,piece3v,piece4v,piece5v,piece6v,piece7v,piece8v,piece9v,piece10v,piece11v,piece12v,piece13v,piece14v,piece15v,piece16v]


#creation de la liste p
p=[2 for i in range(16)]

#crÃ©ation des variables pour les joueurs
ja=1
jb=0
#creation d'une variable pour l'ia
gagnant=0
g=0


# dÃ©finition des rectangles dans lesquelles aparaissent les pieces
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
piecerect12=pygame.Rect(765,400,95,99)
piecerect13=pygame.Rect(765,525,95,99)
piecerect14=pygame.Rect(1180,10,95,99)
piecerect15=pygame.Rect(1180,150,95,99)
piecerect16=pygame.Rect(1240,330,95,99)
cselection=pygame.Rect(1340,40,150,150)


cord_piece=[piecerect1,piecerect2,piecerect3,piecerect4,piecerect5,piecerect6,piecerect7,piecerect8,piecerect9,piecerect10,piecerect11,piecerect12,piecerect13,piecerect14,piecerect15,piecerect16]

lepoucerect=pygame.Rect(950,575,138,157)
volumerect=pygame.Rect(10,800,117,100)
v=1
IAimagerect=pygame.Rect(140,800,117,100)
IAim=1


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
fenetre.blit(piece13,piecerect13)
fenetre.blit(piece14,piecerect14)
fenetre.blit(piece15,piecerect15)
fenetre.blit(piece16,piecerect16)
fenetre.blit(lepouce,lepoucerect)
fenetre.blit(lepouce,lepoucerect)
fenetre.blit(volume,volumerect)
fenetre.blit(IAimage,IAimagerect)

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


#crÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©ation liste des cases
case=[["OOOO" for i in range(4) ] for i in range(4) ]


print("test")

#RafraÃ®chissement de l'Ã©cran
pygame.display.flip()

#BOUCLE INFINIE
continuer = 1

try:
#Boucle infinie
    while continuer:
        for event in pygame.event.get():   #On parcours la liste de tous les Ã©vÃ©nements recus
            if event.type == QUIT:     #Si un de ces evenements est de type QUIT
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                #mouvement piÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¨ce 1

                if pygame.mouse.get_pressed()[0]:
                    pos=pygame.mouse.get_pos()
                    #positions pieces


                    for i in range(16):
                        if cord_piece[i].collidepoint(pos) and p[i]==2:
                            p[i]=1
                            print ("piece cliquÃ©" ,i)
                            #IA
                            cord_piece[i]=cselection
                            e=i
                            if ja==1:
                                  ja=0
                                  jb=1

                            else :
                                ja=1
                                jb=0

                        for r in range (16):

                            if cord_case[r].collidepoint(pos) and p[i]==1 and c[r]==0 :
                                cord_piece[i]=cord_case[r]
                                p[i]=0
                                c[r]=1
                                case[r//4][r%4]=piecev[i]


                                print ("case",r)

                    def restart(cord_piece,case,p,c):
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
                            cord_piece[11]=pygame.Rect(765,400,95,99)
                            cord_piece[12]=pygame.Rect(765,525,95,99)
                            cord_piece[13]=pygame.Rect(1180,10,95,99)
                            cord_piece[14]=pygame.Rect(1180,150,95,99)
                            cord_piece[15]=pygame.Rect(1240,330,95,99)

                            for i in range (16):
                                p[i]=2
                                c[i]=0

                            for x in range (4):
                                for y in range (4):
                                    case [x][y]="OOOO"


                    if volumerect.collidepoint(pos):
                        if v==1:
                            v=0
                            pygame.mixer.music.set_volume(0)
                        else :
                            v=1
                            pygame.mixer.music.set_volume(1)


                    if IAimagerect.collidepoint(pos):
                        restart(cord_piece,case,p,c)
                        if IAim==1:
                            IAim=0

                        else :
                            IAim=1


                    #tests
                    if  lepoucerect.collidepoint(pos):
                        if IAim==1:
                            IA(case,e,piecev,cord_piece,cord_case,g,p,c,cselection)



                    #bouton reset
                    if resetrect.collidepoint(pos):
                        restart(cord_piece,case,p,c)

        if test(case)!=1:
            fenetre.blit(fond, (0,0))
            fenetre.blit(reset,resetrect)
            for x in range (16):
                fenetre.blit(piece[x],cord_piece[x])
            fenetre.blit(lepouce,lepoucerect)
            fenetre.blit(IAimage,IAimagerect)
            if v==1:
                fenetre.blit(volume,volumerect)
            else:
                fenetre.blit(pasvolume,volumerect)
            if IAim==1:
                fenetre.blit(IAimage,IAimagerect)
            else:
                fenetre.blit(plusIA,IAimagerect)

        else:
            fenetre.blit(fond, (0,0))

            if ja==1:
                fenetre.blit(victoire, (0,0))
                fenetre.blit(perdu, (800,0))
            else :
                fenetre.blit(perdu, (0,0))
                fenetre.blit(victoire, (800,0))
            fenetre.blit(reset,resetrect)





        pygame.display.flip()


finally:
    pygame.quit()

