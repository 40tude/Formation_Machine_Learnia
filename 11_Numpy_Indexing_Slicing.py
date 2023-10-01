# py -m venv .\PrjVEnv          				            # créé, entre autres, un sous repertoire PrjVEnv                     
# code .                                            # Lance Visual Studio Code
# choisir son debugueur python                      # CTRL + SHIFT + P puis Python Select Interpreter 
                                                    # Choisir l'interpreteur avec l'environnment virtuel
                                                    # Python 3.10.7 ('PrjVEnv':venv)./PrjVEnv/Scripts/python.exe
                                                    # Dans la console dans VS Code on voit (PrjVEnv) en début de prompt 
# Depuis la console de VS Code
# python -m pip install numpy scipy            # install les lib



import numpy as np
from scipy import misc
import matplotlib.pyplot as plt



def Exercice():
  face = misc.face(gray=True)
  #plt.imshow(face, cmap=plt.cm.gray)
  #plt.show()

  Zoom = 2 
  assert Zoom>=1, ("Zoom doit être >= à 1") 

  # face.shape[0] = nb pixel en y
  print("Dimensions image : ", face.shape)
  
  # si on veut un zoom de 4 la longueur c'est (1/zoom * long)
  # le point de départ c'est 1/2 de la long - 1/2 de (1/zoom * long)
  # Après on met long en facteur etc. Et on toruve Coef
  # Par symétrie, la fin c'est la longueur totale - l'indice du pixel de départ 
  Coef = (Zoom-1)/(2*Zoom)
  BeginVertical = int(face.shape[0]*Coef)
  EndVertical = int(face.shape[0] - BeginVertical)
  
  BeginHorizontal = int(face.shape[1]*Coef)
  EndHorizontal = int(face.shape[1] - BeginHorizontal)
  
  face2 = face[BeginVertical:EndVertical, BeginHorizontal:EndHorizontal]
  
  TriggerDark = 100
  TriggerLight = 255-TriggerDark
  face2[face2<TriggerDark] = 0x00
  face2[face2>TriggerLight] = 0xFF

  plt.imshow(face2, cmap=plt.cm.gray)
  plt.show()





def main():
  A = np.array([i for i in range(100, 109)]).reshape(3,3)
  print("Matrice initiale : \n", A)
  print("Indexing : ", A[0, 0])                   # ligne, colonne 
  print("Indexing : ", A[1, 2])

  # ----------------------------------------------
  # slicing A[debut:fin:pas, debut:fin:pas]
  print("Colonne 0          : ", A[:, 0])
  print("Colonne 2          : ", A[:, 2])
  print("Ligne 1            : ", A[1, :])
  print("Ligne 2            : ", A[2])                     # on est row-ligne major comme en C++
  print("2 premières lignes : ", A[:2])                    # Afiche les 2 premières lignes (indices 0 et 1)
  
  # ----------------------------------------------
  # subseting
  B = A[0:2, 0:2]                                 # /!\ de 0 à 2 exclu    
  print("Matrice B : \n", B)

  A[0:2, 0:2] = 100                               # Initialise une sous-partie de la matrice
  print("Matrice A : \n", A)


  C = np.array([i for i in range(25)]).reshape(5,5)
  print("Matrice C initiale : \n", C)
  # copier les 2 dernières colonnes
  # D = C[:, 1:] # on veut pas à partir de la colonne 1 mais les 2 dernières colonnes
  D = C[:,-2:]
  print("2 dernières colonne de C : \n", D)


  E = np.zeros((4,4))             # faut passer un tuple
  print("Matrice E : \n", E)
  # remplir au milieu avec 4 1
  E[1:3, 1:3] = 1                 # de [1, 3[
  print("Matrice E modifiée: \n", E)


  E = np.zeros((5,5))             # faut passer un tuple
  print("Matrice E : \n", E)
  # faire un damier de 1 en utilisant le pas du slicing
  E[::2, ::2] = 1                 
  print("Matrice E modifiée: \n", E)


  # ----------------------------------------------
  # boolean indexing (utile en ML et DS)
  A = np.random.randint(0, 100, [5,5])
  print("Matrice A : \n", A)
  print ("Masque A < 50 : \n", A < 50)            # A<5 retourne un tableau 5x5, un masque
  # Mettre à 100 tous les elements inf à 5
  mask = A<25
  A[mask] = 100                 # A[A < 25] = 100
  print("Matrice A : \n", A)

  A = np.random.randint(0, 10, [5,5])
  print("Matrice A : \n", A)
  A[(A<5) & (A>2)] = 100            # pas oublier les ( et )
  print("Matrice A : \n", A)

  # filtrer les données
  print("Filtrer les données\n")
  A = np.random.randint(0,10, [5,5])
  print("Matrice A : \n", A)
  print("Vecteur des valeurs de A inf à 5 : \n", A[A<5])   # c'est plus une matrice mais un vecteur!
  print("Shape de A[A<5] : ", A[A<5].shape)

  A = np.random.randint(0,10, [5,5])
  print("Matrice A : \n", A)
  B = np.random.randn(5, 5)
  #print(f"Matrice B : {B:.2f}\n", )
  print(f"Matrice B :\n {B}", )
  C = B[A<2]                                # on applique à B le filtre
  print(f"Vecteur C qui contient les valeurs B filtrées selon le boolean indexing de A: {C}\n")
  

if __name__ == '__main__':
   main()
   #Exercice()
   