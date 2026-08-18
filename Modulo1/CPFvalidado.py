#Código focado no primeiro Digito
cpf = "746.824.890-70"
cpf_formatado = cpf.replace(".", "")
cpf_formatado = cpf_formatado.replace("-","")
digito=0
digito2=0

i = 0
b = 10
soma_total = 0
while i < 9:
    soma_total += int(cpf_formatado[i])*b
    i+=1
    b-=1
soma_total*=10
soma_total%=11
if soma_total > 9:
    digito=0
else:
    digito = soma_total
if int(cpf_formatado[9]) == digito:
    print("Primeiro digito válidado!")
else:
    print("Primeiro digito inválido!")

i = 0
b = 11
soma_total = 0
while i < 10:
    soma_total += int(cpf_formatado[i])*b
    i+=1
    b-=1
soma_total*=10
soma_total%=11
if soma_total > 9:
    soma_total=0
    if soma_total == int(cpf_formatado[10]):
        print("Segundo digito válido!")
    else:
        print("Segundo digito inválido!")
else:
    if soma_total == int(cpf_formatado[10]):
        print("Segundo digito válido!")
    else:
        print("Segundo digito inválido!")