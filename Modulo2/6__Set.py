# s1 = set() #Vazio
# s2= {'Luiz', 1, 2, 3} #Com Dados

# l1 = [1, 2, 2, 2, 2, 3,3,3,1]
# l1 = set(l1)
# l1 = list(l1)
# print(l1) #Forma de longa de remover duplicado em lista, transformando em set depois em list denovo
#Sets não garantem ordem!
#Set é imutavél, e só aceita valores imutáveis
#Sem indices!
# s1 = {1, 2, 3, 4, 5, 6, 7, 7, 7, 7, 2, 2, 2, 3, 3}
# #Sets eliminam naturalmente valores duplicados
# for numero in s1:
#     print(numero)



#Métodos em Set
#Métodos de adicionar
s1= set()
s1.add('Luiz')
s1.add(1)
#Update pode mandar vário valores, mas atenção! Caso mande apenas a frase 'Olá mundo!' será separado cada char da frase
s1.update(('Olá mundo!', 1,2,3,4))
#Limpa tudo no Set
# s1.clear()
#Remove um valor especifico de acordo com oque é passado!
s1.discard('Luiz')
print(s1)
