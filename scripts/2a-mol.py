#!/usr/bin/python3.6
#EXERCICE : 2a-mol.py
#DESCRIPTION : Jeu du plus ou moins avec fichier externe "démon"
#AUTEUR : Galmot
#DATE : 04/11/18

import random
import signal
import sys
from time import sleep

#Intercept le Ctrl+c
signal.signal(signal.SIGINT, ctrl)

#generation du nombre aléatoire
nombrealeatoire=random.randint(0, 100)

#fichier communiquant avec 
file = open('deamonjeu.txt', 'w').write("")
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

#règle du jeu
print("Choisir un nombre entre 0 et 100, (q pour quitter)")
while True:
	#l'user entre un nombre
	nombreuser = open('deamonjeu.txt', 'rt').readline(3)
	nombreuser = int(nombreuser)
	#si l'user entre q, alors il quitte la partie
	nombreuser = open('deamonjeu.txt', 'rt').readline(1)
	if nombreuser== "q":
		#on appelle la fonction quitter
		quitter()
		break
	#si le nombre choisis est égal au nombre aléatoire alors:
	elif nombreuser == nombrealeatoire:
		#l'user gagne
		solution()
		break
	#tant que le nombre n'a pas été trouvé, la boucle continue
	else:
		if nombreuser > nombrealeatoire:
			file = open('deamonjeu.txt', 'w').write("c'est moins")
		else:
			file = open('deamonjeu.txt', 'w').write("c'est plus")
