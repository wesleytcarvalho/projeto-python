"""
Escreva um script Python para classificar (ascendente e descendente) um dicionário por valor.
"""

dicionario = {'nome': 'Ricardo', 'idade': 34}

ordem = input('Por favor, escolha uma opção de visialização "ascendente e descendente" [a/d]\n')

if ordem == 'a':
    print(dicionario)
elif ordem == 'd':
    print(sorted(dicionario), reverse=True)
else:
    print('Opção incorreta')