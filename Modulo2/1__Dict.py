pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'endereços': [
        {'rua': 'tal tal', 'numero': 123},
        {'rua': 'outra rua', 'numero': 321},
    ]
}
pessoa2 = dict(nome='Manuel', sobrenome='Amiranto')
print(pessoa, type(pessoa))
print(pessoa2)
print(pessoa['nome'])

for chave in pessoa:
    print(chave, pessoa[chave])