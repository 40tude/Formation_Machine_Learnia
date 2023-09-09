# py -m venv .\PrjVEnv          				            # créé, entre autres, un sous repertoire PrjVEnv                     
# code .                                            # Lance Visual Studio Code
# choisir son debugueur python                      # CTRL + SHIFT + P puis Python Select Interpreter 
                                                    # Choisir l'interpreteur avec l'environnment virtuel
                                                    # Python 3.10.7 ('PrjVEnv':venv)./PrjVEnv/Scripts/python.exe
                                                    # Dans la console dans VS Code on voit (PrjVEnv) en début de prompt 
# Depuis la console de VS Code
# python -m pip install numpy matplotlib sklearn    # install les lib

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from mpl_toolkits.mplot3d import Axes3D
from scipy import misc
from matplotlib import cm # voir exemple ContourPlot

# -----------------------------------------------------------------------------
# Scatter
def Scatter_Demo():
  Iris = load_iris()
  x = Iris.data
  y = Iris.target
  names = list(Iris.target_names)

  print(f"x contient {x.shape[0]} exemples et {x.shape[1]} variables")
  print(f"Il y a {np.unique(y).size} classes")

  Figure = plt.figure()
  Graphe = Figure.add_subplot(111)
  Graphe.set_xlabel("longeur sépal")
  Graphe.set_ylabel("largeur sépal")
  # graphe.scatter(x[:, 0], x[:, 1])
  # graphe.scatter(x[:, 0], x[:, 1], c=y)                               # ajoute la couleur en fonction de y qui vaut O, 1 ou 2
  # graphe.scatter(x[:, 0], x[:, 1], c=y, alpha=0.5)                    # ajoute transparence
  Graphe.scatter(x[:, 0], x[:, 1], c=y, alpha=0.5, s=x[:,2]*100)        # ajoute la taille en fonction du 3eme parametre
  plt.show()


# -----------------------------------------------------------------------------
# 3D
def ThreeD_Demo():
  Iris = load_iris()
  x = Iris.data
  y = Iris.target

  Figure = plt.figure()
  Graphe3D = Figure.add_subplot(111, projection='3d')
  Graphe3D.scatter(x[:, 0], x[:, 1], x[:,2], c=y, alpha=0.5)
  Graphe3D.set_xlabel("longeur sépal")
  Graphe3D.set_ylabel("largeur sépal")
  Graphe3D.set_zlabel("longeur pétal")
  plt.show()

# -----------------------------------------------------------------------------
# 3D
def ThreeD_Demo2():
  
  f=lambda x, y : np.sin(x) + np.sin(x+y) # générateur de fonction anonyme
  x=np.linspace(0, 5, 10)  # vecteur de 20 valeurs
  y=np.linspace(0, 5, 10)
  print(x)
  print(y)
  
  # meshgrid returns coordinate matrices from coordinate vectors.
  # la matrice x contient : 
  # 0.0 0.1 0.2... 10
  # 0.0 0.1 0.2... 10
  # 0.0 0.1 0.2... 10
  # ...
  # 0.0 0.1 0.2... 10

  # la matrice y contient : 
  # 0.0 0.0 0.0... 0.0
  # 0.1 0.1 0.1... 0.1
  # 0.2 0.2 0.2... 0.2
  # ...
  # 10  10  10 ... 10
  
  x,y = np.meshgrid(x, y)       
  print("\n Matrice x:\n", x)                      # matrice de 400 valeurs???
  print("\n Matrice y:\n", y)
  z = f(x,y)

  Figure = plt.figure()
  Graphe3D = Figure.add_subplot(111, projection='3d')
  Graphe3D.plot_surface(x, y, z, cmap="plasma")   # Couleur 3D voir https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html
  plt.show()


# -----------------------------------------------------------------------------
def Histogramme():
  
  Iris = load_iris()
  x = Iris.data
  y = Iris.target
  names = list(Iris.target_names)

  Figure = plt.figure()
  Graphe = Figure.add_subplot(121) # nrows ncols index
  # The subplot will take the index position on a grid with nrows rows and ncols columns. 
  # index starts at 1 in the upper left corner and increases to the right
  Graphe.hist(x[:,0])
  Graphe.hist(x[:,0], bins=20)

  Graphe = Figure.add_subplot(122)
  Graphe.hist(x[:,0])
  Graphe.hist(x[:,1])

  plt.show()


