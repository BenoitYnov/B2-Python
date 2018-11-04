#!/usr/bin/python3.6
#EXERCICE : 1a-add
#DESCRIPTION : Demander 2 nombres à l’utilisateur et afficher le résultat de l’addition des 2 nombres. + Contrôler que l’utilisateur a bien saisi deux nombres.
#DATE : 15/10/18
#AUTEURS : Galmot

def add():
	#on demande à l'utilisateur d'entrer 2 valeurs
	nombre1 = input("Saisissez un premier nombre : ") 
	nombre2 = input("Saisissez un second nombre : ")
	
	#instruction
	try:
		#on convertit les valeurs en entier
		num1 = int(nombre1) 
		num2 = int(nombre2)
		#addition des deux valeurs et on retourne le résultat à l'utilisateur
		sum = num1+num2
		print("La somme de {} et {} est égal à {}.".format(nombre1, nombre2, sum))
	#en cas d'erreur, on prévient l'utilisateur 
	except ValueError:
		print("Erreur : Un ou plusieurs nombres saisis ne sont pas des nombres.")
add()
