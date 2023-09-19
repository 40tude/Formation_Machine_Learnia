# py -m venv .\PrjVEnv          				            # créé, entre autres, un sous repertoire PrjVEnv                     
# code .                                            # Lance Visual Studio Code
# choisir son debugueur python                      # CTRL + SHIFT + P puis Python Select Interpreter 
                                                    # Choisir l'interpreteur avec l'environnment virtuel
                                                    # Python 3.10.7 ('PrjVEnv':venv)./PrjVEnv/Scripts/python.exe
                                                    # Dans la console dans VS Code on voit (PrjVEnv) en début de prompt 
# Depuis la console de VS Code
# python -m pip install numpy matplotlib            # install les lib

import numpy as np

# -----------------------------------------------------------------------------
def main():

  # -----------------------------------------------------------------------------
  A = np.random.randint(0,100,(2,3))
  print("Matrice A: \n", A)

  B = np.ones((2,3))
  print("Matrice B: \n", B)

  C = np.ones((2,3))
  print("Matrice C: \n", C)
  
  print("Matrice A+B: \n", A+B)
  #print("Matrice A+C: \n", A+C) # Pas possible car pas les mêmes dimensions


  # -----------------------------------------------------------------------------
  # Broadcasting = Etendre les dimensions d'un tableau
  # On peut faire A+2 ou 2 est un scalaire (tableau 1x1)
  print("Matrice A+2: \n", A+2)


  print("Matrice A: \n", A)
  B = np.ones((2,1))
  print("Matrice B: \n", B)
  print (A+B)

  # Ne fonctionne pas
  # print("Matrice A: \n", A)
  # B = np.ones((3,1))
  # print("Matrice B: \n", B)
  # print (A+B)

  # REGLE : les dimensions de A et B doivent être identiques ou alors l'une des 2 est égale à 1
  # Matrice (2,3) et matrice (2,3) OK
  # Matrice (2,3) et matrice (2,2) NOK
  # Matrice (2,3) et matrice (2,1) OK (on transforme le 1 en 3. On répette à droite le motif (2,1) pour couvrir (2,3))
  # Matrice (2,3) et matrice (3,1) NOK
  # Matrice (4,1) et matrice (1,3) OK (on broadcast dans les 2 axes)

  A = np.random.randint(0,100,(4,3))
  print("Matrice A: \n", A)
  B = np.ones((1,3))
  print("Matrice B: \n", B)
  print("Matrice A+B: \n", A+B)


  A = np.random.randint(0,100,(4,1))
  print("Matrice A: \n", A)
  B = np.ones((1,3))
  print("Matrice B: \n", B)
  print("Matrice A+B: \n", A+B)

   # -----------------------------------------------------------------------------
  # Attention aux dimensions incomplètes
  print("\n\n\nDimensions incomplètes (voir B ci-dessous) : ")
  print("Python est row major, donc quand il n'y a qu'une dimmension c'est une ligne.")
  print("Donc le 2eme paramètre de shape quand on est en 2D")
  print("Faut vraiment faire l'effort de mettre les dim en face l'une de l'autre et y penser.")
  print("(4,1)")
  print("  (3,)")
  print("La matrice (4,1) va devenir une (4,3) en répétant à droite la première colonne")
  print("Ensuite on va additionner ligne à ligne")
  print()

  A = np.random.randint(0,10,(4,1))
  print("Matrice A: \n", A)
  print("Shape de A : ", A.shape)
  print()

  B = np.ones((3))
  print("Matrice B: \n", B)
  print("Shape de B : ", B.shape)

  print()
  print("Matrice A+B: \n", A+B)

  print ("\nPour éviter les broacast intempestifs, faut utiliser reshape ")
  B = np.ones((3))
  print("Matrice B (matrice ligne): \n", B)
  print("Shape de B : ", B.shape)
  
  B = B.reshape(3,1)
  print("\nNouvelle forme de la matrice B (un vecteur): \n", B)
  print("Nouvelle shape de B : ", B.shape)

  # Ne peut pas marcher
  # (1, 4)
  #    (3,)

  # A = np.random.randint(0,10,(1,4))
  # print("Matrice A: \n", A)
  # print("Shape de A : ", A.shape)
  # print()

  # B = np.ones((3))
  # print("Matrice B: \n", B)
  # print("Shape de B : ", B.shape)

  # print()
  # print("Matrice A+B: \n", A+B)



  


if __name__ == '__main__':
   main()
   # Exercice()