encomendas=input("Digite os números das encomendas separadas por vígulas:").split(',')
try:
  for encomenda in encomendas :
    print (in (encomenda))
except valueError:
  print (" Uma das entradas não é um número válido.")
