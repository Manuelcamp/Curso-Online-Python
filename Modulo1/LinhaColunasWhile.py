"""" Olá! Código com o objetivo de imitar as colunas e linhas do excel, de maneira bem básica, ao assistir das aulas surgiu a ideia"""
qtd_linha = 5
qtd_coluna = 5

linha = 1

while linha <= qtd_linha:
    print(linha, end="")
    linha+=1
    coluna = 1
    while coluna <= qtd_coluna:
        print(coluna, end="")
        coluna+=1
    coluna = 1
    print("")
