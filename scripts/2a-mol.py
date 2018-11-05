#!/usr/bin/python3.6
#EXERCICE : 2a-mol.py
#DESCRIPTION : Jeu du plus ou moins avec fichier externe "démon"
#AUTEUR : Galmot
#DATE : 04/11/18

import random
import signal
import sys
from time import sleep

#generation du nombre aléatoire
nombrealeatoire=random.randint(0, 100)

#fichier communiquant avec 
file = open('deamonjeu.txt', 'w').write("Jeu du plus ou moins")
#fonction quitter
def quitter():
	print(' \nleaving ...')
	ctrl()

#fonction quitter
def solution():
	print("bravo vous avez trouvé le nombre", nombrealeatoire)

#l'uttilisateur coupe le script avec CTRL + C 
def ctrl(sig, frame):
	print("\nvous avez quittez la partie avec ctrl+c")
	sys.exit(0)
	
#Intercept le Ctrl+c
signal.signal(signal.SIGINT, ctrl)

#règle du jeu
print("Choisir un nombre entre 0 et 100, (q pour quitter)")
while 1:
    #Variable int de l'utilisateur
    nombreuser = open('deamonjeu.txt', 'rt').readline(3)
    #si l'user entre q, alors il quitte la partie
    userq = open('deamonjeu.txt', 'rt').readline(1)
    if userq == "q":
		#on appelle la fonction quitter
        quitter()
    try:
        #transforme l'entrée de l'utilisateur en int
        uservaleur = int(nombreuser)
        #Si nombre inconnu est plus grand écrit plus grand dans le fichier
        if uservaleur < nombrealeatoire:
            file = open('deamonjeu.txt', 'w').write("c'est plus")
        #Si nombre inconnu est plus petit écrit plus petit dans le fichier
        elif uservaleur > nombrealeatoire:
            file = open('deamonjeu.txt', 'w').write("c'est moins")
        #Si nombre inconnu est trouvé affiche le nombre (nombrealeatoire)
        elif uservaleur == randomInt:
            solution()
            sys.exit(0)
        #Si user entre autre que int l'ignore
    except ValueError:
            sleep(1)