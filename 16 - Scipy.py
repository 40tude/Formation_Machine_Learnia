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
from scipy.interpolate import interp1d
from scipy import optimize
from scipy import signal
from scipy import fftpack
from scipy import ndimage

# -----------------------------------------------------------------------------
def Interpolate():
  x = np.linspace(0, 10, 10)
  y = x**2
  
  Figure = plt.figure()
  Graphe = Figure.add_subplot()
  Graphe.scatter(x, y)

  # Pour kind voir : https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.interp1d.html
  f = interp1d(x, y, kind='linear')
  x2 = np.linspace(0, 10, 100)               # 10 fois plus de points
  Graphe.scatter(x2, f(x2), s=1, c='red')

  plt.show()
  


# -----------------------------------------------------------------------------
def Interpolate2():
  x = np.linspace(0, 10, 10)
  y = np.sin(x)
  
  Figure = plt.figure()
  Graphe = Figure.add_subplot()
  Graphe.scatter(x, y)

  f = interp1d(x, y, kind='linear')
  x2 = np.linspace(0, 10, 100)               # 10 fois plus de points
  Graphe.scatter(x2, f(x2), s=1, c='red')


  g = interp1d(x, y, kind='cubic')
  x2 = np.linspace(0, 10, 100)               # 10 fois plus de points
  Graphe.scatter(x2, g(x2), s=2, c='green')

  plt.show()

# -----------------------------------------------------------------------------
def f (x, a, b, c, d):
  return a * x**3 + b*x**2 + c*x +d

def Optimize():
  # https://docs.scipy.org/doc/scipy/reference/optimize.html?highlight=scipy%20optimize#module-scipy.optimize
  # minimize, curve fit, algebre lineaire
  # Note : vaut mieux faire ce type de curve fitting dans SciKitLearn

  x = np.linspace(0, 2, 100)
  y = 1/3*x**3 - 3/5*x**2 + 2 * np.random.randn(x.shape[0])/20
  Figure = plt.figure()
  Graphe = Figure.add_subplot()
  Graphe.scatter(x, y)

  # Retourne 2 tableaux numpy
  # les paramètres a, b, c, d 
  # la matrice de covariance du modèle (???)
  Param, MatParamCov = optimize.curve_fit(f, x, y)
  Graphe.plot(x, f(x, Param[0], Param[1], Param[2],Param[3]), c="green", lw="2")
  plt.show()



# -----------------------------------------------------------------------------
def f(x):
  return x**2 + 15*np.sin(x)

def Minimize():
  x = np.linspace(-10, 10, 100)
  y = f(x)
  Figure = plt.figure()
  Graphe = Figure.add_subplot()
  Graphe.plot(x, y)

  x0=-7.5
  Info = optimize.minimize(f, x0)
  print(Info)
  xmin0 = Info.x
  Graphe.scatter(x0,   f(x0),   s=100, c = "Green", zorder = 2)
  Graphe.scatter(xmin0, f(xmin0), s=100, c = "Red",   zorder = 2)


  x1=-4
  Info = optimize.minimize(f, x1)
  xmin1 = Info.x
  Graphe.scatter(x1,   f(x1),   s=100, c = "Green", zorder = 2)
  Graphe.scatter(xmin1, f(xmin1), s=100, c = "Red",   zorder = 2)
  
  
  plt.show()

# -----------------------------------------------------------------------------
# la fonction attend un tableau de 2 coordonnées
def f1(pt):
  return np.sin(pt[0]) + np.cos(pt[0]+pt[1])*np.cos(pt[0])

def Minimze2D():
  x = np.linspace(-3, 3, 100)
  y = np.linspace(-3, 3, 100)

  x, y = np.meshgrid(x, y)
  
  Figure = plt.figure(figsize=(5, 5)) # Make sure the figure is a square. /!\Inches
  Graphe = Figure.add_subplot()
  Graphe.contour(x, y, f1(np.array([x,y])), 20)

  Pt0 = np.zeros((2,1))
  Graphe.scatter(Pt0[0], Pt0[1], s=25, c="Green")

  Info = optimize.minimize(f1, Pt0) # Pt0 doit être un 1D array. Voir https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html#scipy.optimize.minimize
  PtMin = Info.x
  Graphe.scatter(PtMin[0], PtMin[1], s=25, c="Red")
  
  plt.show()



