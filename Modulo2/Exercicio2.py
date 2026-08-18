# number = input("What is the your number?")
# number = int(number)
# def Two(firstNumber):
#     return firstNumber * 2

# def Three(secondNumber):
#     return secondNumber * 3

# def Four(thirdNumber):
#     return thirdNumber * 4

# def FunctionAll(num): 
#     num = Two(num)
#     num = Three(num)
#     num = Four(num)
#     print(num)
    
# FunctionAll(number)

#Solução Própria, mas, bem mais ou menos :(

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(3))
print(quadruplicar(4))
