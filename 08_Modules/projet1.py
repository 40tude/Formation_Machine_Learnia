def Fibonacci(limit):
  # retourne dans une liste, la suite de Fibonacci jusqu'à limit 
  f=[0,1]
  n = 1
  while f[n] < limit:
    n+=1
    f.append(f[n-1] + f[n-2])
  return f