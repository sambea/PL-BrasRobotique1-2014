# script pion.py
# -*- coding: iso-8859-1 -*-

'''
Created on April 2014

@author: El Hadji Malick FALL && Adji Ndeye Ndate SAMBE

'''

from Tkinter import *
import tkMessageBox
from xml.dom import minidom
import math



def Destination():

    #recuperation des coordonnees du marqueur
    #un marqueur est un carre forme de 4 points p1, p2, p3 et p4

    #on parse le fichier xml recu par le server

    xmldoc = minidom.parse('fichierSimulation.xml')
    #on recupere les  coordonnes de p1 : (coin inferieur gauche)
    p1 = xmldoc.getElementsByTagName('p1')
    
    #on recupere les  coordonnes de p2 : (coin superieur gauche)
    p2 = xmldoc.getElementsByTagName('p2')

    #on recupere les  coordonnes de p3 : (coin superieur droit) 
    p3 = xmldoc.getElementsByTagName('p3') 

    #on recupere les  coordonnes de p4 : (coin inferieur droit)
    p4 = xmldoc.getElementsByTagName('p4')  

    #on recupere les  coordonnes de x du point p1
    x1 = p1[0].attributes['x'].value

    #on recupere les coordonnes de y du point p1
    y1 = p1[0].attributes['y'].value

    #on recupere les  coordonnes de x du point p3
    x3 = p3[0].attributes['x'].value

    #on recupere les  coordonnes de y du point p1
    y3 = p3[0].attributes['y'].value

    #fin de la recuperation...............

    #on calcule le centre du carre qui representera le marqueur

    global xprim,yprim

    """ Dessine un cercle de centre (x,y) et de rayon r=10 """
  
    xprim = (float(x1) + float(x3))/2
   
    yprim = (float(y1) + float(y3)) /2
    
    #on definit le rayon du cercle. le marqueur sera represente par un cercle
    rprim = 10.
    Canevas.create_oval(xprim-rprim, yprim-rprim, xprim+rprim, yprim+rprim, outline='green', fill='green')


def Clavier(event):
    """ Gestion de l'événement Appui sur une touche du clavier """
    global PosX,PosY
    touche = event.keysym
    print(touche)

    # déplacement vers le haut
    if touche == 'Up':
        PosY -= 20.

    # déplacement vers le bas
    if touche == 'Down':
        PosY += 20.

    # déplacement vers la droite
    if touche == 'Right':
        PosX += 20.

    # déplacement vers la gauche
    if touche == 'Left':
        PosX -= 20.

    # on dessine le pion à sa nouvelle position
    Canevas.coords(Pion,PosX -10., PosY -10., PosX +10., PosY +10.)
    
    #on calcule la distance qui separe le bras du marqueur
    n1 = (xprim -PosX) * (xprim -PosX)
    n2 = (yprim -PosY) * (yprim -PosY)
    distance = math.sqrt(n1 + n2)
  

    if (distance < 16):
	tkMessageBox.showinfo(title="Notification", message="Marker reached!")
    


# Création de la fenêtre principale
Mafenetre = Tk()
Mafenetre.title('MakerDetect')

#hauteur et largeur de la fenetre
Largeur = 480
Hauteur = 320

# position initiale du pion
PosX = 10
PosY = 10


# Création d'un widget Canvas (zone graphique)
Canevas = Canvas(Mafenetre, width = Largeur, height =Hauteur, bg ='white')
Pion = Canevas.create_oval(PosX-10,PosY-10,PosX+10,PosY+10,width=2,outline='blue',fill='blue')
Canevas.focus_set()
Canevas.bind('<Key>',Clavier)
Canevas.pack(padx =5, pady =5)


# Création du widget Button (bouton DestinationMarker)
BoutonGo = Button(Mafenetre, text ='GetMarkerPosition',command = Destination)
BoutonGo.pack(side = LEFT, padx = 10, pady = 10)

# Création du widget Button (bouton Quitter)
Button(Mafenetre, text ='Quitter', command = Mafenetre.destroy).pack(side=LEFT,padx=5,pady=5)



Mafenetre.mainloop()
