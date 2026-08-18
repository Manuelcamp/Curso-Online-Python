import os
listas_compras = []

while True:
    opcao = input("Selecione uma opção\n [i]nserir [a]pagar [l]istar\n")
    
    if(opcao == 'i'):
        elemento = input("Valor: ")
        listas_compras.append(elemento)
        os.system('cls')

    elif(opcao == 'a'):
        indice = input("Qual o indice? ")
        try:
            indice = int(indice)
            del listas_compras[indice]
            os.system('cls')
        except TypeError or ValueError:
            print("Digite apenas números inteiros")
        except IndexError:
            print("Valor de indice não encontrado")
    elif(opcao == 'l'):
        os.system('cls')
        for elemento, indice in enumerate(listas_compras):
            print(elemento, indice)