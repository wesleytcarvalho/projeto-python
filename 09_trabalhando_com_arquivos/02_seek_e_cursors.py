"""
Seek e Cursors

- seek() -> A função seek() é utilizada para movimentar o cursor pelo o arquivo aberto. Ele recebe um parâmetro que
indica onde queremos colocar o cursor.

# Exemplo 1
# Como verificamos anteriormente para abrir um arquivo utilizamos
arquivo = open("texto.txt")
# veja que mesmo que eu coloque varios prints ele faz a leitura somente uma vez

# Para ler o arquivo utilizamos
print(arquivo.read())

NOTA: Para você movimentar e iniciar o curso apartir de alguma palavra utilizando a função seek()

# movimentando o cursor, neste caso do seek(17), ele vai iniciar apartir do caracter 17
arquivo.seek(17)
print(arquivo.read())

# readline() -> a função readline() lê o arquivo linha a linha, então se você tem 7 linha de um texto
# você pode colocar 7 prints com o readline()
# print(arquivo.readline())

retorno = arquivo.readline()
print(type(retorno))
print(retorno)
print(retorno.split(' '))

# readlines() - Veja que está no plural então ele cria uma 01_lista com o conteúdo do texto
linhas = arquivo.readlines()
print(len(linhas))

OBS: Quando abrirmos um arquivo com a função open() é criado uma conexão entre o arquivo
no disco do computador e o nosso programa. Essa conexão é chamado de streamig. Ao finalizar
os trabalho com o arquivo devemos fechar essa conexão. Para isso utlizamos a função close()

Passos para se trabalhar com o arquivo
1 - Abrir o arquivo
2 - Trabalhar o arquivo
3 - Fechar o arquivo;

# Exemplos
# 1 - Abrir o arquivo
arquivo = open('texto.txt')
# 2 - Trabalhar o arquivo
print(arquivo.read())
print(arquivo.closed)  # False - Verifica se o arquivo está aberto ou fechado
# 3 - Fechar o arquivo;
arquivo.close()
print(arquivo.closed)  # True - Verifica se o arquivo está aberto ou fechado

# OBS: Se tivermos que manipular os arquivos após ele fechado, teremos o erro ValueError
print(arquivo.read())

arquivo = open('texto.txt')
# Com a função read() é possivel limitar a quantidade de caracteres a serem lidos no arquivo
print(arquivo.read(58))
print(len(arquivo.read(58)))
"""

