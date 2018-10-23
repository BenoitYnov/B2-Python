#!/usr/bin/python3.6
#EXERCICE : 1d-mol.py
#DESCRIPTION : Jeu du plus ou moins
#AUTEUR : Galmot
#DATE : 23/10/18

import random
import signal
import sys
from time import sleep

#fonction quitter
def quitter():
	print("vous avez quittez la partie")

#fonction quitter
def solution():
	print("bravo vous avez trouvé le nombre", nombrealeatoire)

#l'uttilisateur coupe le script avec CTRL + C 
def ctrl(sig, frame):
	print("\nvous avez quittez la partie avec ctrl+c")
	sys.exit(0)

signal.signal(signal.SIGINT, ctrl)

#generation du nombre aléatoire
nombrealeatoire=random.randint(0, 100)
#règle du jeu
print("Choisir un nombre entre 0 et 100, (q pour quitter)")
while True:
	#l'user entre un nombre
	nombreuser = input()
	#si l'user entre q, alors il quitte la partie
	if nombreuser == "q":
		#on appelle la fonction quitter
		quitter()
		break
	#si le nombre choisis est égal au nombre aléatoire alors:
	elif int(nombreuser) == nombrealeatoire:
		#l'user gagne
		solution()
		break
	#tant que le nombre n'a pas été trouvé, la boucle continue
	else:
		if int(nombreuser) > nombrealeatoire:
			print("c'est moins")
		else:
			print("c'est plus")
