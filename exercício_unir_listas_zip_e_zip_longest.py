# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

from itertools import zip_longest

def zipper(lista1, lista2):
  tam = min(len(lista1),len(lista2))
  return [
    (lista1[i],lista2[i]) for i in range(tam)
  ]


cidade = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estado = ['BA', 'SP', 'MG', 'RJ']

print(zipper(cidade,estado))

# OBS.: existe uma função no Python que chama zip que faz o mesmo que 
# foi pedido no exercício, essa função retorna um iterator.

print('--------------------------------------------------------------------')
print(list(zip(cidade, estado)))


# existe um módulo no Python chamado itertools que contém o 'zip_longest' que 
# é a mesma coisa de 'zip', só que invertido, ou seja, ele utiliza o tamanho da lista maior.

print('--------------------------------------------------------------------')
print(list(zip_longest(cidade, estado, fillvalue = 'SEM CIDADE')))
