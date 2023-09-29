# py -m venv .\PrjVEnv          				            # créé, entre autres, un sous repertoire PrjVEnv                     
# code .                                            # Lance Visual Studio Code
# choisir son debugueur python                      # CTRL + SHIFT + P puis Python Select Interpreter 
                                                    # Choisir l'interpreteur avec l'environnment virtuel
                                                    # Python 3.10.7 ('PrjVEnv':venv)./PrjVEnv/Scripts/python.exe
                                                    # Dans la console dans VS Code on voit (PrjVEnv) en début de prompt 
# Depuis la console de VS Code
# python -m pip install numpy scipy                 # install les lib



# Retourne la suite de Fiboncci jusqu'à limit
def Fibonacci2(limit):
  f=[0,1]
  n = 1
  while f[n] < limit:
    n+=1
    f.append(f[n-1] + f[n-2])
  return f


def TestZip():
  liste1 = [23, 43, 56, 81, 108]
  liste2 = ["Riri", "Fifi", "Loulou"]
  for age, nom in zip(liste1, liste2): # zip retourne un iterator de tuples
    print (age, " - ", nom)



def Test():
  liste = ["Paris", "Toulouse", "Brest", "Bastia"]
  n = liste.index("Brest")
  print(n)
  #print(liste.index("Zanzibar")) # Part en erreur

  liste.append("Ghisoni")
  print (liste)

  liste.insert(2, "Madrid")
  print (liste)

  liste.extend(("Ajaccio", "Bonifacio")) # peut ajout un iterable (tuple ou liste ou...)
  print (liste)
  print (len(liste))

  liste.sort(reverse=True)
  print(liste)

  print(liste.count("Paris"))
  
  if ("Paris" in liste) :
    print ("In the list")
  else:
    print ("Not in list")

  for v in liste:
    print (v[0])

  # enumerate retourne un couple
  for index, ville in enumerate(liste):
    print (index, " ---- ", ville)  

  # S'arrête à la fin de la liste la plus courte
  liste2 = [75, 12, 24, 44]
  for x, y in zip (liste2, liste):
    print (y, x)





def main():
  liste1 = [1,2,3]
  liste2 = ["Paris", "Toulouse", "Brest", "Bastia"]
  liste3 = [liste1, liste2]                           # contient 2 listes
  liste4 = []
  liste5 = [1, 2, 3, "Toulouse"]

  tuple1=(1,2,3)

  Nom = "Robert"

  # list, tuple et string sont des séquences (y a un  ordre)

  print (liste2[0], "     ", liste2[1], "     ", liste2[-1])

  #slicing [debut:fin:pas] - Z! fin exclue
  print(liste2[1:2]) # n'imprime pas 2
  print(liste2[1:-1]) # imprime pas le dernier
  print(liste2[:2]) # imprime à partir de 0
  print(liste2[2:]) # imprime jusqu'au dernier!
  print(liste2[::2]) # imprime du début à la fin de 2 en 2
  print(liste2[::-1]) # imprime à l'envers toute la liste

  #Test()





if __name__ == '__main__':
   # TestZip()
  # Test()
  # main()
  print(Fibonacci2(4))
   