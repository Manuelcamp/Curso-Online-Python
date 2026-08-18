import string
frase = 'O Python é uma linguagem de programação '\
    'Multiparadigma. ' \
    'Python foi criado por Guido van Rossum.'

frase_formatada = frase.lower().replace(" ", "")
tamanho_frase = len(frase_formatada)

i=0 
letra_atual = frase_formatada[i]

while i < tamanho_frase - 1:
    i+=1
    indice_atual = frase_formatada[i]
    if frase_formatada.count(letra_atual) < frase_formatada.count(indice_atual):
        letra_atual = indice_atual
print(f'A letra que mais aparece é "{letra_atual}"')