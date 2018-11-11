#!/usr/bin/python3.6
# Nom: 2b-mol
# Description: Jeu du plus ou moins dans un fichier
# Auteur: Galmot
# Date: 05/11/2018 - 07/11/2018

# Importation des modules
from random import randint
import re
import signal

# Fonction d'au revoir + affichage de la solution
def ctrl(*args):
  global nombrerandom
  nombreadd("Au revoir!\nLa solution était: " + str(nombrerandom))
  exit(0)

# Gestion signals
signal.signal(signal.SIGINT, ctrl)
signal.signal(signal.SIGTERM, ctrl)

# Ecrire dans un fichier
def nombreadd(message):
  fichier = open("deamonjeu.txt", "w")
  fichier.write(message)
  fichier.close()

# Lecture du fichier
def readfile():
  fichier = open("deamonjeu.txt", "r")
  message = fichier.read()
  fichier.close()
  return message
nombrerandom = randint(0,100)
fin = False

# Jeu
nombreadd("Choisir un nombre entre 0 et 100\n")
while fin is False:
  nb = readfile()

  # On vérifie l'entrée utilisateur (int uniquement)
  if re.match(r"^[0-9]+$", nb):
    nb = int(nb)
    if nb > 100:
      continue
    
    if nb < nombrerandom:
      nombread("C'est plus")
    elif nb > nombrerandom:
      nombread("C'est moins")
    else:
      nombread("Bravo tu as trouvé")
      fin = True
  
  elif nb == 'q' or nb == 'q\n':
    ctrl()  

  else:
    continue
