import sys
#Generator expression
lista = [n for n in range(1000)]
generator = (n for n in range(1000))
print(sys.getsizeof(lista))

#Generator - Uma função que sabe pausar, ele te entrega um valor por vez, mas não tem len() nem como acessar determinada localização, afinal ele não está na memoria
#Navegar sequencialmente é seu objetivo!
print(sys.getsizeof(generator))

for element in generator:
    print(next(generator))
    