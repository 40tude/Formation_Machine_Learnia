# py -m venv .\PrjVEnv          				            # créé, entre autres, un sous repertoire PrjVEnv                     
# code .                                            # Lance Visual Studio Code
# choisir son debugueur python                      # CTRL + SHIFT + P puis Python Select Interpreter 
                                                    # Choisir l'interpreteur avec l'environnment virtuel
                                                    # Python 3.10.7 ('PrjVEnv':venv)./PrjVEnv/Scripts/python.exe
                                                    # Dans la console dans VS Code on voit (PrjVEnv) en début de prompt 
# Depuis la console de VS Code
# python -m pip install numpy scipy                 # install les lib

# -----------------------------------------------------------------------------
def avec_listes():
  liste1=[]
  for i in range(10):
    liste1.append(2*i)

  liste2=[i**3 for i in range (5)]

  # nested listes
  # vaut mieux commencer par la nested liste puis après ajouter "for j..."
  # on va créer 4 listes de 5 éléments
  liste3=[[i**3 for i in range (5)] for j in range (4)]
  print (liste3)  



# -----------------------------------------------------------------------------
def avec_dico():
  dico = {
    0 : "riri",
    1 : "fifi",
    2 : "loulou" 
  }

  prénoms = ["riri", "fifi", "loulou"]

  dico2 ={
    i:prénoms[i] for i in range(3)
  }
  print (dico2)

  dico3 ={
    # enumerate retourne un couple indice valeur
    # k, v pour key value
    k:v for k,v in enumerate(prénoms)
  }
  print (dico3)

  dico4 ={
    k*10:v.capitalize() for k,v in enumerate(prénoms)
  }
  print (dico4)

  ages=[13, 15, 18, 42]
  dico5 ={
    p.capitalize():a for p,a in zip(prénoms, ages) # zip retourne un iterator de tuples
  }
  print (dico5)


  ages2=[22, 15, 42, 100]
  dico6 ={
    p.capitalize():a for p,a in zip(prénoms, ages2) if a > 20
  }
  print (dico6)






# -----------------------------------------------------------------------------
def avec_tuple():
  # c'est un générator !
  # tuple1 = (i**3 for i in range(5))
  # print(tuple1)

  # ça ca marche
  tuple1 = tuple(i**3 for i in range(5))
  print("Tuple1", tuple1)





# -----------------------------------------------------------------------------
def exercice():
  # dictionnaire k:v
  # k 0:20
  # v = k**2
  Dico = {
    str(k):k**2 for k in range (20)
    #k:k**2 for k in range (20)
  }
  print ("Dico de l'exercice : ", Dico)
  print(f"Dictionnaire de l'exercice avec une f-string : {Dico}")




def main():
  avec_listes()
  avec_dico()
  avec_tuple()
  exercice()

  
if __name__ == '__main__':
  main()