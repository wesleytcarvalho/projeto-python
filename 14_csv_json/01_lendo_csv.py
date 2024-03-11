"""
https://dados.mj.gov.br/dataset

Lendo arquivos CSV
CSV - Comma Separeted Values - Valores separados por Virguala

Precisamos definir um padrão para separar nossos dados no CSV se você começa com virtula, termine com virgula
se você começa com ponto e virgula termine com ponto e virgula, o mais apropriado e indicado é a virtula e ponto e
virgula para CSV então vamos seguir assim;



# números
1, 2, 3, 4, 5

# Palavras
'Amanda', 'Raquel', 'Suelem'



# Possivel de se trabalhar, mas não é o ideal para trabalhar
with open('lutadores.csv') as arquivo:
    dados = arquivo.read()
    # print(type(dados))
    dados = dados.split(',')[2:]
    print(dados)



A linguagem Python possui duas formas difrente para ler dados em arquivo CSV:
- reader -> Permite que iteremos sobre as linhas do arquivo CSV como Listas;
- DictReader -> Permite que iteremos sobre as linhas do arquivo CSV como OrderedDicts;



# Reader
from csv import reader

with open('lutadores.csv') as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv)
    for linha in leitor_csv:
        print(f'{linha[0]} nasceu {linha[1]} e mede {linha[2]}')



# DictReader
from csv import DictReader

with open('lutadores.csv') as arquivo:
    leitor_csv = DictReader(arquivo)
    next(leitor_csv)
    for linha in leitor_csv:
        print(f'{linha['Nome']} nasceu {linha['País']} e mede {linha['Altura (em cm)']}')
"""
# DictReader com outro seprador

from csv import DictReader

with open('lutadores.csv') as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=',')
    next(leitor_csv)
    for linha in leitor_csv:
        print(f'{linha['Nome']} nasceu {linha['País']} e mede {linha['Altura (em cm)']}')