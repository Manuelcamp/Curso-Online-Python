perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
       'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25', 
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5', 
        },
]

corrects_answers = 0
for Chave in perguntas:
    Lista = []
    for Key, Value in Chave.items():
        Lista.append(Key)
        Lista.append(Value)
        
    print("\n" + Lista[0] + ": " + Lista[1])
    print("\n" + Lista[2] + ":")
    i = 0
    while i < len(Lista[3]):
        for Option in Lista[3]:
            print(f'{i}) {Option}')
            if(Option == Lista[5]):
                correct_answer = i
                correct_answer = str(correct_answer)
            i+=1
        user_response = input("Escolha uma opção: ")
        if(user_response == correct_answer):
            print("Acertou! 👍")
            corrects_answers += 1
        else:
            print("Errou ❌")
corrects_answers = str(corrects_answers)
qtd_perguntas = str(len(perguntas))
print("\nVocê acertou " + corrects_answers)
print("de " + qtd_perguntas + " perguntas.")

#Que dificuldade para resolver um négocio tão simples, mas oq importa é que fiz sozinho e consegui :)