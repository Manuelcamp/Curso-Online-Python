import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1' : [0, 1, 2],
}
d2 = d1
#D2 aponta para o mesmo dicionário que D1

d2['c1'] = '100'
print(d1['c1'])
#Se alterar o d2 vai alterar o d1 também!

d2 = d1.copy()

d2['c1'] = '200'
print(d1['c1'])

#Agora foi uma copia rasa, tudo que não for mutável ele copia em novos dados apra d2

d2['l1'][1] = 900
print(d2['l1'])
print(d1['l1'])

#Pela lista ser mutável, ambos apontam para a mesma lista na memória

d2 = copy.deepcopy(d1)

d2['l1'][1] = 1200
print(d2['l1'])
print(d1['l1'])

#Agora uma deepCopy, uma cópia profunda pelo módulo importado



