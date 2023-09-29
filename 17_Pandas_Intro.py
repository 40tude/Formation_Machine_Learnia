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
  df = pd.read_excel("titanic.xls")
  print(df.shape)
  print(df.columns)
  print(df.head())
  print(df.describe())

  # supprime les colonnes pas utiles
  df = df.drop(["name", "sibsp", "parch", "ticket", "fare", "cabin", "embarked", "boat", "body", "home.dest"], axis=1)
  print(df.head())
  print(df.describe())

  # describe montre qu'il y a des ages qui manquent encore
  df = df.dropna(axis=0)
  print(df.describe())

  # Nb de passager par classe
  NbPerClass = df['pclass'].value_counts() # compte les répétitions
  print(NbPerClass)
  print(NbPerClass[3])
  #df['pclass'].value_counts().plot.bar()
  df["age"].hist()
  df["age"].plot.hist(bins=20) # le nb de paquets à utiliser
  
  # Afficher les moyennes, regroupées par sexe
  print(df.groupby(['sex']).mean())
  
  # groupby retourne est un dataframe
  df_bysex = df.groupby(['sex']).mean()
  print(f"{df_bysex['survived']['female']:.2f} % des femmes ont survécu")
  print(f"{df_bysex['survived']['male']:.2f} % des hommes ont survécu")
  
  df_SexClass = df.groupby(by=['sex', 'pclass']).mean()
  print(df_SexClass)
  # TO DO : comment accèder aux valeurs?
  #print(f"{df_SexClass['survived']['female']['pclass']:.2f} % des femmes en 1ere ont survécu")
  pass

# -----------------------------------------------------------------------------
# Panda : dataframe, traitement des données

def main():
  Demo1()


if __name__ == '__main__':
  main()