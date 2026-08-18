nome = input('What is your first name? ')

if nome:
    tamanho_nome = len(nome)
    if(tamanho_nome <= 4):
        print('Your name is short')
    elif(tamanho_nome >= 5 and tamanho_nome <= 6):
        print('Your name is normal')
    else: 
        print('Your name is big')
else:
    print("Write something, please!")