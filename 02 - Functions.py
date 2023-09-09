# py -m venv .\PrjVEnv          				            # créé, entre autres, un sous repertoire PrjVEnv                     
# code .                                            # Lance Visual Studio Code
# choisir son debugueur python                      # CTRL + SHIFT + P puis Python Select Interpreter 
                                                    # Choisir l'interpreteur avec l'environnment virtuel
                                                    # Python 3.10.7 ('PrjVEnv':venv)./PrjVEnv/Scripts/python.exe
                                                    # Dans la console dans VS Code on voit (PrjVEnv) en début de prompt 
# Depuis la console de VS Code
# python -m pip install numpy scipy                 # install les lib


f = lambda x,y : x**2 + y

def nrj_pot2(m, h, limit, g=9.81):
  nrj = m * g *h
  if nrj>limit:
    return True, nrj
  else:
    return False, nrj


def nrj_pot(m, h, g=9.81):
  nrj = m * g *h
  return nrj


def main():

  print(f(3,1))
  print(f(5,1))

  nrj = nrj_pot(100, 5, 9.8)
  print(nrj)

  nrj = nrj_pot(h=5, m=100)
  print(nrj)

  AboveLimit, Nrj = nrj_pot2(1, 1, 10)
  print(AboveLimit, Nrj)

  AboveLimit, Nrj = nrj_pot2(15, 1, 10)
  print(AboveLimit, Nrj)


if __name__ == '__main__':
   main()
   