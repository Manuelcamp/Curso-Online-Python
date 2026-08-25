# print(list(range(10)))

#Forma normal e comum de fazer o acima
# lista = []
# for numero in range(10):
#     lista.append(numero)
# print(lista)

#Método List Comprehension
# lista = [numero for numero in range(10)]
# print(lista)

#É permitido nesse método adicionar lógica no elemento
lista = [
    numero * 2 
    for numero in range(10)]
print(lista)