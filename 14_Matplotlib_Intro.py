# py -m venv .\PrjVEnv          				            # créé, entre autres, un sous repertoire PrjVEnv                     
# code .                                            # Lance Visual Studio Code
# choisir son debugueur python                      # CTRL + SHIFT + P puis Python Select Interpreter 
                                                    # Choisir l'interpreteur avec l'environnment virtuel
                                                    # Python 3.10.7 ('PrjVEnv':venv)./PrjVEnv/Scripts/python.exe
                                                    # Dans la console dans VS Code on voit (PrjVEnv) en début de prompt 
# Depuis la console de VS Code
# python -m pip install numpy matplotlib            # install les lib

import numpy as np
import matplotlib.pyplot as plt



###############################################################################
# Mode Classique
# In the implicit interface, inspired by and modeled on MATLAB, we use a global 
# state-based interface which is encapsulated in the pyplot module to plot to 
# the "current Axes". 
# https://matplotlib.org/stable/users/explain/api_interfaces.html#api-interfaces
def Mode_Classique_0() -> None :
  x = np.linspace(0, 2, 100)
  y = x**2

  plt.plot(x, y)                # Lance l'affichage sans que show() soit invoquée
  # plt.show()

  x2 = np.linspace(0, 2, 10)
  y2 = x2**2
  plt.scatter(x2, y2)
  # plt.show()
  
  # Faire simple
  # Apprendre 2 ou 3 paramètres
  # couleur     c  = "red" "black"... see https://matplotlib.org/stable/gallery/color/named_colors.html
  # line style  ls =
  # line width  lw =
  # label       label="Courbe" 

  plt.plot(x, y/2, c="moccasin", lw=5, ls="--") # nom de couleur CSS
  # plt.show()
  # plt.close(None)                   # None => close current figure


  

###############################################################################
# Mode Classique
# Cycle de vie d'une figure
def Mode_Classique_1() -> None :
  x = np.linspace(0, 2, 100)
  y = x**2
 
  # fig = plt.figure()
  fig = plt.figure(figsize=(12, 8))
  plt.plot(x, y, label="vehicle 1")
  plt.plot(x, x**3, label="vehicle 2")
  plt.title("Fig. 1")
  plt.xlabel("Time (s)")
  plt.ylabel("Speed (m/s)")
  plt.legend() 
  plt.savefig('Fig1.png')
  plt.savefig('Fig1.svg')
  fig.savefig("Figure.png")
  # plt.show()
  # plt.close(None)                   # None => close current figure


###############################################################################
# Mode Classique
def Mode_Classique_2() -> None :
  x = np.linspace(0, 2, 100)
  y = x**2
  
  # Sub plots
  plt.subplot(2, 1, 1)              # row, col, index starts at 1
  plt.plot(x, y, c="red")
  # fixer la limit en y
  axes = plt.gca()                  # Get current axes
  axes.set_ylim([None, 8])

  plt.subplot(2, 1, 2)              # row, col, index
  plt.plot(x, x**3, c="blue")
    
  # plt.show()
  # plt.close(None)                   # None => close current figure






###############################################################################
# Mode Objet
# In the explicit object-oriented (OO) interface we directly utilize instances 
# of axes.Axes to build up the visualization in an instance of figure.Figure.
# https://matplotlib.org/stable/users/explain/api_interfaces.html#api-interfaces 
def Mode_Objet_0() -> None:

  x = np.linspace(0, 2, 100)
  y = x**2

  fig, ax = plt.subplots()      # bien voir le s à subplots
                                # An Axes object encapsulates all the elements of an individual (sub-)plot in a figure.
  ax.plot(x, y)
  # plt.show()
  # plt.close(None)               # None => close current figure


  



###############################################################################
# Mode Objet
def Mode_Objet_1() -> None:

  x = np.linspace(0, 2, 100)
  y = x**2
  
  fig, axs = plt.subplots(2, 1, sharex=True) 
  axs[0].set_ylim([None, 8])                    # on peut passer un tuple ou une liste (un iterator)
  axs[0].plot(x, y)
  axs[1].plot(x, x**3)
  # plt.show()
  # plt.close(None)                             # None => close current figure



# -----------------------------------------------------------------------------
def Exercice():
  # crée un dataset
  NbCharts = 4
  XMax = 50
  dataset = {f"Experience{i}" : np.random.randn(XMax) for i in range(NbCharts)}

  # affiche les courbes sur un seule figure
  fig, axs = plt.subplots(NbCharts, 1, sharex=True)
  fig.suptitle("Titre de la figure")
  for i in range(NbCharts):
    axs[i].plot(range(XMax), dataset[f"Experience{i}"], label=f"Experience {i}:")
    axs[i].legend(loc="upper left")
  
  # plt.show()



# -----------------------------------------------------------------------------
def Corrigé():
  # crée un dataset
  NbChart = 4
  XMax = 50
  dataset = {f"Experience{i}" : np.random.randn(XMax) for i in range(NbChart)}

  n = len(dataset)
  plt.figure(figsize=(12,8))
  for k,i in zip(dataset.keys(), range(1, n+1)):  # attention au s de keys
    plt.subplot(n, 1, i)                          # Z! index starts at 1
    plt.plot(dataset[k])
    plt.title(k)
  # plt.show()  



# -----------------------------------------------------------------------------
def Corrigé2():
  # crée un dataset
  NbChart = 4
  XMax = 100
  dataset = {f"Experience{i}" : np.random.randn(XMax, 3) for i in range(NbChart)} # on a 3 variables dans cahque dataset

  n = len(dataset)
  Figure = plt.figure(figsize=(12, 7.4))
  for k,i in zip(dataset.keys(), range(1, n+1)):  # attention au s de keys. zip retourne un iterator de tuples
    Graphe = Figure.add_subplot(n, 1, i)          # nrows ncols index - 1,1,1 par défaut
    Graphe.plot(dataset[k])
    Graphe.set_title(k)
  # plt.show()  







# -----------------------------------------------------------------------------
def main():
  
  # Mode_Classique_0()
  # Mode_Classique_1()
  # Mode_Classique_2()
  
  # Mode_Objet_0()
  # Mode_Objet_1()

  Exercice()
  Corrigé()
  Corrigé2()

if __name__ == '__main__':
  main()
  