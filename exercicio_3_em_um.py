# copy, sorted, produtos.sort
# Exercícios

from dados import produtos
import copy

# Aumente os preços dos produtos em 10%
# Gere novos_produtos por deep copy (cópia profunda)

novos_produtos = copy.deepcopy(produtos)

novos_produtos = [{**produto, 'preco': round(produto['preco'] * 1.1, 2)}
            for produto in novos_produtos]

print(*produtos, sep='\n')
print()
print(*novos_produtos,sep='\n')

print('------------------------------------------------------------------')

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos), 
    key=lambda item:item['nome'], 
    reverse=True
)


print()
print(*produtos_ordenados_por_nome,sep='\n')

print('------------------------------------------------------------------')

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda item:item['preco']
)

print()
print(*produtos_ordenados_por_preco, sep='\n')