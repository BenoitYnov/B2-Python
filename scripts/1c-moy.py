#!/usr/bin/python3.6
#EXERCICE : 1c-moy
#DATE : 15/10/18
#AUTEURS : Galmot
#intialisation du tableau
tableau = []
i = 0
moy = 0

#boucle
while 1 :
	#fonction
	def reverse_numeric(x, y):
        	return y - x
	#saisie utilisateur
	prenom = input("Saisissez un prénom : ")
	note = int(input("Saisissez une note : "))
	noteuser = "[{}, {}.]".format(prenom, note)

	try:
		#convertit valeur en entier
		num = int(note)
		print(noteuser)
	except ValueError:
		print("Erreur : La note saisie doit être un nombre.")
		break

	tableau.insert(i, noteuser)
	moy += int(note)
	i += 1

	print("Continuer ou quitter la saisie ?[c/q]")
	keypress = input()
	
	#condition quitter et afficher le résultat
	if keypress == "q":
		print("Saisie quittée.")
		moy = moy/i
		print(sorted(note))
		print("La moyenne totale est de {}/20.".format(moy))
		break

