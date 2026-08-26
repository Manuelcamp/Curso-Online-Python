# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path
#Para recarregar um módulo importado, caso raro, mas se necessário basta dar (modulo importado).reload() e assim sera recarregado caso tenha mudança de variáveis ou algo do tipo

print('Este módulo se chama', __name__)