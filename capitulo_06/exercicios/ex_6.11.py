# Modifique o programa abaixo utilizando for e explique porque nem todos os while podem ser transformado em for.
'''
L = []
while True:
    n = int(input('Digite um número (0 sai):' ))
    if n == 0:
        break
    L.append(n)
x = 0
while x < len(L):
    print(L[x])
    x+=1
'''