# -----------------------------------------------------------------------------
def Histogramme2D():
  
  Iris = load_iris()
  x = Iris.data
  y = Iris.target
  names = list(Iris.target_names)

  Figure = plt.figure()
  Graphe = Figure.add_subplot(111) # nrows ncols index
  Graphe.hist2d(x[:,0], x[:,1])
  Graphe.set_xlabel("Longeur sépal")
  Graphe.set_ylabel("Largeur sépal")
  #Figure.colorbar() ???????????????????????????????????????
  plt.show()


# -----------------------------------------------------------------------------
def HistoImg():
  
  face = misc.face(gray=True)
  plt.imshow(face, cmap="gray")


  Figure = plt.figure()
  Graphe = Figure.add_subplot(111) # nrows ncols index
  Graphe.hist(face.ravel(), bins=255)
  plt.show()  



# -----------------------------------------------------------------------------
def ContourPlot():
  
  f=lambda x, y : np.sin(x) + np.sin(x+y) # générateur de fonction anonyme
  x=np.linspace(0, 5, 100)  # vecteur de 20 valeurs
  y=np.linspace(0, 5, 100)
  x,y = np.meshgrid(x, y)       
  z = f(x,y)

  Figure = plt.figure(figsize=(5, 5)) # Make sure the figure is a square. /!\Inches
  Graphe = Figure.add_subplot(111) # nrows ncols index
  #Graphe.contour(x, y, z)
  #Graphe.contour(x, y, z, 20)
  #Graphe.contour(x, y, z, 20, colors='black')    # Attention au 's' à colors
  #Graphe.contourf(x, y, z, 20, cmap="RdGy")
  # Graphe.contourf(x, y, z, 10, cmap=cm.jet)
  ContourSet = Graphe.contourf(x, y, z, 10, cmap=cm.jet)
  Graphe.clabel(ContourSet, inline=1, fontsize=8, colors="black")
  plt.show()    


  
# -----------------------------------------------------------------------------
def DemoImage():
  
  # face = misc.face()
  # plt.imshow(face)
  # plt.show()
  
  # face = misc.face(gray=True)
  # plt.imshow(face, cmap="gray")
  # plt.show()

  # face est juste un tableau de pixels
  # On affiche la matrice de correlaction entre les colonnes (c'est pour ça qu'on prend la transposée)
  Iris = load_iris()
  x = Iris.data
  
  #plt.imshow(np.corrcoef(x.T))
  #plt.imshow(np.corrcoef(x.T), cmap="Blues")
  plt.imshow(np.corrcoef(x.T), cmap=cm.jet)
  plt.colorbar()
  plt.show()






  f=lambda x, y : np.sin(x) + np.sin(x+y) # générateur de fonction anonyme
  x=np.linspace(0, 5, 100)  # vecteur de 20 valeurs
  y=np.linspace(0, 5, 100)
  x,y = np.meshgrid(x, y)       
  z = f(x,y)
  plt.imshow(z, cmap=cm.jet)
  plt.show()


# -----------------------------------------------------------------------------
# afficher sur la même figure, les différentes variables
def Exercice():
  Iris = load_iris()
  x = Iris.data
  y = Iris.target

  n = x.shape[1]
  Figure = plt.figure(figsize=(12, 7.4))
  for i in range (n):
    Graphe = Figure.add_subplot(n//2, n//2, i+1)
    Graphe.scatter(x[:, 0], x[:, i], c=y)
    Graphe.set_xlabel("0")
    Graphe.set_ylabel(i)
  plt.show()  

  
  
  


# -----------------------------------------------------------------------------
def main():
  #Scatter_Demo()
  ThreeD_Demo()
  ThreeD_Demo2()
  #Histogramme()
  #Histogramme2D()
  #HistoImg()
  #ContourPlot()
  #DemoImage()
  #Exercice()

if __name__ == '__main__':
  main()