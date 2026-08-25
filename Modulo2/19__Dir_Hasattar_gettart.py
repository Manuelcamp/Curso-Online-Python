string = 'Luiz'
metodo = 'upper'

if hasattr(string, metodo):
    print("Existe " + metodo + "!")
    print(getattr(string, metodo)())
else: 
    print("Não existe o método " + metodo)
print(string)

#hasattr(class, method) - confere se o método existe em determinada classe, objeto, variável e etc...
#getattr(class, method) - Executa um método a partir da chamada normal, colocando os dois como parâmetros separados
#dir(string) - no debug console mostra todos os atributos de string