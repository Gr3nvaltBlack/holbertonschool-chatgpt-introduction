#!/usr/bin/python3
import sys

# Parcours des arguments à partir de l'index 1 pour ignorer le nom du fichier
for i in range(1, len(sys.argv)):
    print(sys.argv[i])
