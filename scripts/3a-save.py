#!/usr/bin/python3.6
# Nom: 3a-save.py
# Description: Sauvegarde d'archive /*/ réalisé à l'aide de la docs.python
# Auteur: Galmot
# Date: 06/11/2018 - 11/11/2018

import shutil
import gzip
import os
import sys
import signal

#Variables, chemins
path_directory = os.path.expanduser('~/B2-Python/scripts')
path_data = os.path.expanduser('~/data/')
path_save = os.path.expanduser('~/B2-Python_save')

#Fonction :
#création de l'archive
def creeArchive(path, archive):
    if os.access(path, os.R_OK):
        shutil.make_archive(archive, 'gztar', path)

#Supprime l'archive existante
def suppArchive():
    if os.path.exists(archive + '.tar.gz'):
        os.remove(archive + '.tar.gz')

#quitter le programme
def quitter(sig, frame):
    suppArchive()
    sys.exit(0)

signal.signal(signal.SIGINT, quitter)

#Script
creeArchive(path_directory, path_save)
path_save += '.tar.gz'

if os.path.isfile(path_data + '/B2-Python_save.tar.gz'):
        archive = gzip.open(path_save)
        archive_exist = gzip.open(path_data+'/B2-Python_save.tar.gz')
        #archive déjà existante
        if archive.read() == archive_exist.read():
                sys.stdout.write('Le fichier existe déjà')
                os.remove(path_save)
        #archive sauvegarder
        else:
                sys.stdout.write('Sauvegarde réussi')
                os.remove(path_data+'/B2-Python_save.tar.gz')
                shutil.move(path_save, path_data)
else:
        shutil.move(path_save, path_data)
