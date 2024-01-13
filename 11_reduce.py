# reduce - faz a redução de um iterável em um único valor
# deve-se fazer import

from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 22},
    {'nome': 'Produto 3', 'preco': 2},
    {'nome': 'Produto 2', 'preco': 6},
    {'nome': 'Produto 4', 'preco': 4},
]

# def funcao_do_reduce(acumulador, produto):
#     return acumulador + produto['preco']

total = reduce(
    lambda acumulador, produto: acumulador + produto['preco'],
    produtos,
    0.0
)

# total = reduce(
#     funcao_do_reduce,
#     produtos,
#     0.0
# )

print('O total é:', total)

# ----------------------------------------
# total = 0
# for produto in produtos:
#     total += produto['preco']
# print(total)

# ----------------------------------------
# print(sum([produto['preco'] for produto in produtos])) - list comprehesion