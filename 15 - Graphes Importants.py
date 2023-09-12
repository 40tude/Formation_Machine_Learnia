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
# from mpl_toolkits.mplot3d import Axes3D # plus nécessaire depuis matplotlib 3.2
from scipy import misc
from matplotlib import cm # voir exemple ContourPlot

# -----------------------------------------------------------------------------
# Scatter
def Scatter_Demo():
  Iris = load_iris()
  x = Iris.data                             # contient les 4 paramètres long-larg sepal long-larg petal
  y = Iris.target                           # contient les classes 0 1 ou 2
  names = list(Iris.target_names)

  print(f"x contient {x.shape[0]} exemples et {x.shape[1]} variables")
  print(f"Il y a {np.unique(y).size} classes")

  # Figure = plt.figure()
  # ax = Figure.add_subplot(111)
  # ax = Figure.add_subplot()
  fig, ax = plt.subplots()
  ax.set_xlabel("longeur sépal")
  ax.set_ylabel("largeur sépal")
  # ax.scatter(x[:, 0], x[:, 1])
  # ax.scatter(x[:, 0], x[:, 1], c=y)                               # ajoute la couleur en fonction de y qui vaut O, 1 ou 2
  # ax.scatter(x[:, 0], x[:, 1], c=y, alpha=0.5)                    # ajoute transparence
  ax.scatter(x[:, 0], x[:, 1], c=y, alpha=0.5, s=x[:,2]*100)        # ajoute la taille en fonction du 3eme parametre
  # plt.show()


# -----------------------------------------------------------------------------
# 3D
def ThreeD_Demo0():
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
def ThreeD_Demo1():
  Iris = load_iris()
  x = Iris.data
  y = Iris.target

  fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
  ax.scatter(x[:, 0], x[:, 1], x[:,2], c=y, alpha=0.5)
  ax.set_xlabel("longeur sépal")
  ax.set_ylabel("largeur sépal")
  ax.set_zlabel("longeur pétal")
  plt.show()



# -----------------------------------------------------------------------------
# 3D
def ThreeD_Demo2():
  
  f=lambda x, y : np.sin(x) + np.sin(x+y) # générateur de fonction anonyme
  x=np.linspace(0, 5, 10)  # vecteur de 10 valeurs
  y=np.linspace(0, 5, 10)

  # 0.0 0.55 1.11 ... 5
  print(f"x : {x}")
  print(f"y : {y}")
  
  # meshgrid returns coordinate matrices from coordinate vectors.
  # x est un vecteur ligne   qu'on étend en bas
  # y est un vecteur colonne qu'on étend à  droite
  # la matrice x contient : 
  # 0.0 0.55 1.11 ... 5
  # 0.0 0.55 1.11 ... 5
  # 0.0 0.55 1.11 ... 5
  # ...
  # 0.0 0.55 1.11 ... 5

  # la matrice y contient : 
  # 0.00 0.00 0.00 ... 0.00
  # 0.55 0.55 0.55 ... 0.55
  # 1.11 1.11 1.11 ... 1.11
  # ...
  # 5.00 5.00 5.00 ... 5.00
  
  x, y = np.meshgrid(x, y)       
  print(f"Matrice x:\n {x}")                      # matrice de 400 valeurs???
  print(f"Matrice y:\n {y}")
  z = f(x,y)

  Figure = plt.figure()
  Graphe3D = Figure.add_subplot(111, projection='3d')
  Graphe3D.plot_surface(x, y, z, cmap="plasma")   # https://matplotlib.org/stable/tutorials/colors/colormaps.html
  plt.show()



# -----------------------------------------------------------------------------
# 3D
def ThreeD_Demo3():
  
  f=lambda x, y : np.sin(x) + np.sin(x+y) 
  x=np.linspace(0, 5, 10)  
  y=np.linspace(0, 5, 10)
  x, y = np.meshgrid(x, y)       
  z = f(x,y)

  fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
  ax.plot_surface(x, y, z, cmap="plasma")   


# -----------------------------------------------------------------------------
def Histogramme0():
  
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
def Histogramme1():
  
  Iris = load_iris()
  x = Iris.data
  y = Iris.target
  names = list(Iris.target_names)

  fig, axs = plt.subplots(2, 1)
  axs[0].hist(x[:,0])
  axs[0].hist(x[:,0], bins=20)
  axs[0].set_title("2 fois le même jeu mais bin différents")
  axs[1].hist(x[:,0])
  axs[1].hist(x[:,1])
  axs[1].set_title("2 jeux différents")
  plt.show()




# -----------------------------------------------------------------------------
# Hist 2D
def Histogramme2D0():
  
  Iris = load_iris()
  x = Iris.data
  y = Iris.target
  names = list(Iris.target_names)

  Figure = plt.figure()
  Graphe = Figure.add_subplot(111) # nrows ncols index
  Graphe.hist2d(x[:,0], x[:,1])
  Graphe.set_xlabel("Longeur sépal")
  Graphe.set_ylabel("Largeur sépal")
  # plt.colorbar() # fonctionne pas 
  plt.show()



# -----------------------------------------------------------------------------
# Hist 2D
# Suivre la distribution des données quand elles suivent 2 variables
def Histogramme2D1():
  
  Iris = load_iris()
  x = Iris.data
  y = Iris.target
  names = list(Iris.target_names)

  fig, ax = plt.subplots()
  h = ax.hist2d(x[:,0], x[:,1])
  ax.set_xlabel("Longeur sépal")
  ax.set_ylabel("Largeur sépal")
  cbar = fig.colorbar(h[3])
  plt.show()


