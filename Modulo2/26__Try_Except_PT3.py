try:
    print('ABRIR ARQUIVO')
    a = 9/0
#Sempre será finalizado, mesmo que ocorra um erro
except ZeroDivisionError:
    print('DIVIDIU 0 :()')
else:
    print('Zero erros')
finally:
    print('FECHAR ARQUIVO')