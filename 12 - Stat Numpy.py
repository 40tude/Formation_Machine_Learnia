# py -m venv .\PrjVEnv          				            # créé, entre autres, un sous repertoire PrjVEnv                     
# code .                                            # Lance Visual Studio Code
# choisir son debugueur python                      # CTRL + SHIFT + P puis Python Select Interpreter 
                                                    # Choisir l'interpreteur avec l'environnment virtuel
                                                    # Python 3.10.7 ('PrjVEnv':venv)./PrjVEnv/Scripts/python.exe
                                                    # Dans la console dans VS Code on voit (PrjVEnv) en début de prompt 
# Depuis la console de VS Code
# python -m pip install numpy matplotlib            # install les lib


import numpy as np
import os

# -----------------------------------------------------------------------------
# Normalisation par colonne ((A-MoyCol)/SigmaCol)
def Exercice():
  np.random.seed(0)
  A = np.random.randint(0, 100, [10, 5])
  print(A, "\n\n")
  
  N = np.zeros(shape=(10, 5), dtype=float)
  v_Moy = A.mean(axis=0)                        # une matrice ligne
  v_Std = A.std(axis=0)                         # une matrice ligne
  for i in range(A.shape[1]):                   # Faut éviter les boucles for à tout prix!
    for j in range(A.shape[0]):
      N[j,i] = (A[j,i]-v_Moy[i])/v_Std[i]
  print(N)
  print("\nMoyenne par colonne vaut 0 et ecart type vaut 1")
  print("Les moyennes des colonnes : ", N.mean(axis=0))
  print("Ecart type de colonnes    : ", N.std(axis=0))
  print()
  print()


  




# -----------------------------------------------------------------------------
# Normalisation par colonne ((A-MoyCol)/SigmaCol)
def Correction():
  np.random.seed(0)
  A = np.random.randint(0, 100, [10, 5])      # randint génère bien entre [0 et 100[
  print(A, "\n\n")

  # Attention c'est du broadcasting
  # A               = (10, 5)
  # A.mean(axis=0)  =     (5, )     Matrice ligne de 5 colonnes qui va être soustraite à chaque ligne de A
  # A.std(axis=0)   =     (5, )     Matrice ligne de 5 colonnes qui va être soustraite à chaque ligne de A  
  D = (A - A.mean(axis=0))/A.std(axis=0)
  print(D, "\n\n")





# -----------------------------------------------------------------------------
# https://numpy.org/doc/stable/reference/arrays.ndarray.html
def main():
  os.system('cls')

  # -----------------------------------------------------------------------------
  np.random.seed(0)
  A = np.random.randint(0, 99, [2, 3])   # 2 li, 3 col
  print(A, "\n")
  print("Somme elements de A : ", A.sum())
  print("Sommes elements de A suivant axe 0 : ", A.sum(axis=0))  # Somme des colonnes. Retourne un vecteur avec A.shape[1] elements
  print("Sommes cumulées des elements de A : ", A.cumsum())       # retourne un vecteur A.size fait la somme en row major (ligne après ligne)
  print("Sommes cumulées selon les colonnes de A : \n", A.cumsum(axis=1)) 
  print("Position des minimums dans les colonnes de A : \n", A.argmin(axis=0)) 

  B = np.random.randint(0, 99, [2, 3])
  print("\n\n")
  print("Tableau à deux dimensions                                                : \n", B)
  print("Tableau des indices pour trier sur chaque ligne, selon les colonnes de B : \n", B.argsort(axis=1))


  # -----------------------------------------------------------------------------
  print("\n\n")
  A = np.random.randn(5, 5)
  print("Matrice A: \n", A)
  A = np.exp(A)
  print("Exp de A : \n", A)


  A = np.random.randint(0, 99, [4, 5])
  print("\n\n")
  print("Matrice A : \n", A )
  print("Moyenne de A : ", A.mean())
  print("Moyennes dans les colonnes de A : ", A.mean(axis=0))
  
  # L0L0 L0L1 L0L2 ...
  # L1L0 L1L1 L1L2 ...
  # Matrice symétrique selon sa diag
  print("Matrice des coefs de correlation entre les lignes de A :\n ", np.corrcoef(A))
  print("Coef de correlation entre les lignes 0 et 1 de A : ", np.corrcoef(A)[0,1])


  # -----------------------------------------------------------------------------
  A = np.random.randint(0, 10, [5, 5])
  print("\n\n")
  print("Matrice A : \n", A )
  print(np.unique(A, return_counts=True)) # retroune les occurences classéess et leurs nombres d'apparations


  A = np.random.randint(0, 10, [5, 3])
  print("\n\n")
  print("Matrice A : \n", A )
  Values, Counts = np.unique(A, return_counts=True)
  print ("Les valeurs triées en valeurs croissantes                  : ", Values)
  print ("Le nb d'occurences associé                                 : ", Counts)

  B = Counts.argsort()
  print ("Les index des occurences pour les trier en ordre croissant : ", B)
  print ("Les valeurs triées par nombre d'occurence croissant        : ", Values[B])
  print ("Même chose mais en une ligne dans le code                  : ", Values[Counts.argsort()])


  for i,j in zip(Values[Counts.argsort()], Counts[Counts.argsort()]):    # zip retourne un iterator de tuples
    print(f"La valeur {i} apparaît {j} fois.")

  
  # -----------------------------------------------------------------------------
  # Nan
  A = np.random.randn(5, 5)
  A[0,2]= np.nan
  A[4,3]= np.nan
  print("\n\n")
  print("Matrice A : \n", A )
  print(f"Moyenne avec Nan : {np.nanmean(A):.2f}", )

  B = np.isnan(A) # masque booléen avec T quand y a un Nan
  NbDeNan = B.sum()
  Qualité = NbDeNan/A.size
  print("% de Nan dans la matrice               : ", Qualité)

  # On remplace les Nan par 0 et on calcule la nouvelle moyenne
  # A[B==True]=0.0
  # A[B]=0.0
  A[np.isnan(A)]=0.0
  print("\n\n")
  print("Matrice A avec Nan remplcés par 0.0 : \n", A )
  print("La nouvelle moyenne de A               :", A.mean())


  # -----------------------------------------------------------------------------
  # Algèbre linéaire
  A = np.ones((2,3))
  B = np.ones((3,2))
  print("\n\n")
  print("Transposée de A :\n", A.T)
  print("A.B : \n", A.dot(B))
  print("B.A : \n", B.dot(A))

  A = np.random.randint(0,10, [3,3])
  print("\n\n")
  print("Matrice A : \n", A )
  # déterminant
  print ("Determinant : ", np.linalg.det(A))
  # inverse
  print ("Inverse     :\n", np.linalg.inv(A))
  # valeurs propres
  print ("Valeurs et verteur propres     :\n", np.linalg.eig(A))



if __name__ == '__main__':
  main()
  # Exercice()
  # Correction()

   