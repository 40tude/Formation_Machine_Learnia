# py -m venv .\PrjVEnv          				            # créé, entre autres, un sous repertoire PrjVEnv                     
# code .                                            # Lance Visual Studio Code
# choisir son debugueur python                      # CTRL + SHIFT + P puis Python Select Interpreter 
                                                    # Choisir l'interpreteur avec l'environnment virtuel
                                                    # Python 3.10.7 ('PrjVEnv':venv)./PrjVEnv/Scripts/python.exe
                                                    # Dans la console dans VS Code on voit (PrjVEnv) en début de prompt 
# Depuis la console de VS Code
# python -m pip install numpy scipy                 # install les lib

from asyncio.windows_events import NULL
from operator import inv
import numpy as np


classeur={
  "positifs" : [],
  "négatifs" : []
}

# Range nombre dans positifs ou negatif selon son signe
def trier(classeur, n):
  if(n>=0):
    classeur["positifs"].append(n)
  else:
    classeur["négatifs"].append(n)





def main():
  # les clés sont uniques
  dico = {
    "chien" : "dog",
    "chat" : "cat",
    "oiseau" : "bird"
  }

  # En machine learning (surtout deep learning) 
  # on stocke souvent les paramètres des réseaux de neurons dans des dicos
  parameters = {
    "W1" : np.random.randn(10, 100), # retourne un tableau de 10 lignes 100 colonnes
    "b1" : np.random.randn(10, 1),
    "W2" : np.random.randn(5, 3),
    "b2" : np.random.randn(10, 1)
  }
  
  #NULL
  
  print(parameters["W2"])

  inventaire = {
    "item1" : 100,
    "item2" : 200,
    "item3" : 300,
    "item4" : 400
  }

  print(inventaire.keys())
  print (inventaire.values())

  # pas de insert ou extend car il n'y a pas d'ordre dans un dictionnaire
  inventaire["boulons"] = 42
  print(inventaire)

  # print(inventaire[]"ecrous"] # ecrous n'existe pas => erreur
  print(inventaire.get("ecrous", "Zoubida")) # pas d'erreur si ecrous n'existe pas - retourne Zoubida
  print(inventaire)                          # pas de création de la clé "écrous"

  print(inventaire.get("item3", False))

  if inventaire.get("ecrous") == None:
    print("Pas d'écrou en stock")
  else:
    print("Pas de problème")  

  liste1 = ('Riri', 'Fifi', 'Loulou')
  Inventaire2 = dict.fromkeys(liste1)
  print(Inventaire2)
  Inventaire3 = dict.fromkeys(liste1, "Zoubida")
  print(Inventaire3)

  # retire l'association clé-valeur et retourne la valeur
  stock = inventaire.pop("item2")
  print(stock)
  print(inventaire)

  # affiche les clés
  for i in inventaire:
    print(i)

  
  for k, v in inventaire.items():
    print(k, " --- ", v)
  




if __name__ == '__main__':
    main()
    # for i in range(-5,10):
    #   trier (classeur, i)

    NULL     
   