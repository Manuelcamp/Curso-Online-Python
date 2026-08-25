
# try:
#     a = 18
#     b = 0
#     print('LLLL')
#     c = a/b
#     print('MMMMM')
# except:
#     ...

# print('Continue')



try:
        
    a = 18
    b = 0
    c = a/b

except ZeroDivisionError:
    print("Não é permitido divisão por 0" )
except NameError:
    print('Alguns dos nomes das variáveis não está definido!')
except TypeError:
    print('Só são permitido operações com números inteiros!')
except Exception:
    print('Erro desconhecido')
print('Continue')

