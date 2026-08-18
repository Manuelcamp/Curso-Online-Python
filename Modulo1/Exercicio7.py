"""" Calculadora While """

cont = 's'
operadores_validos = '+-*/'
while cont == 's':
    resultado=0
    valor1 =input("Digite o primeiro valor: ")
    valor2 =input("Digite o segundo valor: ")
    operador =input("Digite o seu operador\nSubtração(-) Adição(+) Multiplicação(*) Divisão(/)\nOperador: ")
    
    try:
        valores = float(valor1) and float(valor2)
        numerosValidos = True
    except:
        numerosValidos = None
    if numerosValidos == None:
        print("Um ou ambos os números digitados são inválidos")
        continue

    if operador not in operadores_validos:
        print("Operador inválido.")
        continue
    elif len(operador) > 1:
        print("Digite apenas um operador")
        continue



    if operador == '+':
        resultado = float(valor1) + float(valor2)
    elif operador == '-':
        resultado = float(valor1) - float(valor2)
    elif operador == '*':
        resultado = float(valor1) * float(valor2)
    elif operador == '/':
        resultado = float(valor1) / float(valor2)

    print(resultado)

    cont = input("Deseja continuar? Sim(s) Não(n)")
    cont = cont.lower()