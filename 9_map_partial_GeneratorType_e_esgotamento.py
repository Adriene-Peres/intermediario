# map, partial, GeneratorType e esgotamento de Iterators


from functools import partial

# map - para mapear dados
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


# mapeamento

""""
Uma alternativa ao que foi feito seria criar uma função 
para aumentar o valor:

novos_produtos = [
    {**produto, 'preco': round(produto['preco']*1.10, 2)} 
    for produto in produtos
] 

"""

def aumentar_valor(valor, porcentagem):
    return round(valor*porcentagem,2)

aumentar_dez_porceto = partial(aumentar_valor, porcentagem = 1.1)

# novos_produtos = [
#     {**produto, 'preco': aumentar_dez_porceto(produto['preco'])} 
#     for produto in produtos
# ] 

def muda_preço_de_produtos(produto):
    return  {
        **produto, 
        'preco': aumentar_dez_porceto(
            produto['preco']
        )
    }

novos_produtos = map(
    muda_preço_de_produtos,
    produtos
)

print_iter(produtos)
print_iter(novos_produtos)

