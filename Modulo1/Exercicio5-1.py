numero = input("Escreva um número inteiro: ")

try:
    numero_int = int(numero)
    if(numero_int % 2 == 0):
        print("Número par")
    else:
        print("Número impar")
except:
        print('Digite um número inteiro!')