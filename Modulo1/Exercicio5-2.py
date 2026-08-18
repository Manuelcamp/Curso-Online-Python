horas = input("Olá! que horas são?(em números inteiros!) ")
try:
    horas_int = int(horas)
    if(horas_int <= 11):
        print('Bom dia!')
    elif(horas_int >= 12 and horas_int <= 17):
        print('Boa tarde!')
    else:
        print('Boa noite!')
except:
    print("Digite apenas números inteiros")