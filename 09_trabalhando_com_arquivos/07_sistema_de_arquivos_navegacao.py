"""
Sistemas de arquivos e navegação

- Para fazer o uso de manipulação de arquivos do sistema operacional, precisamos importar e fazer uso do módulo os,
modulo os usa posix para acessar as funcionalidades do sitema operacional que é padronizado pelo C e pela normma posix
https://docs.python.org/pt-br/3/library/posix.html

- os -> Operationg systems - Sistema operacional

# Fazendo o import do os
import os

# getcwd() -> Pega o current work directory - diretório de trabalho corrente
# Retorna o path (caminho) absoluto
print(os.getcwd())

# Para voltar para um ponto corrente você pode utilizar a função chdir() observe que se eu repetir este comando
# Ele vai voltando para os diretorios anteriores
os.chdir('..')
print(os.getcwd())

# Repetindo...
os.chdir('..')
print(os.getcwd())

# Podemos checar se um diretorio é absoluto ou ralativo
print(os.path.isabs('/User/uday'))  # este caso é para MacOs

Obs: para usuários Windows
# Se você, infelizmente, estiver ultilizando um computador com Windows
# terá que ter cuidado ao verificar diretórios

print(os.path.isabs('C:\\Users\\Uday'))

# Podemos identificar o sistema operacional com o módulo os
# nos referenciamos o sistema operacional assim: posix - (Macos e Linux), nt (Windows)
print(os.name)

# Podemos ter mais detalhes do sistema operacional
print(os.uname())

# Entrando nos diretorios apartir do diretório corrente Uday
print(os.getcwd()) # Mostrando o diretorio corrente

# Join siguinifica juntar, então ele vai entrando nos diretorios
res = os.path.join(os.getcwd(),  'dirteste')
os.chdir(res)
print(os.getcwd())

# Veja que o os.path.join() recebe dois parâmetros, sendo o primeiro o diretorio atual e o segundo o
# diretorio que será juntado ao atual

# Podemos listar os arquivo e diretórios com o listdir() se voce inserir nada na funcao ele pega os arquivos correntes
print(os.listdir())
# Listando apartir de um diretorio desejado
print(os.listdir("/etc"))
# Podemos verificar a contidade que tem dentro do diretorio
print(len(os.listdir('/etc')))
"""
import os

# Podemos 01_lista os arquivos ou diretorios com mais detalhes com scandir()
# print(os.scandir('/etc'))
# 01_lista = list(os.scandir('/etc'))  # Pode utilizar assim
# ou podemos utilizar igual abaixo para depois fecha
arquivo = os.scandir('/etc')
lista = list(arquivo)
# print(01_lista)

# print(dir(01_lista[0]))  # aqui estou verificando o que temos para trabalhar com estes dados

print(lista[0].inode())  # Cada arquivo tem uma númeração decimal para identificar o mesmo
print(lista[0].is_dir())  # é um diretorio? True
print(lista[0].is_file())  # é um arquivo? False
print(lista[0].is_symlink())  # É um link simbolico? False
print(lista[0].path)  # Caminho ate o arquivo
print(lista[0].stat())   # Estatisticas...
print(lista[0].name)  # nome do arquivo

# Quando utilizamos a função scandir() nós precisamos fecha-lá, assim que abrimos o arquivo e não precisamos mais.
arquivo.close()
