# py -m venv .\PrjVEnv          				            # créé, entre autres, un sous repertoire PrjVEnv                     
# code .                                            # Lance Visual Studio Code
# choisir son debugueur python                      # CTRL + SHIFT + P puis Python Select Interpreter 
                                                    # Choisir l'interpreteur avec l'environnment virtuel
                                                    # Python 3.10.7 ('PrjVEnv':venv)./PrjVEnv/Scripts/python.exe
                                                    # Dans la console dans VS Code on voit (PrjVEnv) en début de prompt 
# Depuis la console de VS Code
# python -m pip install numpy scipy                 # install les lib


# un module c'est 1 fichier avec des définitions de fonctions
# un package c'est un ensemble de modules
# Exemple : matplotlib

import matplotlib.pyplot as plt    # importe le module pyplot du package matplotlib sous l'abréviation plt                                                                                                                                                            
import numpy as np

import math
import random
import statistics
import os
import glob


def Exercice():
  dico = {}

  filenames = glob.glob("*.txt")
  for f in filenames:
    with open(f, "r") as f:
      dico[f.name] = f.read().splitlines()
  print(dico)






def SaveAsSVG():
  x = np.arange(0, 2*np.pi, 0.01)
  y = np.sin(x)
  plt.plot(y)
  plt.show()
  plt.savefig("test.svg", format="svg")


def main():
  
  print(math.pi, type(math.pi))
  print(np.pi, type(np.pi))

  # statistics.mean etc.
  print (statistics.mean((1,2,3)))                        # on passe un iterable : tuple, liste...
  print (statistics.variance([i**2 for i in range(10)]))

  # random
  # random.seed(0)                                 # 0 définit la série
  print("J'ai choisi", random.choice((1,2,3)))
  print("J'ai choisi", random.choice(("riri", "fifi", "loulou")))
  
  print ("random : ", random.random())                         # nb aléatoire float entre 0 et 1
  print ("randint : ", random.randint(100, 200))               # nb aléatoire int entre 100 et 200 (inclus)
  print ("randrange : ", random.randrange(180, 200))           # entre [180, 200[
  print ("sample :", random.sample(range(100), 15))            # 15 elements de la liste qui en contient 100 de 0 à 99  
  print ("sample :", random.sample(range(100), random.randrange(20))) # liste de 0 à 19 éléments dont les valeurs sont entre 0 et 99
  
  tmp = [1,2,3]
  random.shuffle(tmp)
  print ("Suffle : ", tmp) # on peut pas passer un tuple

  # OS
  print(os.getcwd())

  # glob
  print(glob.glob("*.*"))           # génère une liste avec tous les noms des fichiers du répertoire courant qui correspondent au masque 
                                    # * retroune répertoires et fichiers. *.* retourne que les fichiers

  filenames = glob.glob("*.txt")
  for f in filenames:
    with open(f, "r") as f:
      print(f.read())
      # pas besoin de fermer le fichier





if __name__ == '__main__':
  main()
  #  SaveAsSVG()
  # Exercice()