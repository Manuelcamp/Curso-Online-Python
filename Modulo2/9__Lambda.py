# lista = [4, 32, 1, 34, 5, 6, 6, 21]
# lista.sort(reverse=True)
# print(lista)

lista = [
    {'nome': 'Luiz', 'sobrenome': 'Miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

# def orderna(item):
#     return item['sobrenome']

# lista.sort(key=orderna)

#Expressão lambda
def exibir(lista):
    for item in lista:
        print(item)
    print


l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])
exibir(l1)
print()
exibir(l2)
