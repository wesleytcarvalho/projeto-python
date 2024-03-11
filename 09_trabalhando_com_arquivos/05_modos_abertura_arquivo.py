"""
Modos de abertura de arquivos
r -> Abre para leitura - padrão
w -> Abre para escrita - sobrescreve caso o arquivo já exista
x -> Abre para escrita somente se o arquivo não existir. Caso o arquivo exista, gere FileExistsError
a -> Abre para escrita, adicionando o conteúdo ao final das frases.
+ -> Abre para o modo de atualização leitura e escrita

# OBS: Abrindo no modo 'a' -> append, se o arquivo não existir será criado. Caso existam, o novo conteúdo
será adicionando SEMPRE ao final arquivo. Com o modo 'a' não controlamos o cursor.

# Exemplo x
try:
    with open('uday.txt', 'x') as arquivo:
        arquivo.write('Teste de conteudo 2. \n')
except FileExistsError:
    print('O Aquivo já existe')

Exemplo a - criando um arquivo até que você ensira sair e adicione no final do arquivo .
with open('escrever_final.txt', 'a') as arquivo:
    while True:
        fruta = input('Digite uma fruta: ')
        if fruta != 'sair':
            arquivo.write(fruta + '\n')
        else:
            break
"""