# -----------------------------------------------------------------------------
def SignalProcessing():
  x = np.linspace(0, 20, 100)
  y = x + 4*np.sin(x) + np.random.randn(x.shape[0])
  Figure = plt.figure()
  Graphe = Figure.add_subplot()
  Graphe.plot(x, y)

  # Eliminer la tendance linéraire du signal
  y1 = signal.detrend(y)
  Graphe.plot(x, y1)

  plt.show()


# -----------------------------------------------------------------------------
def FFT():
  x = np.linspace(0, 30, 1024)
  y = 3 * np.sin(x) + 2 * np.sin(5*x) + np.sin(10*x)
  Figure = plt.figure()
  Graphe = Figure.add_subplot()
  #Graphe.plot(x, y)

  tft = fftpack.fft(y)
  freq = fftpack.fftfreq(y.size)
  #Graphe.plot(freq, tft)
  Graphe.plot(np.abs(freq), np.abs(tft))

  plt.show()


# -----------------------------------------------------------------------------
def FFT2():
  x = np.linspace(0, 30, 1000)
  y = 3 * np.sin(x) + 2 * np.sin(5*x) + np.sin(10*x) + np.random.random(x.shape[0])*10
  
  Figure = plt.figure()
  Graphe1 = Figure.add_subplot(311)
  Graphe1.plot(x, y)

  tft = fftpack.fft(y)
  power = abs(tft)
  freq = fftpack.fftfreq(y.size)
  Graphe2 = Figure.add_subplot(312)
  Graphe2.plot(np.abs(freq), power)

  # on filtre les valeur de la TFT qui sont inf à un certains seuil
  seuil = 400
  tft[power<seuil] = 0.0
  Graphe3 = Figure.add_subplot(313)
  Graphe3.plot(np.abs(freq), np.abs(tft))

  Filtered = fftpack.ifft(tft)
  Graphe1.plot(x, Filtered)

  plt.show()


# -----------------------------------------------------------------------------
def TraitementImage():
  np.random.seed(0)
  x = np.zeros((32,32)) # faut passer un tuple !!!
  x[10:-10, 10:-10] = 1
  x[np.random.randint(0, 32, 30), np.random.randint(0, 32, 30)] = 1
  plt.imshow(x)
  plt.show()

  # On filtre les pixels isolés
  OpenX = ndimage.binary_opening(x)
  plt.imshow(OpenX)
  plt.show()



# -----------------------------------------------------------------------------
def Bacteries():

  image = plt.imread("Bacteria.png")
  print(image.shape)
  image = image[:,:,0] #subseting, enlève la 3eme dimmension. Pas oublier img = img...
  print(image.shape)
  
  plt.imshow(image, cmap="gray")
  # plt.show()

  # Extraire les bacteries de l'ar plan
  image_2 = np.copy(image)
  plt.hist(image_2.ravel(), bins=255)
  # plt.show()

  # on veut garder les pixels les plus sombres
  # on filtre tout ce qui est inf à 0.6 avec boolean indexing
  image = image < 0.6
  # image est dorénavant un masque booléen
  plt.imshow(image)
  # plt.show()
  
  # retirer les artefacts, les pixels isolés
  OpenX = ndimage.binary_opening(image)
  plt.imshow(OpenX)
  # plt.show()
  
  # labeliser le contenu
  LabeledImage, NbLabels = ndimage.label(OpenX)
  print(NbLabels)
  plt.imshow(LabeledImage)
  plt.show()

  #Compter le nb de pixels dans chaque bactérie
  sizes = ndimage.sum(OpenX, LabeledImage, range(NbLabels))

  Figure = plt.figure()
  Graphe1 = Figure.add_subplot()
  Graphe1.scatter(range(NbLabels), sizes)
  plt.show()

  
  





# -----------------------------------------------------------------------------
# https://docs.scipy.org/doc/scipy/reference/index.html
def main():
  
  # Interpolate()
  # Interpolate2()
  #Optimize()
  #Minimize()
  #Minimze2D()
  # SignalProcessing()
  #FFT()
  #FFT2()
  #TraitementImage()
  Bacteries()



if __name__ == '__main__':
  main()