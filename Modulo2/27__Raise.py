
# def divide(n, d):
#     try:
#         return n/d
#     except ZeroDivisionError:
#         raise ZeroDivisionError('Erro de bulice, fique mais inteligente!')
#         return n

# def divide(n, d):
#     try:
#         return n/d
#     except ZeroDivisionError:
#         raise # Relançando a execeção
#         return n


def naoAceitoZero(d):
    if d == 0:
        raise ZeroDivisionError('Você é a vergonha dos programadores')
    return True
def divide(n, d):
    if naoAceitoZero(d) and naoAceitoZero(n):
        return n/d
    raise ZeroDivisionError('Você está de sacanagem?')
    

    
print(divide(8, 0))


# print(123)
# raise KeyboardInterrupt('Erro no tecrado, comple um glatis na shoupie')
# print(456)