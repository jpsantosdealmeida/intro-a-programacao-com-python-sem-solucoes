# Modifique o programa para que aceite resposta com letras maiúsculas e minúsculas.
'''
pontos = 0
questao = 1
while questao <= 3:
    resposta = input(f'Insira a resposta da questao {questao}: ')
    if questao == 1 and resposta == 'b' :
        pontos += 1
    elif questao == 2 and resposta == 'a':
        pontos += 1
    elif questao == 3 and resposta == 'd':
        pontos += 1
    else:
        pass
    questao += 1
print(f'Aluno fez {pontos} ponto(s)')'''