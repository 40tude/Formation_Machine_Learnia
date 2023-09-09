# py -m venv .\PrjVEnv          				            # créé, entre autres, un sous repertoire PrjVEnv                     
# code .                                            # Lance Visual Studio Code
# choisir son debugueur python                      # CTRL + SHIFT + P puis Python Select Interpreter 
                                                    # Choisir l'interpreteur avec l'environnment virtuel
                                                    # Python 3.10.7 ('PrjVEnv':venv)./PrjVEnv/Scripts/python.exe
                                                    # Dans la console dans VS Code on voit (PrjVEnv) en début de prompt 
# Depuis la console de VS Code
# python -m pip install numpy scipy                 # install les lib

import random
import numpy as np

# lire le fichier Monfichier2.txt et écrire dans une liste toutes les lignes
def Exercice():
  Liste = []
  with open("MonFichier2.txt", "r") as f:
    #Liste.append(f.readlines()) # readlines pas read
    Liste.append(f.read().splitlines()) # read mais en virant les \n
  return Liste



def Exercice2():
  #Liste = [line for line in open (MonFichier2.txt, "r")]  
  Liste = [line.strip() for line in open ("MonFichier2.txt", "r")]  
  return Liste





def main():
  # ----------------------------
  x = -2
  y = abs(x)
  z = 3.14159
  z = round(z)

  # ----------------------------
  liste1=[i**2 for i in range(5)]
  print(max(liste1))
  print(min(liste1))
  print(len(liste1))

  # ----------------------------
  # all retourne true si tous les éléments sont true
  liste2 = [True, True]
  print(all(liste2))

  # any retroune true si au moins un élément est true
  liste3 = [True, False]
  print(any(liste3))

  # générer une liste de 10 valeurs T ou F 
  liste4 = [bool(random.randrange(2)) for i in range(10)]
  print (liste4)
  

  # ----------------------------
  print("Le type de x est : ", type(x))
  print("Le type des éléments de liste4 est : ", type(liste4[0]))

  # transforme en string
  x = 3
  print (str(x))

  # de string en int
  y = "42"
  x = x + int(y)
  print (x)

  # ----------------------------
  # crée un tuple à partir d'une liste
  liste5=[i**2 for i in range(5)]
  tuple5 = tuple(liste5)
  print (tuple5)

  # une liste à partir d'un tuple
  MaListe = list(tuple5)
  print (MaListe)

  dico = {
    "a" : 3,
    "b" : 5
  }
  # crée une liste à partir d'un dico
  liste6 = list(dico.keys())
  print(liste6)
  liste7 = list(dico.values())
  print(liste7)

  # ----------------------------
  # bin(), oct()...


  # ----------------------------
  # Z!!!!!!!!!! x est une string
  # input()
  # x = input("Taper un chiffre : ")
  # print (int(x)+2)
  
  # ----------------------------
  # format() et open()
  x = 3.14159
  print(format(x, ".1f"))
  print (f"La valeur de Pi est {x:.2f}.")            # 2 chiffres après la virgule
  print ("La valeur de Pi est {:.2f}.".format(x))    # même sortie
  
  parametre = {
    "W1" : np.random.randn(2,4),                # randn = normalized
    "b1" : np.zeros((2,1)),
    "W2" : np.random.randn(3,5),
    "b@" : np.zeros((2,1))
  }
  # accède aux différentes couches 1..2
  for i in range(1,3):                                 # comme en C++ le dernier est exclu. Ici on aura donc que 1 et 2
    print ("Voici ce que contient la couche ", i)
    print (parametre[f"W{i}"])


  # ----------------------------
  # open
  # https://docs.python.org/3/library/functions.html#open
  f = open("MonFichier.txt", "a")
  f.write("Hello\n")
  f.close()

  with open("MonFichier.txt", "r") as f:
    print(f.read())
    # pas besoin de f.close() !!!!!!!!!!!!!!!!

  # ----------------------------
  # Ecrire les nb de 0 à 10 au carré danns un fichier
  with open("MonFichier2.txt", "w") as f:               
    for i in range(10):
      f.write(f"{i}^2 = {i**2}\n")
  

  # ----------------------------
  MaListe = Exercice()
  print(MaListe)

  MaListe = Exercice2()
  print(MaListe)












if __name__ == '__main__':
  main()