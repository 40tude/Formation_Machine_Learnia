# py -m venv .\PrjVEnv          				            # créé, entre autres, un sous repertoire PrjVEnv                     
# code .                                            # Lance Visual Studio Code
# choisir son debugueur python                      # CTRL + SHIFT + P puis Python Select Interpreter 
                                                    # Choisir l'interpreteur avec l'environnment virtuel
                                                    # Python 3.10.7 ('PrjVEnv':venv)./PrjVEnv/Scripts/python.exe
                                                    # Dans la console dans VS Code on voit (PrjVEnv) en début de prompt 
# Depuis la console de VS Code
# python -m pip install numpy scipy                 # install les lib

import numpy as np

def main():
  # shape retourne un tuple
  # on peut accèder avec []
  # A.shape[0] = nb de lignes    A.shape[1] = nb de colonnes 
  A = np.array([0, 1, 2, 3])     # 1D et 4 ele dans la colonnne
  print(f"Shape : {A.shape} Nb dim : {A.ndim}    Size : {A.size}")

  # On passe z puis x et y
  B = np.zeros((3, 4, 5))          # 3D 3x4x5 ele - On passe le shape sous forme de tuple
  print(B.shape)
  print(type(B.shape))
  print (B.ndim)
  print (B.size)
  print (B)

  C = np.ones((2,4))
  print(C.size)
  print(C)

  D = np.random.randn(3,4)          # n comme normalized - pas de tuple à passer
                                    # c'est np.random... et pas random
                                    # y a aussi un np.random.seed
  print(D)

  E = np.eye(4)   # matrice identité
  print(E)

  F = np.linspace(10, 20, 100)      # Une dimension. 100 points entre [10 et 20]
  print(F)
  print (F.shape)

  G = np.arange(10, 20, .7, dtype=np.float16)        # n points entre [10 et 20[ au pas de .7
  print(G)


  # --------------------------------------------------
  Tab1 = np.zeros((3,2))
  Tab2 = np.ones((3,2))
  print(Tab1)
  print(Tab2)


  Tab4 = np.vstack((Tab1, Tab2))                      # Z! on passe un tuple
  print(Tab4)
  Tab5 = np.concatenate((Tab1, Tab2), axis=0)         # axis = 0 => vertical
                                                      # Peut être celle à utiliser car on peut faire axis=2 etc.  
  print(Tab5)
  
  Tab3 = np.hstack((Tab1, Tab2))                      # Z! on passe un tuple
  print(Tab3)
  
  Tab6 = np.concatenate((Tab1, Tab2), axis=1)      
  print(Tab6)

  Tab7 = Tab6.reshape(6, 2)
  print(Tab7)

  Tab8 = Tab6.reshape(2, 6)
  print(Tab8)

  Tab9 = np.array([1,2,3])                          
  print(Tab9.shape)
  Tab9 = Tab9.reshape(3,1)                             # Z!!!!!!!!!! Important
  print(Tab9.shape)

  Tab10 = np.array([1,2,3]).reshape(3,1)
  print("Les dimensions du Tableau 10 sont : {}".format(Tab10.shape))

  Tab10 = Tab10.squeeze()   # Enlève la dernière dimmension.(3,) au lieu de (3,1) 
                            # Utile pour les graphiques etc.
  print(Tab10.shape)
  

  Tab11 = np.array([1,2,3,4,5,6,7,8,9,10])
  print(Tab11)

  Tab12 = Tab11.reshape(5,2)  
  print(Tab12)
  Tab11 = Tab11.reshape(5,2)  
  print(Tab11)
  

  Tab13 = Tab11.ravel() # transforme en tableau 1D. Utile pour le images en entrée de réseau de neurones
  print(Tab13)
  
  Tab11 = Tab11.ravel()
  print(Tab11)
  


def initialisation(m,n):
  X = np.random.randn(m, n+1)
  print(X)
  X[:,-1:] = 1
  print(X)
  return X



if __name__ == '__main__':
  main()
  print(initialisation(3,4))