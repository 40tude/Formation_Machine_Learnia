# py -m venv .\PrjVEnv          				            # créé, entre autres, un sous repertoire PrjVEnv                     
# code .                                            # Lance Visual Studio Code
# choisir son debugueur python                      # CTRL + SHIFT + P puis Python Select Interpreter 
                                                    # Choisir l'interpreteur avec l'environnment virtuel
                                                    # Python 3.10.7 ('PrjVEnv':venv)./PrjVEnv/Scripts/python.exe
                                                    # Dans la console dans VS Code on voit (PrjVEnv) en début de prompt 
# Depuis la console de VS Code
# python -m pip install numpy matplotlib panda xlrd   # install les lib

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# -----------------------------------------------------------------------------
def Demo1():
  data = pd.read_excel("titanic.xls")
  print()
  print(data.shape)
  print()
  print(data.columns)
  print()
  print(data.head())
  print()
  print(data.describe())
  print()

  # supprime les colonnes pas utiles
  data = data.drop(["name", "sibsp", "parch", "ticket", "fare", "cabin", "embarked", "boat", "body", "home.dest"], axis=1)
  print(data.head())
  print()

# -----------------------------------------------------------------------------
# Panda : dataframe, traitement des données

def main():
  Demo1()


if __name__ == '__main__':
  main()