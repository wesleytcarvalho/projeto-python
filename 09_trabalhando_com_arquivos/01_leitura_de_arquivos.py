"""
Leitura de arquivos

Para o conteúdo de uma arquivo em Python, utilizamos a função integrada open(), que lietralmente
siguinifica 'abrir'

open() -> Na forma mais simples de utilização nós passamos apenas um parâmetro de entrada, que neste
caso é o caminho para o arquivo a ser lido. Essa função retorna um _io.TextIOWrapper e é com ele que
trabalhamos.

https://docs.python.org/3/library/functions.html#open

# OBS: Por padrão, a função open() abre o arquivo para leitura. Este arquivo deve existir, ou então teremos o
erro FileNotFoudError

<_io.TextIOWrapper name='texto.txt' mode='r' encoding='UTF-8'>

Veja a linha acima que seria a saída da minha execução para abrir o arquivo
- _io.TextIOWrapper = Tipo de dado
- name='texto.txt' = nome do arquivo que estou abrindo
- mode='r' = ele está abrindo arquivo em MODO LEITURA, r vem de read()
- encoding='UTF-8'> = São para o programa entender assentuação

# Exemplo
arquivo = open('texto.txt')
# print(arquivo)
# print(type(arquivo))

# Para ler o conteúdo de uma arquivo, após a sua abertura, devemos utlizar a função read()

retorno = arquivo.read()
print(type(retorno))
print(retorno)

# OBS: O python, utiliza um recurso para trabalhar com arquivos chamado cursor. Esse cursor,
# funciona como o cursor que estamos escrevendo ele vai lendo linha a linha

# print(arquivo.read())

# Obs A função read() lê todo o conteúdo do arquivo.
"""
