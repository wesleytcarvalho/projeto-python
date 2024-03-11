"""
StringIO

ATENÇÃO: Para ler ou escrever dados em arquivo do sistema operacional o software precisa ter permissão
- Permissão de Leitura -> Para ler o arquivo
- Permissão de Escrita -> Para escrever o arquivo

StringIO -> Utilizado para ler ou criar arquivos em memório

# Primeiro fazemos o import
from io import StringIO

mensagem = 'Este é apenas uma string na memória'

# Podemos criar um arquivo em memória já com uma string inserida ou mesmo vazia para inserirmos texto depois
arquivo = StringIO(mensagem)

# Agora tendo o arquivo, podemos utitlizar tudo que já sabemos
print(arquivo.read())

# Escrevendo outro texto
arquivo.write('Outro texto')

# Podemos inclusive movimentar o cursor
arquivo.seek(0)
print(arquivo.read())
"""


