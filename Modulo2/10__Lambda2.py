def executa(funcao, *args):
    return funcao(*args)



def soma(x, y):
    return x + y

def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

#Exemplo da cria_multiplicador em lambda
duplica = executa(
    lambda m: lambda n: n * m,
    4
)
print(duplica(2))

#Exemplo sobre o que não fazer!
# funcao = lambda parametro: parametro

print (
    #Exemplo da função Soma em lambda
    executa(
        lambda x, y: x+y,
        2, 3
    )    
)

print(
    executa(
        lambda *args: sum(args),
        1, 2, 3,4,5,6,7
    )
)


