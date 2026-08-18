p1= {
    'nome': 'Luiz',
    'sobrenome': 'Miranda',
}
p2 = {

}

print(p1.get("nome", 'Not Found'))
print(p2.get("nome", 'Not Found'))

#Atribui a variável nome o valor da chave e remove do dicionário original
# nome = p1.pop('nome')
# print(nome)
# print(p1)

#Remove a ultima chave do dicionário
# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)


#Atualiza o nome e também cria nova chaves
# p1.update({
#     'nome': 'Jose',
#     'idade': 30,
# })

#Forma mais simples
# p1.update(nome='Katarino', idade=20)

#Forma usando Tupla
tupla = ('nome', 'Lindovaldo'),
p1.update(tupla)

lista = [['nome', 'lidoskev'], ['idade', 40]]
p2.update(lista)

print(p1)
print(p2)