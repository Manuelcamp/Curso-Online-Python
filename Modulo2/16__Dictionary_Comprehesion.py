produto = {
    'nome': 'Caneta Azul',
    'preco': 2.6,
    'Categoria': 'Escritorio'
}

# for chave, valor in produto.items():
#     print(chave)

dc = {
    chave.upper(): valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
}


lista = [
    ('a', 'valor a'),
    ('b', 'valor b'),
    ('c', 'valor c'),
]

# dc = {
#     chave: valor
#     for chave, valor in lista
# }
# print(dict(lista))

#Isto foi dictionary_Comprehesion
#Agora Set_Comprehesion

s1 = {i **2 for i in range(10)}
print(s1)
print(set(range(10)))