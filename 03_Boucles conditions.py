# py -m venv .\PrjVEnv          				            # créé, entre autres, un sous repertoire PrjVEnv                     
# code .                                            # Lance Visual Studio Code
# choisir son debugueur python                      # CTRL + SHIFT + P puis Python Select Interpreter 
                                                    # Choisir l'interpreteur avec l'environnment virtuel
                                                    # Python 3.10.7 ('PrjVEnv':venv)./PrjVEnv/Scripts/python.exe
                                                    # Dans la console dans VS Code on voit (PrjVEnv) en début de prompt 
# Depuis la console de VS Code
# python -m pip install numpy scipy                 # install les lib

# Imprime la suite de Fiboncci jusqu'à limit
def Fibonacci(limit):
  f0=0
  f1=1
  print (f0)
  print (f1)
  while f1 < limit:
    tmp = f1
    f1 = f1+f0
    f0 = tmp
    print (f1) 

# Imprime la suite de Fiboncci jusqu'à limit
def Fibonacci2(limit):
  f0=0
  f1=1
  while f0 < limit:
    print (f0) 
    f0, f1 = f1, f0+f1

def main():
  # Fibonacci2 (100)

  for i in range (10, 0, -1): # de 10 à 1
    print(i)
  
  print()
  for i in range (9, -1, -1): # de 9 à 0
    print(i)

  # j=0
  # for i in range(5):
  #   j+=1                                            # j++ n'est pas supporté
  # print(j)


if __name__ == '__main__':
   main()
   