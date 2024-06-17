'''
Modifique o jogo da forca de forma a utilizar uma lista de palavras
No início, pergunte um número e calcule o índice da palavra a utilizar pela fórmula:
indice = (numero * 776) % len(lista_de_palavras).
Ou seja, criamos uma lista
adicionamos palavras a essa lista
perguntamos o índice para selecionar a palavra , por exemplo, se colocarmos 10 palavras poderiamos perguntar "selecione um número de 1 a 10"

numero = int(input('Insira um número de 0 a 4: '))
indice = (numero * 776) % len(lista_de_palavras) # fui fazendo passo a passo para ir ver como ficaria , resultou nisso 
print(f'Indice: {indice}')
print(lista_de_palavras[indice])

'''

