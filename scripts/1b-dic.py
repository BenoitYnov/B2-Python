#!/usr/bin/python3.6
#EXERCICE : 1b-dic.py
#DESCRIPTION : Trier les noms qu'entre l'utilisateur par ordre alphabétique dans une collection
#Date : 15/10/2018
#AUTEURS : Galmot

def addDic():
		#initialisation du dictionnaire
        name_dic={}
        i=0
        while 1:
	    #l'utilisateur doit saisir un mot ou il peut quitter
            print("Entrez le nom à ajouter (q pour quitter)")
            saisie=input()
            if saisie == "q":
                    print("fin de la saisie")
                    break
            #si l'utilisateur entre un mot, le mot est ajouté au dictionnaire
            else:
                    name_dic[str(i)]=saisie
                    i=i+1
        name_dic=sorted(name_dic.values())
		#mot dictionnaire affichée dans l'ordre alphabétique
        print(name_dic)
addDic()
