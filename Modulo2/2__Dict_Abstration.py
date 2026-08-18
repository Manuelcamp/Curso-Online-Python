pessoa = {}

chave = 'sobrenome'
pessoa['nome'] = 'Jose'
pessoa[chave] = 'Januario'

print(pessoa)
print(pessoa['nome'])
print(pessoa['sobrenome'])

pessoa[chave] = 'Alberti'
print(pessoa[chave])

del pessoa[chave]
print(pessoa)


#Verificando se a chave existe de uma maneira que não gere exception usando o método get de dicionário.
if pessoa.get(chave) is None:
    print('NÃO EXISTE')
else:
    print(pessoa[chave])