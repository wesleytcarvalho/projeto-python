"""
O break é muito utilizado quando estamos usando estruturas de repetição
pode ser usado no FOR, WHILE etc.
"""

for a in range(1, 11):
    if a == 10:
        break
    else:
        print(a)
print('Saiu do loop')

# Exemplo com while
while True:
    comando=input('Quer sair? ')
    if comando == 'sim':
        break
    else:
        print('Continuando...')
print('Voce descidu sair! ')