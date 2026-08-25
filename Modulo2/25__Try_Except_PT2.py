try:
        
    a = 18
    b = '0'
    c = a/b

except(NameError, ZeroDivisionError) as error:
    if error == 'NameError':
        print('Alguns dos nomes das variáveis não está definido!')
    else:
        print("Não é permitido divisão por 0" )
    print('MSG:', error)
    print('MSG', error.__class__.__name__)
except TypeError as e:
    print(e)
except Exception:
    print('Erro desconhecido')
print('Continue')
