pessoa = {
    'nome': 'Luiz',
    'sobrenome': 'Miranda',
}

print(len(pessoa))

print(tuple(pessoa.keys()))

print(list(pessoa.values()))

print(tuple(pessoa.items()))
# for chave, valor in pessoa.items():
#     print(chave, valor)

pessoa.setdefault('idade', 0)
print(pessoa['idade'])