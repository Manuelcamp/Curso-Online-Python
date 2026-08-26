import copy
import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

# copy, sorted, produtos.sort
# Exercícios
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)


novos_produtos = [ 
    {**p,'preco': round(p['preco'] * 1.1, 2)}
    for p in copy.deepcopy(produtos)
]
p(novos_produtos)

print('--------------------------------')

# novos_produtos = copy.deepcopy([
#     {**produto,'preco': produto['preco'] * 1.10}
#     for produto in produtos
# ])


# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos), 
    key=lambda item: item['nome'],
    reverse=True
    )
p(produtos_ordenados_por_nome)

print('--------------------------------')
# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

produtos_ordenados_por_preco = copy.deepcopy(sorted(novos_produtos, key=lambda item: item["preco"]))
p(produtos_ordenados_por_preco)