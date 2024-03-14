"""
Sistema de Arquivos - Manipulação

Fazendo um IF
arquivo_existe = os.path.exists('/etc/hosts.equiv')
if arquivo_existe == True:
    print('arquivo existe!')
else:
    print('Arquivo NAO existe')

# Descobrindo se um arquivo ou diretório existe
# Path absoluto - veja que tanto faz se e diretorio ou arquivo, só precisamos informe o que queremos
print(os.path.exists('/Users/uday/Downloads/tela_simulados.png'))
print(os.path.exists('/Users/uday'))

# Path relativo
print(os.path.exists('fruta.txt'))
print(os.path.exists('arquivo.txt'))
print(os.path.exists('../Uday/Academy'))

# Criando arquivos
# Forma 1
open('arquivo_teste_.txt', 'w').close()

# Forma 2
open('arquivo_teste2_.txt', 'a').close()

# Forma 3 - o pass ele fala cria e não faz mais nada
with open('arquivo_teste3_.txt', 'w') as arquivo:
    pass

NOTA: está forma acima é possivel criar arquivos, mas não é a indicada dependendo da demanda

# Criando arquivo
os.mknod('/dirteste/teste4.txt')

# OBS 1: Para criar arquivos em diretorios o mesmo precisa existir, este comando não cria diretorio
# OBS 2: Se voce estiver a utilizar no Mac OS, pode haver um erro de PermissionErro
# OBS 3: Criando um arquivo via mknod() se o arquivo ja existir teremos o erro FileExistsErro

# Criar diretório (Caminho relativo)
os.mkdir('templates')

# Criar diretório (Caminho absoluto)
os.mkdir('/Users/uday/Downloads/diretorio')

# Obs: A função mkdir() cria um diretório se ele não existir, Caso exista, teremos um FileExistsError

# Criando diretorios de forma recursiva
os.makedirs('teste/tamplate/')

# Se o diretorio existe ele iguinora
os.makedirs('template/teste/teste01', exist_ok=True)

# Renomear arquivos e diretorios
# Diretorios
os.rename('dirteste', 'diretorio')

# Arquivo
os.rename('teste/tamplate/arquivo.txt', 'teste/tamplate/arquivo-renomeado.txt')

# Remover aquivos
os.remove('teste/tamplate/arquivo-renomeado.txt')

# Removendo um diretorio vazio
NOTA: se o diretorio estiver conteudo ele nao remove
os.rmdir('template')

# Remover todos os diretorio
os.removedirs('teste/tamplate')

from send2trash import send2trash

# ATAENÇÃO: ao remover arquivos e diretório com python ele não vão para lixeira, é deletado permanete.
# Mas podemos usar uma biblioteca de terceiro: pip3 install send2trash, envia arquivo e diretorios na lixeira
send2trash('arquivo_teste_.txt')  # Este arquivo vai para a lixeira pode ser restaurado
os.remove('arquivo_teste2_.txt')  # Este arquivo não vai para lixei, não pode ser restaurado

OBS: Se o arquivo nao existir OSerro

# Trabalhando com arquivos e diretórios temporários
import os
import tempfile

# Criando diretorio temporario
with tempfile.TemporaryDirectory() as tmp:   # O with garanre a finalização de recursos abertos.
    print(f'Criei o diretório em {tmp}')     # Aqui estou somplismente mostrando onde ele criou o diretorio
    with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w') as arquivo: # Aqui abrindo o caminho do tmp e criando um arquivo chamado 'arquivo_temporario.txt'
        arquivo.write('Uday Tecnologia\n')  # Aqui estou criando dentro arquivo esta string 'Uday Tecnologia\n'
    input() # Eu preciso deixa algo esperado senao ele executa depois sai.


# Criando arquivo temporario
with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Uday Univertity\n')
    tmp.seek(0)
    print(tmp.read())

# Obs: Em arquivos temporários só conseguimos escrever bits. Por isso, utilizamos b''
"""