# -----------------------------------------------------------------------------
def HistoImg0():
  
  face = misc.face(gray=True)
  plt.imshow(face, cmap="gray")


  Figure = plt.figure()
  Graphe = Figure.add_subplot(111) # nrows ncols index
  Graphe.hist(face.ravel(), bins=255) # ravel applati l'image
  plt.show()  


# -----------------------------------------------------------------------------
def HistoImg1():
  
  face = misc.face(gray=True)
  plt.imshow(face, cmap="gray")

  fig, ax = plt.subplots()
  ax.hist(face.ravel(), bins=255)
  plt.show()  



# -----------------------------------------------------------------------------
def ContourPlot0():
  
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
  #Graphe.contourf(x, y, z, 20, cmap="RdGy")      # Attention au 'f' pour filled
  # Graphe.contourf(x, y, z, 10, cmap=cm.jet)
  ContourSet = Graphe.contourf(x, y, z, 10, cmap=cm.jet)
  Graphe.clabel(ContourSet, inline=1, fontsize=8, colors="black")
  plt.show()    


# -----------------------------------------------------------------------------
def ContourPlot1():
  
  f = lambda x, y : np.sin(x) + np.sin(x+y) 
  x = np.linspace(0, 5, 100)  
  y = np.linspace(0, 5, 100)
  x, y = np.meshgrid(x, y)       
  z = f(x,y)

  fig, ax = plt.subplots()
  # ax.contour(x, y, z)
  # ax.contour(x, y, z, 20)                    # 20 lignes de niveau
  # ax.contour(x, y, z, 20, colors='black')    # Attention au 's' à colors. Lignes en noir
  # ax.contourf(x, y, z, 20, cmap="RdGy")
  # ax.contourf(x, y, z, 10, cmap=cm.jet)
  Cs1 = ax.contour(x, y, z, 10, colors="red")
  Cs2 = ax.contourf(x, y, z, 10, cmap=cm.jet)
  ax.clabel(Cs1, inline=1, fontsize=8, colors="black")
  cbar = fig.colorbar(Cs2)
  cbar.add_lines(Cs1)
  plt.show()    


# -----------------------------------------------------------------------------
def DemoImage0():
  face = misc.face()
  plt.imshow(face)
  plt.show()

# -----------------------------------------------------------------------------
def DemoImage1():
  face = misc.face(gray=True)
  plt.imshow(face, cmap="gray")
  plt.show()

  
# -----------------------------------------------------------------------------
def DemoImage2():
  # Face est juste un tableau de pixels
  # On affiche la matrice de correlaction entre les colonnes (c'est pour ça qu'on prend la transposée)
  Iris = load_iris()
  x = Iris.data
  
  #plt.imshow(np.corrcoef(x.T))
  #plt.imshow(np.corrcoef(x.T), cmap="Blues")
  plt.imshow(np.corrcoef(x.T), cmap=cm.jet)
  plt.colorbar()
  plt.show()

# -----------------------------------------------------------------------------
def DemoImage3():
  Iris = load_iris()
  x = Iris.data
  
  fig, ax = plt.subplots()
  im = ax.imshow(np.corrcoef(x.T), cmap=cm.jet)
  fig.colorbar(im)
  plt.show()

# -----------------------------------------------------------------------------
# Optimisation d'affichage
def DemoImage4():
  f=lambda x, y : np.sin(x) + np.sin(x+y) 
  x=np.linspace(0, 5, 100)  
  y=np.linspace(0, 5, 100)
  x,y = np.meshgrid(x, y)       
  z = f(x,y)                                  # z = 100x100
  
  fig, ax = plt.subplots()
  im = ax.imshow(z, cmap=cm.jet)
  fig.colorbar(im)
  plt.show()


# -----------------------------------------------------------------------------
# afficher sur la même figure, les différentes variables
def Exercice1():
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
# afficher sur la même figure, les différentes variables
def Exercice2():
  Iris = load_iris()
  x = Iris.data
  y = Iris.target

  n = x.shape[1]
  fig, axs = plt.subplots(n//2, n//2, figsize=(12, 12/1.618)) # axs is a matrice not a list

  for i in range(n):
    axs[i//2, i%2].scatter(x[:, 0], x[:, i], c = y)
    axs[i//2, i%2].set_xlabel("0")
    axs[i//2, i%2].set_ylabel(i)
  plt.show()  

# -----------------------------------------------------------------------------
# afficher sur la même figure, les différentes variables
def Exercice3():
  Iris = load_iris()
  x = Iris.data
  y = Iris.target

  n = x.shape[1]
  fig, axs = plt.subplots(n//2, n//2, figsize=(12, 12/1.618)) # axs is a matrice not a list
  axs = axs.ravel()
  for i, ax in enumerate(axs) :
    ax.scatter(x[:, 0], x[:, i], c = y)
    ax.set_xlabel("0")
    ax.set_ylabel(i)
  plt.show()  

  
  


# -----------------------------------------------------------------------------
def main():
  #Scatter_Demo()
  # ThreeD_Demo0()
  # ThreeD_Demo1()
  # ThreeD_Demo2()
  # ThreeD_Demo3()
  # Histogramme0()
  # Histogramme1()
  # Histogramme2D0()
  # Histogramme2D1()
  # HistoImg0()
  # HistoImg1()
  # ContourPlot0()
  #ContourPlot1()
  # DemoImage0()
  # DemoImage1()
  # DemoImage2()
  #DemoImage3()
  #DemoImage4()
  # Exercice1()
  # Exercice2()
  Exercice3()

if __name__ == '__main__':
  main()