def generator(n=0, maximum= 10):
    while True:
        yield n

        n += 1

        if n > maximum:
            return
        

#Yield - pausa a execução da função

gen = generator(maximum=10)
for n in gen:
    print(n)

