"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]

"""
from itertools import zip_longest

# primeira forma
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

lista_soma1 = [x + y for x,y in zip(lista_a,lista_b)]

print('soma1:', lista_soma1)
print()

intervalo = min(len(lista_a),len(lista_b))

# segunda forma
lista_soma2 = []
for i in range(intervalo):
    lista_soma2.append(lista_a[i] + lista_b[i])

print('soma2:', lista_soma2)
print()


# fazendo o mesmo exeecio porém considerando o tamaho da lista maior:
# para isso deve-se fazer o import -> 'from itertools import zip_longest'

lista_soma3 = [x + y for x,y in zip_longest(lista_a,lista_b, fillvalue=0)]

print('soma3:', lista_soma3)
print()
