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
  tableau1 = np.array([10, 11, 12])                 # https://numpy.org/doc/stable/reference/generated/numpy.array.html
  
  liste = [i**3 for i in range (5)]
  tableau2 = np.array(liste)

  tableau3 = np.array([i**2 for i in range (10)])
  print(tableau3)
  print(tableau3.size)


if __name__ == '__main__':
  main()