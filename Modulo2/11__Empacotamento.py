# a, b = 1, 2
# a, b = b, a
# print(a, b)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa= {
    'idade': 16,
    'altura': 1.6,
}
print(pessoa, dados_pessoa)
pessoa_completa = {**pessoa, **dados_pessoa}
# print(pessoa_completa)

# a, b =pessoa.values()
# print(a, b)
# a, b = pessoa.items()
# print(a, b)
# (a1, a2), b = pessoa.items()
# print(a1, a2)

def mostro_argumentos_nomeados(*args, **kw_args):
    print('NÃO NOMEADOS:', args)

    for chave, valor in kw_args.items():
        print(chave, valor)

# mostro_argumentos_nomeados(1, 2, nome = 'Joana', qlq=123,)
# mostro_argumentos_nomeados(**pessoa_completa)

config = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}
mostro_argumentos_nomeados(**config)